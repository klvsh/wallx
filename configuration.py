import random


class Gradient:
    def __init__(self, start_rgba, stop_rgba):
        self.start_rgba = start_rgba
        self.stop_rgba = stop_rgba


class StarsDensity:
    def __init__(self, min_percent, max_percent):
        self.min_percent = min_percent
        self.max_percent = max_percent


class Moon:
    def __init__(self):
        self.chord = None

    def set_chord(self, start_angle, end_angle):
        self.chord = (start_angle, end_angle)

    @classmethod
    def from_chord(cls, *args):
        obj = Moon()
        obj.set_chord(*args)
        return obj


class Terrain:
    def __init__(self, gradient=None, min_iterations=8, max_iterations=9):
        self.gradient = gradient
        self.min_iterations = min_iterations
        self.max_iterations = max_iterations


class Theme:
    def __init__(self, name, possible_backdrops=None, possible_terrains=None,
                 possible_stars_density=None, possible_moon_arcs=None, max_terrains=1):
        self.name = name
        self.possible_backdrops = possible_backdrops
        self.possible_terrains = possible_terrains
        self.possible_stars_density = possible_stars_density
        self.possible_moon_arcs = possible_moon_arcs
        self.max_terrains = max_terrains

    def __eq__(self, o):
        return self.name == o.name


THEME_PITCH_BLACK = Theme(
    "Pitch Black",
    possible_backdrops=[
        Gradient((0, 0, 0, 255), (0, 0, 0, 255)),
    ],
    possible_terrains=[
        Terrain(
            gradient=Gradient((35, 35, 35, 255), (35, 35, 35, 255)),
        ),
        Terrain(
            gradient=Gradient((28, 28, 28, 255), (28, 28, 28, 255)),
        ),
        Terrain(
            gradient=Gradient((21, 21, 21, 255), (21, 21, 21, 255)),
        ),
        Terrain(
            gradient=Gradient((14, 14, 14, 255), (14, 14, 14, 255)),
        ),
    ],
    max_terrains=2,
    possible_stars_density=[
        StarsDensity(0.10, 0.35),
    ],
    possible_moon_arcs=[
        Moon.from_chord(0, 360),
        Moon.from_chord(45, 45 + 180),
        Moon.from_chord(45 + 270, 45 + 180 + 270),
    ],
)

THEME_MIGHTY_BLUE = Theme(
    "Mighty Blue",
    possible_backdrops=[
        Gradient((1, 6, 15, 255), (18, 56, 90, 255)),
    ],
    possible_terrains=[
        Terrain(
            gradient=Gradient((165, 92, 27, 255), (0, 0, 0, 255)),
        ),
    ],
    max_terrains=2,
    possible_stars_density=[
        StarsDensity(0.05, 0.30),
    ],
    possible_moon_arcs=[
        Moon.from_chord(0, 360),
        Moon.from_chord(45, 45 + 180),
        Moon.from_chord(45 + 270, 45 + 180 + 270),
    ],
)

THEME_EMERALD = Theme(
    "Emerald",
    possible_backdrops=[
        Gradient((5, 34, 42, 255), (22, 98, 122, 255)),
        Gradient((5, 34, 42, 255), (11, 54, 70, 255)),
        Gradient((5, 21, 28, 255), (22, 98, 122, 255)),
    ],
    max_terrains=2,
    possible_terrains=[
        Terrain(
            gradient=Gradient((20, 20, 20, 255), (0, 0, 0, 255)),
        ),
        Terrain(
            gradient=Gradient((20, 20, 20, 255), (5, 5, 5, 255)),
        ),
        Terrain(
            gradient=Gradient((10, 10, 10, 255), (5, 5, 5, 255)),
        ),
        Terrain(
            gradient=Gradient((10, 10, 10, 255), (0, 0, 0, 255)),
        ),
    ],
    possible_stars_density=[
        StarsDensity(0.10, 0.35),
    ],
    possible_moon_arcs=[
        Moon.from_chord(0, 360),
        Moon.from_chord(45, 45 + 180),
        Moon.from_chord(45 + 270, 45 + 180 + 270),
    ],
)

POSSIBLE_THEMES = [
    THEME_EMERALD,
    THEME_PITCH_BLACK,
    THEME_MIGHTY_BLUE,
]


def get_theme_by_name(name):
    for theme in POSSIBLE_THEMES:
        if theme.name == name:
            return theme
    return THEME_MIGHTY_BLUE


class Configuration:
    def __init__(self, theme=None):
        self.theme = theme


class ConfigurationGenerator:
    def __init__(self):
        pass

    def generate(self, theme=None, seed=None):
        if seed:
            print(f"using seed: {seed}")
            random.seed(seed)

        if not theme:
            theme = random.choice(POSSIBLE_THEMES)
        else:
            theme = get_theme_by_name(theme)

        params = {
            "theme": theme,
        }

        return Configuration(**params)
