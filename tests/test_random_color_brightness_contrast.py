import os
import sys
sys.path.insert(0, os.path.abspath('.'))

import tempfile
import shutil
from PIL import Image
from Augmentor import Operations


from util_funcs import create_colour_temp_image, create_greyscale_temp_image


def test_random_color_in_memory():

    im, tmpdir = create_colour_temp_image((800, 800), "JPEG")

    op = Operations.RandomColor(probability=1,min_factor=0.5, max_factor =1.5)
    tmp_im = op.perform_operation([im])

    assert tmp_im is not None
    assert isinstance(tmp_im[0], Image.Image)
    shutil.rmtree(tmpdir)

    im_bw, tmpdir_bw = create_greyscale_temp_image((800, 800), "PNG")

    op = Operations.RandomColor(probability=1,min_factor=0.5, max_factor =1.5)
    tmp_im = op.perform_operation([im_bw])

    assert tmp_im is not None
    assert isinstance(tmp_im[0], Image.Image)

    shutil.rmtree(tmpdir_bw)

def test_random_contrast_in_memory():

    im, tmpdir = create_colour_temp_image((800, 800), "JPEG")

    op = Operations.RandomContrast(probability=1,min_factor=0.5, max_factor =1.5)
    tmp_im = op.perform_operation([im])

    assert tmp_im is not None
    assert isinstance(tmp_im[0], Image.Image)

    shutil.rmtree(tmpdir)

    im_bw, tmpdir_bw = create_greyscale_temp_image((800, 800), "PNG")

    op = Operations.RandomContrast(probability=1,min_factor=0.5, max_factor =1.5)
    tmp_im = op.perform_operation([im_bw])

    assert tmp_im is not None
    assert isinstance(tmp_im[0], Image.Image)
    
    shutil.rmtree(tmpdir_bw)
    
def test_random_brightness_in_memory():

    im, tmpdir = create_colour_temp_image((800, 800), "JPEG")

    op = Operations.RandomBrightness(probability=1,min_factor=0.5, max_factor =1.5)
    tmp_im = op.perform_operation([im])

    assert tmp_im is not None
    assert isinstance(tmp_im[0], Image.Image)
    shutil.rmtree(tmpdir)

    if os.name == "nt":
        # not testing bw images
        return

    im_bw, tmpdir_bw = create_greyscale_temp_image((800, 800), "PNG")

    op = Operations.RandomBrightness(probability=1,min_factor=0.5, max_factor =1.5)
    tmp_im = op.perform_operation([im_bw])

    assert tmp_im is not None
    assert isinstance(tmp_im[0], Image.Image)

    shutil.rmtree(tmpdir_bw)