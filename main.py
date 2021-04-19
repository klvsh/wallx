#
# References:
#   - https://note.nkmk.me/en/python-numpy-generate-gradation-image/
#

import random
import numpy as np
from PIL import Image

from terrain import generate_terrain

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


def generate_gradient(width, height, start_rgb, stop_rgb, is_horizontal=True):
    # create base image data
    # height, width, 3 per pixel for RGB
    image_data = np.zeros((height, width, 4), dtype=np.float)

    for i, (start_color, stop_color) in enumerate(zip(start_rgb, stop_rgb)):
        image_data[:, :, i] = generate_2d_gradient(
            start_color, stop_color, width, height, is_horizontal=is_horizontal)

    return image_data


def generate_image():
    # creating backdrop Day/Night
    phase = random.choice(["day", "night"])

    if phase == "day":
        start_rgb = (56, 182, 255, 255)
        stop_rgb = (255, 255, 255, 255)
    else:
        start_rgb = (0, 0, 0, 255)
        stop_rgb = (70, 70, 70, 255)

    img_data = generate_gradient(
        img_width, img_height, start_rgb, stop_rgb, is_horizontal=False)

    terrain_heights = generate_terrain(img_width, img_height)

    # Draw terrain
    for index, height in enumerate(terrain_heights):
        height = int(height)
        line_width = 6
        for h in range(-line_width // 2, line_width // 2):
            img_data[height + h, index, 0] = 255
            img_data[height + h, index, 1] = 255
            img_data[height + h, index, 2] = 255
            img_data[height + h, index, 3] = 255 - (abs(h) * 50)

    img = Image.fromarray(np.uint8(img_data))
    img.save('wallpaper.png')


generate_image()
