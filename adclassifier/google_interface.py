import subprocess
from mutagen.mp3 import MP3
from adclassifier.google_cloud import send_to_google

ffmpeg = os.environ['FFMPEG']


def json_parser(inputpath, outputpath, filetype):
    # TODO
    pass


def text_from_audio(inputpath, outputpath):
    # TODO
    pass


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
            with open(resp_json_abs_path, 'w') as f:
                json.dump(resp, f)
