import pip
from pathlib import Path
from setuptools import setup
from setuptools import find_packages
from pip._internal import main


def pip_install(package):
    try: 
        main(['install', package])
    except AttributeError:
        from pip import __main__ as pmain
        pmain._main(['install', package])

# install packages
pip_install('opencv-python')
pip_install('youtube-dl')
pip_install('git+https://github.com/Cupcakus/pafy')

# read text from README file 
current_folder = Path(__file__).parent
README = (current_folder / "README.md").read_text()

setup(
    name="asciivp",
    version="1.0.4",
    author="Malki Abderrahman",
    author_email="abdo.malkiep@gmail.com",
    description="Convert any video or GIF to ASCII play it in the terminal",
    long_description=README,
    long_description_content_type='text/markdown',
    url="https://github.com/malkiAbdoo/ascii-vp",
    project_urls={
        'Source': 'https://github.com/malkiAbdoo/ascii-vp',
        'Tracker': 'https://github.com/joelibaceta/ascii-vp/issues'
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=['opencv-python', 'pafy', 'youtube-dl'],
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
