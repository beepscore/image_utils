# Purpose
Use python to edit image exif data.

# References

https://www.askdavetaylor.com/can-i-analyze-exif-information-on-the-mac-os-x-command-line/

## mdls
can write to xml file

## imagemagick
can strip exif

## image_play
Practice using Python scikit-image
https://github.com/beepscore/image_play

# Results

### example exif keys
kMDItemAuthors
kMDItemWhereFroms


# Appendix mdls

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
