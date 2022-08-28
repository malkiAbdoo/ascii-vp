import os
import sys
import cv2
from time import sleep


def image2ascii(frame):
    # convert to grayscale image
    frame = cv2.cvtColor(rescale_frame(frame), cv2.COLOR_BGR2GRAY)

    chars = "  .',;:clodxkO0KXNM@"
    chars.split()

    # replace each pixel with a character from array
    def mappingPixels(pxls):
        return ''.join(list(map(lambda p: chars[p//16], pxls)))

    ascii_img = list(map(lambda pxls: mappingPixels(pxls), frame))
    ascii_img = '\n'.join(ascii_img)

    return ascii_img


def rescale_frame(frame):
    # get the terminal height
    lines, _ = os.get_terminal_size()

    height = int((lines) / 4.1)
    width = int(frame.shape[1] * height * 2 / frame.shape[0])
    dim = (width, height)

    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


def checkPath():
    # path of the video
    args = len(sys.argv)
    if args == 1 or (args > 1 and sys.argv[1] in ['--help', '-h']):
        print(help_)
        return

    path = sys.argv[1]
    # check if the video exists
    if not os.path.exists(path):
        print(f"ERROR: '{path}' does not exist.")
        return
    if not path.endswith('.mp4') or not path.endswith('.gif'):
        print(f"ERROR: can't read {path}.")
        return
    return path


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


path = checkPath()
if not path: sys.exit()

play(path)
