import random


class Backdrop:
    def __init__(self, start_rgba, stop_rgba):
        self.start_rgba = start_rgba
        self.stop_rgba = stop_rgba


POSSIBLE_PHASES_DAY = "day"
POSSIBLE_PHASES_NIGHT = "night"

POSSIBLE_PHASES = [
    # POSSIBLE_PHASES_DAY,
    POSSIBLE_PHASES_NIGHT
]

POSSIBLE_STARS_NO_STARS = "no"
POSSIBLE_STARS_DENSE = "dense"
POSSIBLE_STARS_SPARSE = "sparse"

POSSIBLE_STARS = [
    POSSIBLE_STARS_NO_STARS,
    POSSIBLE_STARS_DENSE,
    POSSIBLE_STARS_SPARSE,
]

POSSIBLE_BACKDROP_DAY_1 = Backdrop((56, 182, 255, 255), (255, 255, 255, 255))
POSSIBLE_BACKDROP_DAY = [
    POSSIBLE_BACKDROP_DAY_1,
]

POSSIBLE_BACKDROP_NIGHT_1 = Backdrop((0, 0, 0, 255), (0, 0, 0, 255))
POSSIBLE_BACKDROP_NIGHT_2 = Backdrop((1, 6, 15, 255), (18, 56, 90, 255))
POSSIBLE_BACKDROP_NIGHT = [
    POSSIBLE_BACKDROP_NIGHT_1,
    POSSIBLE_BACKDROP_NIGHT_2,
]


POSSIBLE_TERRAINS_DAY_1 = Backdrop((165, 92, 27, 255), (0, 0, 0, 255))
POSSIBLE_TERRAINS_DAY = [
    POSSIBLE_TERRAINS_DAY_1,
]

POSSIBLE_TERRAINS_NIGHT_1 = Backdrop((165, 92, 27, 255), (0, 0, 0, 255))
POSSIBLE_TERRAINS_NIGHT = [
    POSSIBLE_TERRAINS_NIGHT_1,
]

POSSIBLE_MOON_PHASES_FULL = (0, 360)
POSSIBLE_MOON_PHASES_HALFTILT_LEFT = (45, 45 + 180)
POSSIBLE_MOON_PHASES_HALFTILT_RIGHT = (45 + 270, 45 + 180 + 270)
POSSIBLE_MOON_PHASES = [
    POSSIBLE_MOON_PHASES_FULL,
    POSSIBLE_MOON_PHASES_HALFTILT_LEFT,
    POSSIBLE_MOON_PHASES_HALFTILT_RIGHT,
]

POSSIBLE_SUN_PHASES_1 = (0, 360)
POSSIBLE_SUN_PHASES = [
    POSSIBLE_SUN_PHASES_1
]


class ImageConfiguration:
    def __init__(self, phase="day", stars=False, backdrop=None,
                 terrain_shade=None, moon_phase=None, sun_phase=None):
        self.phase = phase
        self.stars = stars
        self.backdrop = backdrop
        self.terrain_shade = terrain_shade
        self.moon_phase = moon_phase
        self.sun_phase = sun_phase


class ConfigurationGenerator:
    def __init__(self):
        pass

    def generate(self, seed=None):
        if seed:
            print("seed", seed)
            random.seed(seed)
        phase = random.choice(POSSIBLE_PHASES)

        stars = random.choice(POSSIBLE_STARS) \
            if phase == POSSIBLE_PHASES_NIGHT \
            else POSSIBLE_STARS_NO_STARS

        moon_phase, sun_phase = None, None

        if phase == POSSIBLE_PHASES_NIGHT:
            backdrop = random.choice(POSSIBLE_BACKDROP_NIGHT)
            terrain_shade = random.choice(POSSIBLE_TERRAINS_NIGHT)
            moon_phase = random.choice(POSSIBLE_MOON_PHASES)
        elif phase == POSSIBLE_PHASES_DAY:
            backdrop = random.choice(POSSIBLE_BACKDROP_DAY)
            terrain_shade = random.choice(POSSIBLE_TERRAINS_DAY)
            sun_phase = random.choice(POSSIBLE_SUN_PHASES)
        else:
            backdrop = random.choice(POSSIBLE_BACKDROP_NIGHT)
            terrain_shade = random.choice(POSSIBLE_TERRAINS_NIGHT)
            moon_phase = random.choice(POSSIBLE_MOON_PHASES)

        params = {
            "phase": phase,
            "stars": stars,
            "backdrop": backdrop,
            "terrain_shade": terrain_shade,
            "moon_phase": moon_phase,
            "sun_phase": sun_phase,
        }

        return ImageConfiguration(**params)
