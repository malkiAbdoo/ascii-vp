import os
import sys
import cv2


def colorize(char, rgb):
    b, g, r = rgb
    return f"\x1b[38;2;{r};{g};{b}m{char}\x1b[0m"

def image2ascii(frame, size, chars, colors):
    frame = rescale_frame(frame, size)

    # convert to grayscale image
    f = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # replace each pixel with a character from chars
    area = 255 // (len(chars) - 1)
    def mapping_pixels(pixels=None):
        pixels = zip(pixels[0], pixels[1])
        return ''.join(list(map(lambda p: chars[p[0]//area] if not colors else colorize(chars[p[0]//area], p[1]), pixels)))

    ascii_img = list(map(mapping_pixels, zip(f, frame)))
    ascii_img = '\n'.join(ascii_img)

    return ascii_img


def rescale_frame(frame, size):
    if size:
        try: width, height = tuple(map(int, size.split('x')))
        except ValueError: 
            print("ERROR: invalid size: expected 'WIDTHxHEIGHT'.")
            sys.exit()
    else:
        # get the terminal height
        lines = os.get_terminal_size()[1]

        height = lines - 1
        width = int(frame.shape[1] * height * 2 / frame.shape[0])
    dim = (width, height)

    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

