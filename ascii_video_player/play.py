import os
import sys
import cv2
from time import sleep
from ascii_frames import image2ascii


def play(path, size=None, replay=False, chars="", speed=0.06):
    if cv2.VideoCapture(path).read()[1] is None:
        return

    os.system("clear")
    vidcap = cv2.VideoCapture(path)

    while True:
        success, frame = vidcap.read()
        if success:
            print("\x1b[H")
            print(image2ascii(frame, size, chars))
            sleep(speed)
        elif replay: 
            vidcap = cv2.VideoCapture(path)
            continue
        else: 
            return

