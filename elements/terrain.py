import math
import random

import numpy as np
from numpy import asarray

from PIL import Image


def mapv(v, ol, oh, nl, nh):
    """maps the value `v` from old range [ol, oh] to new range [nl, nh]
    """
    return nl + (v * ((nh - nl) / (oh - ol)))


def linp(a, b, mu):
    """returns the intermediate point between `a` and `b`
    which is `mu` factor away from `a`.
    """
    return a * (1 - mu) + b * mu


def cosp(a, b, mu):
    """returns the intermediate point between `a` and `b`
    which is `mu` factor away from `a`.
    """
    mu2 = (1 - math.cos(mu * math.pi)) / 2
    return a * (1 - mu2) + b * mu2


def generate_naive_terrain(width):
    """returns the list of integers representing height at each point.
    """
    return [random.random() for i in range(width)]


def generate_smooth_terrain(width, interpolation_fn=cosp, iterations=8):
    """Using naive terrain `naive_terrain` the function generates
    Linearly Interpolated Superpositioned terrain that looks real world like.
    """
    naive_terrain = generate_naive_terrain(width)

    terrains = []

    # holds the sum of weights for normalization
    weight_sum = 0

    # for every iteration
    for z in range(iterations, 0, -1):
        terrain = []

        # compute the scaling factor (weight)
        weight = 1 / (2 ** (z - 1))

        # compute sampling frequency suggesting every `sample`th
        # point to be picked from the naive terrain.
        sample = 1 << (iterations - z)

        # get the sample points
        sample_points = naive_terrain[::sample]

        weight_sum += weight

        for i, _ in enumerate(sample_points):

            # append the current sample point (scaled) to the terrain
            terrain.append(weight * sample_points[i])

            # perform interpolation and add all interpolated values to
            # to the terrain.
            for j in range(sample - 1):
                # compute relative distance from the left point
                mu = (j + 1) / sample

                # compute interpolated point at relative distance of mu
                a = sample_points[i]
                b = sample_points[(i + 1) % len(sample_points)]
                v = interpolation_fn(a, b, mu)

                # add interpolated point (scaled) to the terrain
                terrain.append(weight * v)

        # append this terrain to list of terrains preparing
        # it to be superpositioned.
        terrains.append(terrain)

    # perform super position and normalization of terrains to
    # get the final terrain
    return [sum(x) / weight_sum for x in zip(*terrains)]


def generate_terrain(width, terrain_height, iterations=8):
    terrain = generate_smooth_terrain(width, iterations=iterations)
    return [
        mapv(h, 0, 1, 0, terrain_height)
        for h in terrain
    ]


def draw_terrain(img_data, terrain, terrain_height=360, elevation=0):
    img_width, img_height = img_data.shape[1], img_data.shape[0]
    # colors = [
    #     [5, 20, 39, 255],
    #     [11, 39, 76, 255],
    #     [26, 0, 39, 255],
    #     [1, 1, 1, 255],
    #     [7, 22, 35, 255],
    # ]
    terrain_color = np.array(terrain.gradient.start_rgba)

    img_data_terrain = np.zeros(img_data.shape, dtype=float)
    img_data_terrain = img_data_terrain.reshape(img_data.shape)

    iterations = random.randint(terrain.min_iterations, terrain.max_iterations)
    terrain_heights = generate_terrain(
        img_width, terrain_height, iterations=iterations)
    terrain_heights = [h + elevation for h in terrain_heights]

    # Draw terrain
    for index, height in enumerate(terrain_heights):
        height = int(height)
        height_plot = img_height - height
        img_data_terrain[height_plot:img_height, index] = np.tile(
            terrain_color, height).reshape((height, 4))

    img = Image.fromarray(np.uint8(img_data), mode="RGBA")
    img_terrain = Image.fromarray(np.uint8(img_data_terrain), mode="RGBA")
    img = Image.alpha_composite(img, img_terrain)
    return asarray(img)
