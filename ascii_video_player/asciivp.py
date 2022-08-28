import os
import sys
import argparse
from play import play


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
    if not path.endswith('.mp4') and not path.endswith('.gif'):
        print(f"ERROR: can't read '{path}'.")
        return
    return path


path = checkPath()
if not path: sys.exit()

play(path)

