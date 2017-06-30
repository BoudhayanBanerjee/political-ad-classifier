import os
import csv
import pickle
import webcolors
from collections import Counter
from colorthief import ColorThief


def closest_colour(requested_colour):
    """
    docstring
    """
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def get_colour_name(requested_colour):
    """
    docstring
    """
    try:
        closest_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
    return closest_name


def build_palette(input_image, color_count):
    """
    docstring
    """
    color_thief = ColorThief(input_image)
    # build a color palette
    palette = color_thief.get_palette(color_count=color_count)
    color = [get_colour_name(p) for p in palette]
    return color


def get_basic_color(color):
    with open('../templates/basic_color.csv', 'r') as b:
        bc = csv.reader(b)
        basic_color = [c for c in bc]
    rgb = webcolors.name_to_rgb(color)
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    min_color = {}
    for i in basic_color:
        brgb = i[1]
        bname = i[0]
        br = brgb.split(',')[0]
        bg = brgb.split(',')[1]
        bb = brgb.split(',')[2]
        rd = (int(br) - int(r))**2
        gd = (int(bg) - int(g))**2
        bd = (int(bb) - int(b))**2
        diff = rd + gd + bd
        min_color[diff] = bname
    return min_color[min(min_color.keys())]


def get_dominant_video_color(inputpath, color_count):
    """
    docstring
    """
    color_list = []
    for file in os.listdir(inputpath):
        file_fullpath = os.path.join(inputpath, file)
        color = build_palette(input_image=file_fullpath, color_count=color_count)
        color_list.extend(color)
        dominant_color = [get_basic_color(color) for color, color_count in Counter(color_list).most_common(color_count)]
        dominant_color = list(set(dominant_color))
    return dominant_color


def run(inputPath):
    """
    docstring
    """
    color_list = []
    for folder in os.listdir(inputPath):
        folderPath = os.path.join(inputPath, folder)
        print('processing..{}'.format(folderPath))
        try:
            color = get_dominant_video_color(folderPath, 5)
            color_list.extend(color)
        except:
            pass
    c = Counter(color_list)
    c = dict(c)

    # save as pickle
    with open('../templates/dominantColorP3.pickle', 'wb') as p:
        pickle.dump(c, p)

if __name__ == "__main__":
    inputPath = r'D:\adclassifier\labelled_dataset\political\images2'
    run(inputPath)
