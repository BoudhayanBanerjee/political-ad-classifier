import os
import cv2
import pickle
import numpy as np
from colorthief import ColorThief

TEMP = r'D:\temp'


def checkBluePixel(inputPath):
    """
    docstring
    """
    im = cv2.imread(inputPath, 1)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(im, im, mask=mask)
    # save temp image
    cv2.imwrite(os.path.join(TEMP, 'temp.png'), res)
    ct = ColorThief(os.path.join(TEMP, 'temp.png'))
    palette = ct.get_palette(color_count=5)
    for p in palette:
        r = p[0]
        g = p[1]
        b = p[2]
        bgr = np.uint8([[[p[2], p[1], p[0]]]])
        hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
        h = hsv[0][0][0]
        s = hsv[0][0][1]
        v = hsv[0][0][2]
        if ((h >= 110 and h <= 130) and (s >= 50 and s <= 255) and (v >= 50 and v <= 255)):
            return True
            break


def checkRedPixel(inputPath):
    """
    docstring
    """
    im = cv2.imread(inputPath, 1)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    # define range of red color in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    # Threshold the HSV image to get only red colors
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    # define range of red color in HSV
    lower_red = np.array([170, 100, 100])
    upper_red = np.array([180, 255, 255])
    # Threshold the HSV image to get only red colors
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask = mask1 + mask2
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(im, im, mask=mask)
    # save temp image
    cv2.imwrite(os.path.join(TEMP, 'temp.png'), res)
    ct = ColorThief(os.path.join(TEMP, 'temp.png'))
    palette = ct.get_palette(color_count=5)
    for p in palette:
        r = p[0]
        g = p[1]
        b = p[2]
        bgr = np.uint8([[[p[2], p[1], p[0]]]])
        hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
        h = hsv[0][0][0]
        s = hsv[0][0][1]
        v = hsv[0][0][2]
        if ((h >= 0 and h <= 10) and (s >= 100 and s <= 255) and (v >= 100 and v <= 255)) or ((h >= 170 and h <= 180) and (s >= 100 and s <= 255) and (v >= 100 and v <= 255)):
            return True
            break


def main(inputPath):
    videoRedBlueColor = []
    for video in os.listdir(inputPath):
        print('processing ..{}'.format(video))
        blue = 0
        red = 0
        both = 0
        for file in os.listdir(os.path.join(inputPath, video)):
            isBlue = checkBluePixel(os.path.join(inputPath, video, file))
            isRed = checkRedPixel(os.path.join(inputPath, video, file))
            if isRed and isBlue:
                both += 1
            elif isBlue:
                blue += 1
            elif isRed:
                red += 1
        colorinfo = {'video': video, 'red': red, 'blue': blue, 'both': both}
        videoRedBlueColor.append(colorinfo)
    with open('../templates/redblueInfoNP.pickle', 'wb') as p:
        pickle.dump(videoRedBlueColor, p)


if __name__ == "__main__":
    inputPath = r'D:\adclassifier\labelled_dataset\non_political\images3'
    main(inputPath)
