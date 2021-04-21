import math
import random


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
    return [0] + [random.random() for i in range(width - 2)] + [0]


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


def generate_terrain(width, height):
    iterations = random.randint(8, 9)
    terrain = generate_smooth_terrain(width, iterations=iterations)
    elevation = int((0.3 + (random.random() * 0.2)) * height)
    terrain_height = int((0.1 + (random.random() * 0.2)) * height)
    return [
        height - (elevation + mapv(h, 0, 1, 0, terrain_height))
        for h in terrain
    ]


def draw_terrain(img_data):
    (height, width, _) = img_data.shape
    terrain_heights = generate_terrain(width, height)

    # Draw terrain
    for index, height in enumerate(terrain_heights):
        height = int(height)
        line_width = 8
        for h in range(-line_width // 2, line_width // 2):
            img_data[height + h, index] = [125, 125, 125, 255 - (abs(h) * 60)]

    return img_data
