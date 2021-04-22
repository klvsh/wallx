#
# References:
#   - https://note.nkmk.me/en/python-numpy-generate-gradation-image/
#

import random
import numpy as np

from PIL import Image

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
    configuration = generator.generate(theme="Pitch Black")

    img_data = draw_backdrop(img_width, img_height, configuration)

    img_data = draw_stars(img_data)

    terrain = random.choice(configuration.theme.possible_terrains)
    img_data = draw_terrain(img_data, terrain)

    img_data = draw_moon(img_data)

    img = Image.fromarray(np.uint8(img_data))
    img.save('wallpaper.png')


generate_image()
