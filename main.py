#
# References:
#   - https://note.nkmk.me/en/python-numpy-generate-gradation-image/
#

import numpy as np
from PIL import Image

from terrain import generate_terrain

img_width = 1280
img_height = 720


def generate_2d_gradient(start, stop, width, height):
    # create linspace from start to stop with "width" evenly spaced points
    # row of pixels, gradient changes from start to stop having
    # width number of elments
    row = np.linspace(start, stop, width)

    # create 2 dimensional tile equalling height of the image, with
    # the same repetition as one row of pixels
    return np.tile(row, (height, 1))


def generate_gradient(width, height, start_rgb, stop_rgb):
    # create base image data
    # height, width, 3 per pixel for RGB
    image_data = np.zeros((height, width, 4), dtype=np.float)

    for i, (start_color, stop_color) in enumerate(zip(start_rgb, stop_rgb)):
        image_data[:, :, i] = generate_2d_gradient(
            start_color, stop_color, width, height)

    return image_data


def generate_image():
    terrain_heights = generate_terrain(img_width, img_height)
    img_data = generate_gradient(
        img_width, img_height, (0, 0, 0, 255), (0, 0, 0, 255))

    for index, height in enumerate(terrain_heights):
        height = int(height)
        img_data[height, index, 0] = 255
        img_data[height, index, 1] = 255
        img_data[height, index, 2] = 255
        img_data[height, index, 3] = 255

    img = Image.fromarray(np.uint8(img_data))
    img.save('wallpaper.png')


generate_image()
