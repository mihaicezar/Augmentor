# Context
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Imports
import Augmentor
import tempfile
import io
import shutil
from PIL import Image
from Augmentor import Operations

from util_funcs import create_colour_temp_image, create_greyscale_temp_image


def test_in_memory_distortions():
    im, tmpdir = create_colour_temp_image((800, 800), "JPEG")

    r_d = Operations.Distort(probability=1, grid_width=8, grid_height=8, magnitude=8)
    tmp_im = r_d.perform_operation([im])

    assert tmp_im is not None
    assert tmp_im[0].size == (800,800)

    im_bw, tmpdir_bw = create_greyscale_temp_image((800, 800), "PNG")

    r_d_bw = Operations.Distort(probability=1, grid_width=8, grid_height=8, magnitude=8)
    tmp_im_bw = r_d_bw.perform_operation([im_bw])

    assert tmp_im_bw is not None
    assert tmp_im_bw[0].size == (800,800)
    assert isinstance(tmp_im_bw[0], Image.Image)

    shutil.rmtree(tmpdir)
    shutil.rmtree(tmpdir_bw)
