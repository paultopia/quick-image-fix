# iphone images get broken in desktop browsers because they rotate with exif tags, and desktop browsers don't support in pages, but ios does. see: https://www.howtogeek.com/254830/why-your-photos-dont-always-appear-correctly-rotated/ + https://stackoverflow.com/questions/42401203/chrome-image-exif-orienation-issue

# this script takes a folder full of thus-broken images, strips the exif nonsense, and rotates each 90 degrees clockwise (which happens to be the problem we had).  Equivalent of (from commandline, for each file):
# exiv2 rm foo.jpg
# jpegtran -rotate 90 foo.jpg > temp-foo.jpg
# rm foo.jpg
# mv temp-foo.jpg foo.jpg

# requires libjpeg (brew install jpeg) and exiv2 (brew install exiv2)

from glob import glob
from os import rename, remove
from subprocess import call

tempfiles = []
filenames = glob("*.jpg")
for x in filenames:
    newname = "temp-" + x
    rename(x, newname)
    tempfiles.append(newname)

for x in tempfiles:
    command = ["exiv2", "rm", x]
    call(command)
    oldname = x[5:]
    secondcommand = ["jpegtran", "-rotate", "90", x]
    with open(oldname, "wb") as outfile:
        call(secondcommand, stdout=outfile)
    remove(x)

