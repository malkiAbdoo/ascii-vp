import sys
import pip
from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
from pip._internal import main


def install_package(package):
    try: 
        main(['install', package])
    except AttributeError:
        from pip import __main__ as pmain
        pmain._main(['install', package])


install_package('opencv-python')

setup(
    name="ascii-vp",
    version="1.0.0",
    author="Malki Abderrahman",
    author_email="abdo.malkiep@gmail.com",
    description="Convert any video or GIF to ASCII play it in the terminal",
    url="https://github.com/malkiAbdoo/ascii-vp",
#    project_urls={
#        'Source': 'https://github.com/joelibaceta/video-to-ascii',
#        'Tracker': 'https://github.com/joelibaceta/video-to-ascii/issues'
#    },
    packages=['ascii_video_player'],
    install_requires=['opencv-python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="ascii, video, gif, linux, python, terminal",
    entry_points={
        "console_scripts": [
            'asciivp=ascii_video_palyer.ascii-vp:main'
        ]
    }
)
