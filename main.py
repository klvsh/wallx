#
# References:
#   - https://note.nkmk.me/en/python-numpy-generate-gradation-image/
#

import argparse

import random
import numpy as np

from PIL import Image

from elements.moon import draw_moon
from elements.stars import draw_stars
from elements.terrain import draw_terrain
from elements.backdrop import draw_backdrop

from configuration import Configuration, ConfigurationGenerator, POSSIBLE_THEMES


img_width = 720
img_height = int(720 * 1.4)


def generate_image(theme):
    assert img_width >= 360 <= img_height
    generator = ConfigurationGenerator()
    configuration = generator.generate(theme=theme)

    img_data = draw_backdrop(img_width, img_height, configuration)

    img_data = draw_stars(img_data)

    total_terrains = random.randint(1, configuration.theme.max_terrains)
    terrains = random.sample(
        configuration.theme.possible_terrains,
        total_terrains)

    max_terrain_height = int((0.4 + random.random() * 0.2) * img_height)
    elevation = int(random.random() * 0.2 * img_height)
    shift = 0
    for terrain in terrains:
        img_data = draw_terrain(
            img_data, terrain, terrain_height=max_terrain_height, elevation=elevation, shift=shift)
        max_terrain_height = int(
            (0.5 + random.random() * 0.2) * max_terrain_height)
        shift = shift * -1 if shift else random.choice([-1, 1])
        elevation = (0.1 + random.random() * 0.5) * elevation

    img_data = draw_moon(img_data, configuration)

    img = Image.fromarray(np.uint8(img_data))
    img.save('wallpaper.png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='generate a beautiful wallpaper')
    parser.add_argument('--width', type=int, default=720)
    parser.add_argument('--height', type=int, default=720)
    parser.add_argument('--theme', type=str, default="Emerald", choices=[theme.name for theme in POSSIBLE_THEMES])

    args = parser.parse_args()

    img_width, img_height = args.width, args.height
    generate_image(args.theme)
