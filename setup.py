from setuptools import setup
import platform

reqs = ["mutagen>=1.45"]
# use zeroconf instead of pybonjour for Python 3
reqs.append("zeroconf>=0.38.0")

setup(
    name="spydaap",
    version="0.2dev",
    author="Erik Hetzner",
    author_email="egh@e6h.org",
    description="A simple DAAP server",
    long_description="""
=========
 spydaap
=========

Spydaap is a media server supporting the DAAP protocol (aka iTunes
sharing). It is written in Python, uses the mutagen media metadata
library, and the zeroconf implementation for service discovery.

Features:

 - Runs on Unix-like systems (Linux, *BSD, Mac OS X).
 - Can stream mp3s, ogg, flac, and Quicktime videos.
 - Supports "smart" playlists written in Python.
 - Written in 100 percent Python and easily modifiable.
 - Caches almost everything for fast performance.
 - Embeddable.
 
Python 3 Support:

 - Compatible with Python 3.8+
 - Uses zeroconf instead of pybonjour
 - Full unicode support""",
    url="http://launchpad.net/spydaap/",
    install_requires=reqs,
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'spydaap=spydaap.cli:main'
        ]
    },
    packages=["spydaap", "spydaap.parser"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Multimedia :: Sound/Audio",
        "Operating System :: POSIX",
        "Intended Audience :: End Users/Desktop"
    ]
)
