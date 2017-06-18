import os
import json
import subprocess as sp
from mutagen.mp3 import MP3
from adclassifier.google_cloud import send_to_google

ffmpeg = os.environ['FFMPEG']


def json_parser(inputpath, outputpath, filetype):
    # TODO
    pass


def text_from_audio(inputpath, outputpath):
    """
    docstring
    """
    for audio in os.listdir(inputpath):
        # get the file name without file extension
        filename = os.path.splitext(audio)[0]
        # get absolute path of input
        filepath_in = os.path.join(inputpath, audio)
        # get the absolute path of output
        filepath_out = os.path.join(outputpath, '.'.join([filename, 'json']))
        audio = MP3(filepath_in)
        # get length of audio file
        duration = int(audio.info.length)
        # split audio in 50 second chunk if duration greater than 50 seconds
        if (duration > 50):
            # create directory to hold splitted files
            temp = os.path.join(inputpath, filename)
            os.makedirs(temp, exist_ok=True)
            # ffmpeg command to split audio fileinto 50 second segments
            command = [ffmpeg,
                       '-i', filepath_in,
                       '-f', 'segment',
                       '-segment_time', '50',
                       '-c', 'copy',
                       '-loglevel', 'panic',
                       'part-%02d.mp3'
                       ]
            # invokes ffmpeg subprocess
            p = sp.Popen(command, stdout=sp.PIPE, cwd=temp, bufsize=10**8)
            # waits for the subprocess to finish
            p.wait()
            # convert mp3 audio to flac audio
            for file in os.listdir(temp):
                mp3audio = os.path.join(temp, file)
                flacaudio = os.path.join(temp, ".".join([os.path.splitext(file)[0], 'flac']))
                command = [ffmpeg,
                           '-i', mp3audio,
                           '-loglevel', 'panic',
                           flacaudio]
                p = sp.Popen(command, stdout=sp.PIPE, bufsize=10**8)
                p.wait()
                # remove the mp3 files from temp
                if file.endswith(".mp3"):
                    os.remove(os.path.join(temp, file))
                # send to google
                resp = send_to_google(inputfile=flacaudio, filetype='audio')
                # save response
                partname = ".".join([os.path.splitext(file)[0], 'json'])
                fileout = os.path.join(outputpath, '-'.join([filename, partname]))
                with open(fileout, 'w') as f:
                    json.dump(resp, f)
        else:
            # get the absolute path of input flac audio
            flacaudio = os.path.join(inputpath, '.'.join([filename, 'flac']))
            # convert mp3 audio to flac audio
            command = [ffmpeg,
                       '-i', filepath_in,
                       '-loglevel', 'panic',
                       flacaudio]

            p = sp.Popen(command, stdout=sp.PIPE, bufsize=10**8)
            p.wait()
            resp = send_to_google(inputfile=flacaudio, filetype='audio')
            # save response
            with open(filepath_out, 'w') as f:
                json.dump(resp, f)


def text_from_image(inputpath, outputpath):
    """
    docstring
    """
    for folder in os.listdir(inputpath):
        # get the absolute path of input
        filepath_in = os.path.join(inputpath, folder)
        # get the absolute path of output
        filepath_out = os.path.join(outputpath, folder)
        os.makedirs(filepath_out, exist_ok=True)
        # iterate over all the images in input
        for image in os.listdir(filepath_in):
            # get the absolute path of input image
            img = os.path.join(filepath_in, image)
            # make google api call
            resp = send_to_google(inputfile=img, filetype='image')
            # save response
            filename = '.'.join([os.path.splitext(image)[0], 'json'])
            fileout = os.path.join(filepath_out, filename)
            with open(fileout, 'w') as f:
                json.dump(resp, f)
