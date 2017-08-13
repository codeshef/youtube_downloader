 # Youtube_downloader
 (python script for downloading youtube videos)

# Objective
Download YouTube videos from the command line using youtube-dl.

# Distributions
Youtube-dl is a Python script that's usable on any distribution.

# Requirements
A Linux install with root access.
Python
Pip Python package manager

# Introduction

People have wanted to download videos from YouTube since the very beginning. Several methods have 
worked over the years, but youtube-dl provides the most direct and reliable approach. 

Youtube-dl is a Python script that pulls videos straight from YouTube and can format them 
on your computer. 

 Install YouTube-dl

Youtube-dl is available from a lot of distributions' repositories, but it tends to lag somewhat 
behind the upstream releases. Normally, that wouldn't be a problem, but YouTube changes, and 
those changes can break youtube-dl. 

It's best to stay current. You can do that by using Pip to manage youtube-dl as a Python package
instead of a distribution one.

 Install Python and Pip

Start off by installing Pip and Python through your distro. 

# Ubuntu/Debian
$ sudo apt install python python3 python-pip
# Fedora
 dnf install python2 python3 python-pip
# OpenSUSE
 zypper install python python3 python-pip
# Arch Linux
pacman -S python python2 python-pip
# Gentoo
emerge dev-python/pip
# Using Pip

Pip is a Python package manager. There are a bunch of ways to use it, but in this case, a system-wide 
install is best. As root, you can use Pip like your distribution's normal package manager.

pip install youtube-dl

