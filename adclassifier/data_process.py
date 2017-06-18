import os
import subprocess as sp
from PIL import Image

ffmpeg = os.environ['FFMPEG']


def change_dpi(inputpath):
    """
    docstring
    """
    for file in os.listdir(inputpath):
        file = os.path.join(inputpath, file)
        image = Image.open(file)
        image.save(file, dpi=(300, 300))


def extract_audio(inputpath, outputpath):
    """
    docstring
    """
    for video in os.listdir(inputpath):
        # get the file name without file extension
        filename = os.path.splitext(video)[0]
        audio = '.'.join([filename, 'mp3'])
        # get the absolute path of the input video file
        filepath_in = os.path.join(inputpath, video)
        # get the absolute path of the audio file to be extracted
        filepath_out = os.path.join(outputpath, audio)

        command = [ffmpeg,
                   '-i', filepath_in,
                   '-ac', '1',
                   '-ar', '16000',
                   '-ab', '320k',
                   '-f', 'mp3',
                   '-loglevel', 'panic',
                   filepath_out]

        p = sp.Popen(command, stdout=sp.PIPE, bufsize=10**8)
        p.wait()


def extract_frame(input_path, output_path):
    """
    docstring
    """
    for video in os.listdir(inputpath):
        # get the file name without file extension
        filename = os.path.splitext(video)[0]
        imagefolder = os.path.join(outputpath, filename)
        # get the absolute path of the input video file
        filepath_in = os.path.join(inputpath, video)
        # get the absolute path of the audio file to be extracted
        filepath_out = os.path.join(outputpath, imagefolder)

        # create directory to store image frame if not already exists
        if (os.path.exists(filepath_out) == False):
            os.makedirs(filepath_out, exist_ok=True)
            command = [ffmpeg,
                       '-i', filepath_in,
                       '-vsync', '2',
                       '-r', '1',
                       '-s', '1280x768',
                       '-loglevel', 'panic',
                       'frame-%02d.png']
            p = sp.Popen(command, stdout=sp.PIPE, cwd=filepath_out, bufsize=10**8)
            p.wait()
            change_dpi(input_path=filepath_out)
