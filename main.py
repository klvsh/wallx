#
# References:
#   - https://note.nkmk.me/en/python-numpy-generate-gradation-image/
#

import numpy as np

from PIL import Image

from elements.sun import draw_sun
from elements.moon import draw_moon
from elements.stars import draw_stars
from elements.terrain import draw_terrain
from elements.backdrop import draw_backdrop

from configuration import ConfigurationGenerator


img_width = 1280
img_height = 720


def generate_image():
    assert img_width >= img_height >= 360
    generator = ConfigurationGenerator()
    configuration = generator.generate(seed="arpit_bhaani")

    img_data = draw_backdrop(img_width, img_height, configuration)

    img_data = draw_stars(img_data)
    img_data = draw_terrain(img_data)
    img_data = draw_moon(img_data, configuration.moon_phase)
    img_data = draw_sun(img_data, configuration.sun_phase)

    img = Image.fromarray(np.uint8(img_data))
    img.save('wallpaper.png')


generate_image()
