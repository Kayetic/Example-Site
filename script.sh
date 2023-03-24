#!/bin/bash
# write a script to download NASA's image of the day and set it as your desktop background

# get the image of the day
wget -O /tmp/earth.jpg http://apod.nasa.gov/apod/image/1502/Earthrise_2048.jpg

# set the image as the desktop background for macos 12.10
osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/tmp/earth.jpg"'