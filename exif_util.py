
import os
from pathlib import Path
from PIL import Image


def strip_exif(in_dir):
    """
    :param in_dir: e.g. '.'
    :return: 
    """

    filenames = os.listdir(in_dir)

    for filename in filenames:

        if filename.endswith('.jpg') or filename.endswith('.JPG')\
                or filename.endswith('.jpeg') or filename.endswith('.JPEG'):

            filename_base, filename_ext = os.path.splitext(filename)
            print(filename_base, filename_ext)

            # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
            image_file = open(filename)

            image = Image.open(image_file)
            data = list(image.getdata())

            # image_new doesn't contain exif metadata
            image_new = Image.new(image.mode, image.size)
            image_new.putdata(data)

            filename_new_base = filename_base + '_no_exif'
            filename_new = Path.joinpath(filename_new_base).with_suffix(filename_ext)
            image_new.save(filename_new)


if __name__ == '__main__':

    strip_exif('.')
