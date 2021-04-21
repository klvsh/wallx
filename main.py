#
# References:
#   - https://note.nkmk.me/en/python-numpy-generate-gradation-image/
#

import numpy as np

from PIL import Image

from configuration import ConfigurationGenerator
from elements.moon import draw_moon
from elements.terrain import draw_terrain
from elements.gradient import generate_gradient


img_width = 1280
img_height = 720


def generate_image():
    assert img_width >= img_height >= 360
    generator = ConfigurationGenerator()
    configuration = generator.generate(seed="arpit_bhaani")

    img_data = generate_gradient(
        img_width,
        img_height,
        configuration.backdrop.start_rgba,
        configuration.backdrop.stop_rgba,
        is_horizontal=False
    )

    # add_stars(img_data, configuration.stars)
    img_data = draw_terrain(img_data)
    img_data = draw_moon(img_data, configuration.moon_phase)

    img = Image.fromarray(np.uint8(img_data))
    img.save('wallpaper.png')


generate_image()
