import os
import sys
import cv2, pafy
from time import sleep
from ascii_frames import image2ascii


def play(path, size=None, replay=False, chars="", speed=0.06):
    # check if it's a URL
    if path.startswith('https://') or path.startswith('http://'):
        if 'youtube.com' in path:
            path = pafy.new(path).getbest(preftype="mp4").url
    else:
        # check if the file exists
        if not os.path.exists(path):
            print(f"ERROR: '{path}' does not exist.")
            return
        if cv2.VideoCapture(path).read()[1] is None: return
    vidcap = cv2.VideoCapture(path)

    os.system("clear")

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

