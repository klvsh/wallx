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
    def __init__(self, gradient=None, min_iterations=8, max_iterations=10):
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
            min_iterations=9,
            max_iterations=10,
        ),
        Terrain(
            gradient=Gradient((28, 28, 28, 255), (28, 28, 28, 255)),
            min_iterations=9,
            max_iterations=10,
        ),
        Terrain(
            gradient=Gradient((21, 21, 21, 255), (21, 21, 21, 255)),
            min_iterations=9,
            max_iterations=10,
        ),
        Terrain(
            gradient=Gradient((14, 14, 14, 255), (14, 14, 14, 255)),
            min_iterations=9,
            max_iterations=10,
        ),
    ],
    max_terrains=3,
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
        Gradient((4, 8, 22, 255), (47, 108, 153, 255)),
        Gradient((5, 42, 58, 255), (65, 112, 138, 255)),
        Gradient((8, 26, 25, 255), (18, 56, 90, 255)),
    ],
    possible_terrains=[
        Terrain(
            gradient=Gradient((1, 1, 1, 255), (0, 0, 0, 255)),
            min_iterations=9,
            max_iterations=10,
        ),
        Terrain(
            gradient=Gradient((12, 12, 12, 255), (10, 10, 10, 255)),
            min_iterations=9,
            max_iterations=10,
        ),
        Terrain(
            gradient=Gradient((8, 23, 39, 255), (8, 23, 39, 255)),
            min_iterations=9,
            max_iterations=10,
        ),
        Terrain(
            gradient=Gradient((6, 12, 31, 255), (6, 12, 31, 255)),
            min_iterations=9,
            max_iterations=10,
        ),
    ],
    max_terrains=3,
    possible_stars_density=[
        StarsDensity(0.05, 0.30),
    ],
    possible_moon_arcs=[
        Moon.from_chord(0, 360),
        Moon.from_chord(45, 45 + 180),
        Moon.from_chord(45 + 270, 45 + 180 + 270),
    ],
)

THEME_GLEAMY_GREEN = Theme(
    "Gleamy Green",
    possible_backdrops=[
        Gradient((2, 27, 31, 255), (63, 82, 86, 255)),
        Gradient((2, 27, 31, 255), (7, 45, 46, 255)),
    ],
    possible_terrains=[
        Terrain(
            gradient=Gradient((1, 30, 30, 255), (1, 30, 30, 255)),
            min_iterations=9,
            max_iterations=10,
        ),
        Terrain(
            gradient=Gradient((0, 14, 14, 255), (0, 14, 14, 255)),
            min_iterations=9,
            max_iterations=10,
        ),
        Terrain(
            gradient=Gradient((0, 21, 21, 255), (0, 21, 21, 255)),
            min_iterations=9,
            max_iterations=10,
        ),
        Terrain(
            gradient=Gradient((1, 12, 14, 255), (1, 12, 14, 255)),
            min_iterations=9,
            max_iterations=10,
        ),
    ],
    max_terrains=3,
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
        Gradient((15, 44, 51, 255), (61, 142, 133, 255)),
        Gradient((30, 46, 49, 255), (156, 201, 176, 255)),
        Gradient((5, 79, 80, 255), (1, 122, 121, 255)),
    ],
    max_terrains=3,
    possible_terrains=[
        Terrain(
            gradient=Gradient((5, 5, 5, 255), (5, 5, 5, 255)),
            min_iterations=9,
            max_iterations=10,
        ),
        Terrain(
            gradient=Gradient((4, 9, 6, 255), (4, 9, 6, 255)),
            min_iterations=9,
            max_iterations=10,
        ),
        Terrain(
            gradient=Gradient((16, 10, 10, 255), (16, 10, 10, 255)),
            min_iterations=9,
            max_iterations=10,
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
    THEME_GLEAMY_GREEN,
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
