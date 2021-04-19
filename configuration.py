import random


POSSIBLE_PHASES = ["day", "night"]


class ImageConfiguration:
    def __init__(self, phase="day"):
        self.phase = phase


class ConfigurationGenerator:
    def __init__(self):
        pass

    def generate(self, seed):
        print("seed", random.seed(seed))
        phase = random.choice(POSSIBLE_PHASES)
        params = {
            "phase": phase
        }
        return ImageConfiguration(**params)
