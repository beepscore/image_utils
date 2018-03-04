import subprocess
import os


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

            # tested with one file in project root directory
            # exiftool removed exif metadata from original file and
            # made a copy by appending "_original"
            # apparently exiftool did not recompress files.
            # https://docs.python.org/3/library/subprocess.html#module-subprocess
            subprocess.run(["exiftool", "-all=", filename])


if __name__ == '__main__':

    strip_exif('.')
