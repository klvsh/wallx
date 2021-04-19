#
# References:
#   - https://note.nkmk.me/en/python-numpy-generate-gradation-image/
#

import numpy as np
from PIL import Image

img_width = 1024
img_height = 728


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
    img_data = generate_gradient(
        img_width, img_height, (10, 10, 10, 50), (49, 42, 68, 100))
    img = Image.fromarray(np.uint8(img_data))
    img.save('gray_gradient_h.png', quality=95)


generate_image()
