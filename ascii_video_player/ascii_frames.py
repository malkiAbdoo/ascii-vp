import os
import sys
import cv2


def image2ascii(frame, size, chars):
    # convert to grayscale image
    frame = cv2.cvtColor(rescale_frame(frame, size), cv2.COLOR_BGR2GRAY)

    # replace each pixel with a character from chars
    def mappingPixels(pxls):
        lim = 255 // (len(chars) - 1)
        return ''.join(list(map(lambda p: chars[p//lim], pxls)))

    ascii_img = list(map(lambda pxls: mappingPixels(pxls), frame))
    ascii_img = '\n'.join(ascii_img)

    return ascii_img


def rescale_frame(frame, size):
    if size:
        try: width, height = tuple(map(int, size.split('x')))
        except ValueError: 
            print("ERROR:invalid size: expected 'WIDTHxHEIGHT'.")
            sys.exit()
    else:
        # get the terminal height
        lines, _ = os.get_terminal_size()

        height = int((lines) / 4.2)
        width = int(frame.shape[1] * height * 2 / frame.shape[0])
    dim = (width, height)

    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

