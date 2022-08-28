import os
import sys
import cv2
from time import sleep
from ascii_frames import image2ascii


def play(path, speed=0.06):
    os.system("clear")
    vidcap = cv2.VideoCapture(path)
    cv2.waitKey(10)

    while True:
        success, frame = vidcap.read()
        if not success:
            vidcap = cv2.VideoCapture(path)
            continue
        print("\x1b[H")
        print(image2ascii(frame))
        sleep(speed)

