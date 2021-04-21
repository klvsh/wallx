import random

import numpy as np
from numpy import asarray

from PIL import Image, ImageDraw

from elements.shapes import draw_circle


def draw_moon(img_data, moon_phase):
    if not moon_phase:
        return img_data

    moon_size = int(0.08 * min(img_data.shape[0], img_data.shape[1]))

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
    for i in range(rings):
        draw_circle(
            pos_x + moon_size / 2, pos_y + moon_size / 2,
            (moon_size * 10) * ((rings - i) / rings),
            (255, 255, 255, int(40 * (i / rings))),
            draw
        )

    # draw the moon
    draw.chord((pos_x + 0, pos_y + 0, pos_x + moon_size, pos_y + moon_size),
               moon_phase[0], moon_phase[1], fill=(255, 255, 255, 255))

    # add it to the base image
    moon = np.array(img_moon.getdata())
    moon = moon.reshape(img_data.shape)

    img = Image.fromarray(np.uint8(img_data), mode="RGBA")
    img = Image.alpha_composite(img, img_moon)
    return asarray(img)
