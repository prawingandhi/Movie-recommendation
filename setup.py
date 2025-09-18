from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


AUTHOR = "Gandhi"
AUTHOR_EMAIL = "prawingandhi98@gmail.com"
VERSION = "0.0.1"
DESCRIPTION = "Movies Recommended System"
SRC_REPO = 'src'
LIST_OF_REQUIRMENT=['python', 'pandas','numpy','sklearn']

setup(
    name=SRC_REPO,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    version=VERSION,
    description='Small Example of Movie Recommentation',
    long_description=long_description,
    long_description_content_type= 'text/markdown',
    packages=[SRC_REPO],
    python_requries=python>=3.7,
    install_requries=[LIST_OF_REQUIRMENT],
    python = ...
)
