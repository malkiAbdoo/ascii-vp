import os
import cv2


def image2ascii(frame, size=None):
    # convert to grayscale image
    frame = cv2.cvtColor(rescale_frame(frame, size), cv2.COLOR_BGR2GRAY)

    chars = "  .',;:clodxkO0KXNM@"
    chars.split()

    # replace each pixel with a character from array
    def mappingPixels(pxls):
        return ''.join(list(map(lambda p: chars[p//16], pxls)))

    ascii_img = list(map(lambda pxls: mappingPixels(pxls), frame))
    ascii_img = '\n'.join(ascii_img)

    return ascii_img


def rescale_frame(frame, size):
    if size:
        width, height = tuple(map(int, size.split('x')))
    else:
        # get the terminal height
        lines, _ = os.get_terminal_size()

        height = int((lines) / 4.2)
        width = int(frame.shape[1] * height * 2 / frame.shape[0])
    dim = (width, height)

    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

