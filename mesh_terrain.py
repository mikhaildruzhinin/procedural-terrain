import math
import random

from ursina import (
    Entity,
    load_model,
    Mesh,
    Vec2,
    Vec3,
    Vec4,
)

from config import (
    BLOCK_MODEL,
    CHUNK_WIDTH,
    NUMBER_CHUNKS,
    TEXTURE_ATLAS,
    TEXTURE_ATLAS_COORDINATES,
    TEXTURE_SCALE,
    TINT_OFFSET,
    SNOW_HEIGHT,
)
from perlin_noise_wrapper import PerlinNoiseWrapper
from swirl_engine import SwirlEngine


class MeshTerrain:
    def __init__(self):
        self.block = load_model(BLOCK_MODEL)
        self.texture_atlas = TEXTURE_ATLAS
        self.number_vertices = len(self.block.vertices)

        self.chunks = []
        self.number_chunks = NUMBER_CHUNKS
        self.swirl_engine = SwirlEngine(CHUNK_WIDTH)
        self.current_chunk = 0

        self.terrain_coordinates = {}

        self.perlin_noise = PerlinNoiseWrapper()

        for _ in range(0, self.number_chunks):
            entity = Entity(
                model=Mesh(),
                texture=self.texture_atlas
            )
            entity.texture_scale *= TEXTURE_SCALE / entity.texture.width

            self.chunks.append(entity)

    def generate_block(
        self,
        x: int,
        y: int,
        z: int,
    ):
        model = self.chunks[self.current_chunk].model
        model.vertices.extend(
            [Vec3(x, y, z) + vertex for vertex in self.block.vertices]
        )

        block_coordinates = f'x{math.floor(x)}y{math.floor(y)}z{math.floor(z)}'
        self.terrain_coordinates[block_coordinates] = 't'

        random_tint = random.random() - TINT_OFFSET
        model.colors.extend(
            (
                Vec4(1 - random_tint, 1 - random_tint, 1 - random_tint, 1),
            ) * self.number_vertices
        )

        # texture atlas coordinates for grass
        uu, uv = TEXTURE_ATLAS_COORDINATES['grass']

        if y > SNOW_HEIGHT:
            uu, uv = TEXTURE_ATLAS_COORDINATES['snow']

        model.uvs.extend(
            [Vec2(uu, uv) + u for u in self.block.uvs]
        )

    def generate_terrain(self):
        x = math.floor(self.swirl_engine.position.x)
        z = math.floor(self.swirl_engine.position.y)

        distance = int(CHUNK_WIDTH / 2)

        for i in range(-distance, distance):
            for j in range(-distance, distance):
                y = math.floor(self.perlin_noise.get_height(x + i, z + j))
                block_coordinates = f'x{math.floor(x + i)}y{math.floor(y)}z{math.floor(z + j)}'
                if self.terrain_coordinates.get(block_coordinates) != 't':
                    self.generate_block(x + i, y, z + j)

        self.chunks[self.current_chunk].model.generate()

        if self.current_chunk < self.number_chunks - 1:
            self.current_chunk += 1
        else:
            self.current_chunk = 0

        self.swirl_engine.move()
