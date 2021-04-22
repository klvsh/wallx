import math
import random

import numpy as np
from numpy import asarray
from PIL import Image, ImageDraw


def draw_stars(img_data):
    # TODO: Give random colors to stars.
    star_size = math.ceil(0.001 * min(img_data.shape[0], img_data.shape[1]))

    img_star = Image.new(
        "RGBA",
        (img_data.shape[1], img_data.shape[0]),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(img_star)

    # stars: at least 5% of min + random (0, 35) % of min
    total_stars = int((0.05 + random.random() * 0.35) *
                      min(img_data.shape[0], img_data.shape[1]))
    for _ in range(total_stars):
        pos_x = random.randint(
            (2 * star_size), (img_data.shape[1] - 3 * star_size)
        )
        pos_y = random.randint(0, img_data.shape[0])

        # draw the star
        draw.chord((pos_x + 0, pos_y + 0, pos_x + star_size, pos_y + star_size),
                   0, 360, fill=(255, 255, 255, 255))

    # add it to the base image
    star = np.array(img_star.getdata())
    star = star.reshape(img_data.shape)

    img = Image.fromarray(np.uint8(img_data), mode="RGBA")
    img = Image.alpha_composite(img, img_star)
    return asarray(img)
