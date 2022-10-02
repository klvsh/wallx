import numpy as np


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
