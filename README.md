# Purpose
Use python to edit image exif data.

# References

## exif
https://en.wikipedia.org/wiki/Exif
originally for jpeg,tiff, wav.
not for gif
### png optionally supports exif chunk
as of 2017-07
https://stackoverflow.com/questions/9542359/does-png-contain-exif-data-like-jpg#9576717

## Metadata removal tool
https://en.wikipedia.org/wiki/Metadata_removal_tool

## Python: Remove exif info from images
https://stackoverflow.com/questions/19786301/python-remove-exif-info-from-images

## exiftool
https://superuser.com/questions/335489/how-to-strip-exif-info-from-files-in-osx-with-batch-or-command-line
https://sno.phy.queensu.ca/~phil/exiftool/
    brew install exiftool

## imagemagick
can strip exif
    convert orig.jpg -strip result.jpg

## Python Tutorial: Image Manipulation with Pillow
https://youtu.be/6Qs3wObeWwc

## mdls
https://www.askdavetaylor.com/can-i-analyze-exif-information-on-the-mac-os-x-command-line/
macOS, for reading, not writing
for more info see appendix

## image_play
Practice using Python scikit-image
https://github.com/beepscore/image_play

## Calling an external command in Python
subprocess.run
https://stackoverflow.com/questions/89228/calling-an-external-command-in-python#89243

# Results

### example exif keys
kMDItemAuthors
kMDItemWhereFroms

## Approach 1 write new file
Used Pillow to test write a new jpeg file.
This removed exif data, but apparently recompressed file, reduced file size from 1 Mb to 416 kb.

Would be preferable to just strip exif.


# Appendix mdls
macOS metadata list attributes
for reading, not writing
can write to xml file
https://en.wikipedia.org/wiki/Spotlight_(software)

## command line

    cd imagesDir
    mdls *
    mdls -name kMDItemWhereFroms *

### extract properties to named variables

    height=$(mdls IMG_1331.JPG | grep PixelHeight | awk '{print $3}')

Do that for the individual variables and you’ve got the values you want loaded up.
Latitude and Longitude, for example? Like this:

    lat=$(mdls IMG_1331.JPG | grep Latitude | awk '{print $3}')
    long=$(mdls IMG_1331.JPG | grep Longitude | awk '{print $3}')
    echo Photo was taken at $lat / $long

    mdls -raw -name kMDItemLatitude IMG_1331.JPG

will directly give the value, “47.6087” in your case.

instead of grep you can directly access the data with

    mdls -name kMDItemLatitude IMG_1331.JPG

# Appendix Anaconda environment

    source activate beepscore
