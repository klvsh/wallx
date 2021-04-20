#
# References:
#   - https://note.nkmk.me/en/python-numpy-generate-gradation-image/
#

import numpy as np
from PIL import Image

from terrain import generate_terrain
from configuration import ConfigurationGenerator

img_width = 1280
img_height = 720


def generate_2d_gradient(start, stop, width, height, is_horizontal=False):
    # create linspace from start to stop with "width" evenly spaced points
    # row of pixels, gradient changes from start to stop having
    # width number of elments
    # create 2 dimensional tile equalling height of the image, with
    # the same repetition as one row of pixels
    if is_horizontal:
        row = np.linspace(start, stop, width)
        return np.tile(row, (height, 1))

    row = np.linspace(start, stop, height)
    return np.tile(row, (width, 1)).T


def generate_gradient(width, height, start_rgba,
                      stop_rgba, is_horizontal=True):
    # create base image data
    # height, width, 3 per pixel for RGB
    image_data = np.zeros((height, width, 4), dtype=float)

    for i, (start_color, stop_color) in enumerate(zip(start_rgba, stop_rgba)):
        image_data[:, :, i] = generate_2d_gradient(
            start_color, stop_color, width, height, is_horizontal=is_horizontal)

    return image_data


def add_terrain(img_data):
    (height, width, _) = img_data.shape
    terrain_heights = generate_terrain(width, height)

    # Draw terrain
    for index, height in enumerate(terrain_heights):
        height = int(height)
        line_width = 6
        for h in range(-line_width // 2, line_width // 2):
            img_data[height + h, index, 0] = 255
            img_data[height + h, index, 1] = 255
            img_data[height + h, index, 2] = 255
            img_data[height + h, index, 3] = 255 - (abs(h) * 50)


def generate_image():
    generator = ConfigurationGenerator()
    configuration = generator.generate(seed="arpit_bhayani")

    img_data = generate_gradient(
        img_width,
        img_height,
        configuration.backdrop.start_rgba,
        configuration.backdrop.stop_rgba,
        is_horizontal=False
    )

    # add_stars(img_data, configuration.stars)
    add_terrain(img_data)

    img = Image.fromarray(np.uint8(img_data))
    img.save('wallpaper.png')


generate_image()
