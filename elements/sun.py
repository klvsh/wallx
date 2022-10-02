import random

import numpy as np
from numpy import asarray

from PIL import Image, ImageDraw

from shapes.circle import draw_circle


def draw_sun(img_data, sun_phase):
    if not sun_phase:
        return img_data

    sun_size = int(0.08 * min(img_data.shape[0], img_data.shape[1]))

    pos_x = random.randint(
        (2 * sun_size), (img_data.shape[1] - 3 * sun_size)
    )
    pos_y = random.randint(
        int(0.5 * sun_size), int(0.2 * (img_data.shape[0]))
    )

    img_sun = Image.new(
        "RGBA",
        (img_data.shape[1], img_data.shape[0]),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(img_sun)

    # draw the glow of the sun
    rings = 100
    for i in range(rings):
        draw_circle(
            pos_x + sun_size / 2, pos_y + sun_size / 2,
            (sun_size * 10) * ((rings - i) / rings),
            (255, 255, 255, int(125 * (i / rings))),
            draw
        )

    # draw the sun
    draw.chord((pos_x + 0, pos_y + 0, pos_x + sun_size, pos_y + sun_size),
               sun_phase[0], sun_phase[1], fill=(249, 215, 28))

    # add it to the base image
    sun = np.array(img_sun.getdata())
    sun = sun.reshape(img_data.shape)

    img = Image.fromarray(np.uint8(img_data), mode="RGBA")
    img = Image.alpha_composite(img, img_sun)
    return asarray(img)
