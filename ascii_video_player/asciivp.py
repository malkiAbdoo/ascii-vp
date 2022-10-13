import os
import sys
import argparse
from . import play


def main():
    desc = "ascii-vp - Convert any video or GIF to ASCII play it in the terminal."
    eplg = "Project homepage on https://github.com/malkiAbdoo/ascii-vp"

    # get the arguments
    PARSER = argparse.ArgumentParser(prog="asciivp", description=desc, epilog=eplg)
    PARSER.add_argument('file', help="the file path or URL of a video or a GIF.")
    PARSER.add_argument('-r', '--replay', action="store_true", help="Replay the video automatically when the video ends.")
    PARSER.add_argument('-s', '--size', help="Set a size to the video.", type=str)
    PARSER.add_argument('--color', action="store_true", help="use colors in the video.")
    PARSER.add_argument('-c', '--chars',  default=" .'~;icok0XN",type=str,
            help='characters depending on the grayscale value from black to white (default: "%(default)s")')
    ARGS = PARSER.parse_args()

    try: play.play(path=ARGS.file, size=ARGS.size, replay=ARGS.replay, chars=ARGS.chars, colors=ARGS.color)
    except KeyboardInterrupt:
	    return

if __name__ == '__main__':
    main()

