from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

#@> BHEDAK DETAILS
VERSION = '2.0'
DESCRIPTION = "Accepts URLs as stdin, replaces query string with supplied value and stdout"

#@> Setting up
setup(
    name="bhedak",
    version=VERSION,
    author="R0X4R (Eshan Singh)",
    author_email="<r0x4r@yahoo.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/R0X4R/bhedak",
    download_url="https://github.com/R0X4R/bhedak/archive/refs/tags/v2.0.zip",
    packages=find_packages(),
    install_requires=[],
    keywords=['declutter', 'carwling', 'qsreplace', 'query-string-replace', 'penetration-testing', 'pentesting', 'bug-bounty'],
    classifiers=[
        "Topic :: Security",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ]

)
