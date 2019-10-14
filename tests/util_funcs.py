import os
import sys
import tempfile
import io
import shutil
import numpy as np

from PIL import Image


def create_colour_temp_image(size, file_format):
    tmpdir = tempfile.mkdtemp()
    tmp = create_temp_file(tmpdir, '.'+file_format)

    im = Image.fromarray(np.uint8(np.random.rand(size[0], size[1], 3) * 255))
    im.save(tmp.name, file_format)

    return im, tmpdir


def create_greyscale_temp_image(size, file_format):
    tmpdir = tempfile.mkdtemp()
    tmp = create_temp_file(tmpdir, '.'+file_format)
    
    im = Image.fromarray(np.uint8(np.random.rand(size[0], size[1]) * 255))
    im.save(tmp.name, file_format)

    return im, tmpdir


def create_sub_folders(number_of_sub_folders, number_of_images):

    parent_temp_directory = tempfile.mkdtemp()

    temp_directories = []
    temp_files = []

    for x in range(number_of_sub_folders):
        sub_temp_directory = tempfile.mkdtemp(dir=parent_temp_directory)
        temp_directories.append(sub_temp_directory)
        for y in range(number_of_images):
            temp_file = create_temp_file(sub_temp_directory, '.JPEG')
            im_array = Image.fromarray(np.uint8(np.random.rand(800, 800) * 255))
            im_array.save(temp_file.name, 'JPEG')
            temp_files.append(temp_file)

    return temp_directories, temp_files, parent_temp_directory

def create_temp_file(dir, suffix):
    tmp = tempfile.NamedTemporaryFile(dir=dir, suffix=suffix, delete=False)
    tmp.close()
    return tmp

def create_temp_image_file(dir, file_format):
    tmp = create_temp_file(dir, '.'+file_format)

    im = Image.new('RGB', (800, 800))
    im.save(tmp.name, file_format)

    return tmp

def create_multiple_images(dir, num_of_images, size):
    img_file_list = []
    for _ in range(num_of_images):
        tmp = create_temp_file(dir, '.JPEG')
        img_file_list.append(tmp)
        im = Image.new('RGB', size)
        im.save(tmp.name, 'JPEG')
    return img_file_list