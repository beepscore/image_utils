import os
# from PIL import Image


def strip_exif(in_dir):
    """
    :param in_dir: e.g. '.'
    :return: 
    """

    filenames = os.listdir(in_dir)

    for filename in filenames:
        print(filename)


if __name__ == '__main__':

    strip_exif('.')
