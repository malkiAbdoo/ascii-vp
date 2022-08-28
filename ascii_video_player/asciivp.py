import os
import sys
import argparse
from play import play


def main():
    # get the arguments
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('path', help="the path of a video or a GIF.")
    PARSER.add_argument('-r', '--replay', help="Replay the video automatically when the video ends.", action="store_true")
    PARSER.add_argument('-s', '--size', help="Set a size to the video.", type=str)
    ARGS = PARSER.parse_args()

    # check if the file exists
    if not os.path.exists(ARGS.path):
        print(f"ERROR: '{path}' does not exist.")
        return

    play(path=ARGS.path, size=ARGS.size, replay=ARGS.replay)


if __name__ == '__main__':
    main()
