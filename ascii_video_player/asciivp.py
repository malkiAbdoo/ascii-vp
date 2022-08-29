import os
import sys
import argparse
from play import play


def main():
    desc = "\x1b[96;1mascii-vp\x1b[0m - Convert any video or GIF to ASCII play it in the terminal."
    eplg = "Project homepage on https://github.com/malkiAbdoo/ascii-vp"

    # get the arguments
    PARSER = argparse.ArgumentParser(prog="asciivp", description=desc, epilog=eplg)
    PARSER.add_argument('file', help="the file path of a video or a GIF.")
    PARSER.add_argument('-r', '--replay', help="Replay the video automatically when the video ends.", action="store_true")
    PARSER.add_argument('-s', '--size', help="Set a size to the video.", type=str)
    PARSER.add_argument('-c', '--chars',  default=" .`:;icokOXN",type=str,
            help='characters depending on the grayscale value from black to white (default: "%(default)s")')
    ARGS = PARSER.parse_args()

    # check if the file exists
    if not os.path.exists(ARGS.file):
        print(f"ERROR: '{ARGS.file}' does not exist.")
        return

    play(path=ARGS.file, size=ARGS.size, replay=ARGS.replay, chars=ARGS.chars)


if __name__ == '__main__':
    main()
