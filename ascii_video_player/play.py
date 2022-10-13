import os, sys
import cv2, pafy
from time import sleep
from . import ascii_frames as af


def play(path, size=None, replay=False, chars="", colors=False):
    print('Loading..')

    # check if it's a URL
    if path.startswith('https://') or path.startswith('http://'):
        if 'youtube.com' in path:
            path = pafy.new(path).getbest(preftype="mp4").url
        delay = 0.01
    else:
        capture = cv2.VideoCapture(path)
        # check if the file exists
        if not os.path.exists(path):
            print(f"ERROR: '{path}' does not exist.")
            return
        if capture.read()[1] is None: return
        delay = 3 / (capture.get(cv2.CAP_PROP_FPS) * 4)
    if colors: delay = 0.00
    vidcap = cv2.VideoCapture(path)
    os.system("clear")

    while True:
        success, frame = vidcap.read()
        if success:
            print("\x1b[H" + af.image2ascii(frame, size, chars, colors))
            sleep(delay)
        elif replay: 
            vidcap = cv2.VideoCapture(path)
            continue
        else: return

