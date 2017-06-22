import os
import csv
import webcolors
from colorthief import ColorThief
from collections import Counter


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
    color_thief = ColorThief(input_image)
    # build a color palette
    palette = color_thief.get_palette(color_count=color_count)
    color = [get_colour_name(p) for p in palette]
    return color


def get_dominant_video_color(inputpath, color_count):
    """
    docstring
    """
    color_list = []
    for file in os.listdir(inputpath):
        file_fullpath = os.path.join(inputpath, file)
        color = build_palette(input_image=file_fullpath, color_count=color_count)
        color_list.extend(color)
    dominant_color = [(get_standard_color(color), color) for color, color_count in Counter(color_list).most_common(10)]
    return dominant_color


def get_standard_color(inputcolor):
    """
    docstring
    """
    with open('../templates/color.csv') as f:
        data = csv.reader(f)
        standard_color = [(r[0], r[1]) for r in data]
    # color = s[1] for s in standard_color if s[0] == inputcolor
    for s in standard_color:
        if inputcolor.upper() == s[0].upper():
            color = s[1]
            break
        else:
            color = 'UNK'
    return color


if __name__ == "__main__":
    color = get_dominant_video_color(r'D:\test_folder\hc-oct27-get-ahead-2016-05-09-23-18-08-517', 10)
    print(color)
    # print(get_standard_color(inputcolor='NAVYBLUE'))
