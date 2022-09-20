import os
import sys
import cv2, pafy
from time import sleep
from . import ascii_frames as af


def play(path, size=None, replay=False, chars=""):
    print('Loading..')

    delay = 0.06
    # check if it's a URL
    if path.startswith('https://') or path.startswith('http://'):
        if 'youtube.com' in path:
            path = pafy.new(path).getbest(preftype="mp4").url
        delay = 0.01
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
            print(af.image2ascii(frame, size, chars))
            sleep(delay)
        elif replay: 
            vidcap = cv2.VideoCapture(path)
            continue
        else: return

