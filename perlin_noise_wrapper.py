from perlin_noise import PerlinNoise


class PerlinNoiseWrapper:
    def __init__(self):
        self.seed = 123
        self.octaves = 4
        self.frequency = 256
        self.amplitude = 24

        self.perlin_noise = PerlinNoise(
            octaves=self.octaves,
            seed=self.seed,
        )

    def get_height(
        self,
        x: int,
        z: int,
    ) -> int:
        return self.perlin_noise(
            [x / self.frequency, z / self.frequency]
        ) * self.amplitude
