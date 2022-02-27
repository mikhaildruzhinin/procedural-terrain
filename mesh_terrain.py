import math

from ursina import (
    Entity,
    load_model,
    Mesh,
    Vec2,
    Vec3,
)

from perlin_noise_wrapper import PerlinNoiseWrapper


class MeshTerrain:
    def __init__(self):
        self.block = load_model('block.obj')
        self.texture_atlas = 'texture_atlas.png'

        self.subsets = []
        self.num_subsets = 1
        self.subset_width = 64

        self.terrain_coordinates = {}
        self.perlin_noise = PerlinNoiseWrapper()

        for _ in range(0, self.num_subsets):
            entity = Entity(
                model=Mesh(),
                texture=self.texture_atlas
            )
            entity.texture_scale *= 64 / entity.texture.width

            self.subsets.append(entity)

    def generate_block(self, x, y, z):
        model = self.subsets[0].model
        model.vertices.extend(
            [Vec3(x, y, z) + vertex for vertex in self.block.vertices]
        )

        model_coordinates = f'x{math.floor(x)}y{math.floor(y)}z{math.floor(z)}'
        self.terrain_coordinates[model_coordinates] = 't'

        # texture atlas coordinates for grass
        uu = 8
        uv = 7

        if y > 2:
            uu = 8
            uv = 6

        model.uvs.extend(
            [Vec2(uu, uv) + u for u in self.block.uvs]
        )

    def generate_terrain(self):
        x = 0
        z = 0
        distance = int(self.subset_width / 2)

        for i in range(-distance, distance):
            for j in range(-distance, distance):
                y = math.floor(self.perlin_noise.get_height(x + i, z + j))
                self.generate_block(x + i, y, z + j)

        self.subsets[0].model.generate()
