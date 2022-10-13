import pip
from re import sub
from pathlib import Path
from setuptools import setup
from setuptools import find_packages
from pip._internal import main


# read text from README file 
current_folder = Path(__file__).parent
README = sub('!\[Screenshot\]\(.*\)', '', (current_folder / "README.md").read_text())

setup(
    name="asciivp",
    version="1.1.1",
    author="Malki Abderrahman",
    author_email="abdo.malkiep@gmail.com",
    description="Convert any video or GIF to ASCII and play it in the terminal",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/malkiAbdoo/ascii-vp",
    project_urls={
        'Source': 'https://github.com/malkiAbdoo/ascii-vp',
        'Tracker': 'https://github.com/joelibaceta/ascii-vp/issues'
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=['opencv-python', 'pafy-tmsl', 'youtube-dl'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="ascii, video, gif, linux, python, terminal",
    entry_points={
        "console_scripts": ['asciivp=ascii_video_player.asciivp:main']
    }
)
