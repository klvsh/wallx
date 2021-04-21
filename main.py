#
# References:
#   - https://note.nkmk.me/en/python-numpy-generate-gradation-image/
#

import random
import numpy as np
from numpy import asarray

from PIL import Image, ImageDraw

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
        line_width = 8
        for h in range(-line_width // 2, line_width // 2):
            img_data[height + h, index] = [125, 125, 125, 255 - (abs(h) * 60)]

    return img_data


def add_moon(img_data, moon_phase):
    if not moon_phase:
        return img_data

    moon_size = int(0.05 * min(*img_data.shape))

    pos_x = random.randint(
        (2 * moon_size), (img_data.shape[1] - 3 * moon_size)
    )
    pos_y = random.randint(
        int(0.5 * moon_size), int(0.2 * (img_data.shape[0]))
    )

    img_moon = Image.new(
        "RGBA", (img_data.shape[1], img_data.shape[0]), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img_moon)
    draw.chord((pos_x + 0, pos_y + 0, pos_x + 45, pos_y + 45),
               moon_phase[0], moon_phase[1], fill="white")
    moon = np.array(img_moon.getdata())
    moon = moon.reshape(img_data.shape)

    img = Image.fromarray(np.uint8(img_data), mode="RGBA")
    img = Image.alpha_composite(img, img_moon)
    return asarray(img)


def generate_image():
    generator = ConfigurationGenerator()
    configuration = generator.generate()

    img_data = generate_gradient(
        img_width,
        img_height,
        configuration.backdrop.start_rgba,
        configuration.backdrop.stop_rgba,
        is_horizontal=False
    )

    # add_stars(img_data, configuration.stars)
    img_data = add_terrain(img_data)
    img_data = add_moon(img_data, configuration.moon_phase)

    img = Image.fromarray(np.uint8(img_data))
    img.save('wallpaper.png')


generate_image()
