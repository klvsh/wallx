import random

import numpy as np
from numpy import asarray

from PIL import Image, ImageDraw

from shapes.circle import draw_circle


def draw_moon(img_data, configuration):
    moon_size = int((0.05 + (random.random() * 0.05)) *
                    min(img_data.shape[0], img_data.shape[1]))

    pos_x = random.randint(
        (2 * moon_size), (img_data.shape[1] - 3 * moon_size)
    )
    pos_y = random.randint(
        int(0.5 * moon_size), int(0.2 * (img_data.shape[0]))
    )

    img_moon = Image.new(
        "RGBA",
        (img_data.shape[1], img_data.shape[0]),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(img_moon)

    # draw the glow of the moon
    rings = 100
    max_intensity = random.randint(35, 55)
    for i in range(rings):
        draw_circle(
            pos_x + moon_size / 2, pos_y + moon_size / 2,
            (moon_size * 10) * ((rings - i) / rings),
            (255, 255, 255, int(max_intensity * (i / rings))),
            draw
        )

    # draw the moon
    config_moon = random.choice(configuration.theme.possible_moon_arcs)
    draw.chord((pos_x + 0, pos_y + 0, pos_x + moon_size, pos_y + moon_size),
               *config_moon.chord, fill=(255, 255, 255, 255))

    # add it to the base image
    moon = np.array(img_moon.getdata())
    moon = moon.reshape(img_data.shape)

    img = Image.fromarray(np.uint8(img_data), mode="RGBA")
    img = Image.alpha_composite(img, img_moon)
    return asarray(img)
