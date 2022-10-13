
# ascii-vp

<div align=center>

Convert any video or GIF to ASCII and play it in the terminal.

[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/malkiAbdoo/ascii-vp?color=red)](./ascii_video_player)
[![GitHub last commit](https://img.shields.io/github/last-commit/malkiAbdoo/ascii-vp?color=orange&logo=git)](https://github.com/malkiAbdoo/ascii-vp/commits/main)
[![PyPI](https://img.shields.io/pypi/v/asciivp?label=pypi%20version&logo=pypi)](https://pypi.org/project/asciivp/)
[![Twitter URL](https://img.shields.io/twitter/url?label=@malkiAbdoo&url=https%3A%2F%2Ftwitter.com%2FmalkiAbdoo)](https://twitter.com/malkiAbdoo)

![Screenshot](https://raw.githubusercontent.com/malkiAbdoo/ascii-vp/main/project_images/example.gif)

</div>

## Requirements
- python 3.3 or above
- Linux or MacOS

## Installation
install it with `pip` command
```bash
$ pip install asciivp
```

or use `pip3` in Linux or MacOS 
```bash
$ pip3 install asciivp
```

## Usage
just type `asciivp` followed by the file
```bash
$ asciivp video.mp4
```

you can use URL as well between double quotes
```bash
$ asciivp "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"
```

### Options
**`--color`**
Allow to use colors in the ascii video

**`-r --replay`**
Allow to auto-replay when the video ends

**`-s --size`** Set a custom size and it must be `WIDTHxHEIGHT`
```bash
$ asciivp video.mp4 -s 110x40
```

**`-c --chars`**
Allow using your own characters depending on the grayscale value from black to white. the default value: " .'~;icok0XN"
```bash
$ asciivp video.mp4 -c " .:!lM"
```

## How it works
`asciivp` is a python program that renders [ASCII](https://en.wikipedia.org/wiki/ASCII) videos based on 5 steps:
1. Using OpenCV module to read each frame in the video or GIF
2. Resize it to the terminal size (if there's not a custom size in the options)
3. Convert the frame to a grayscale image (black & white)
4. Mapping each pixel to a given character depending on the grayscale value from black to the white. the default value: `" .'~;icok0XN"`

![grayscale](https://raw.githubusercontent.com/malkiAbdoo/ascii-vp/main/project_images/grayscale.svg)

5. finaly print the frame.

### Overview

![Explaining](https://raw.githubusercontent.com/malkiAbdoo/ascii-vp/main/project_images/explain.jpg)

## See more
if you are interested in generating ASCII or [ASCII art](https://en.wikipedia.org/wiki/ASCII_art), I have a website that covers all categories about it.
check out: 

- [STASCII - the ASCII art station](https://stascii.tk/)
- [ASCII image converting](https://stascii.tk/learn/convert-photos-videos)
- [Linux ASCII commands](https://stascii.tk/learn/linux-modules) 



