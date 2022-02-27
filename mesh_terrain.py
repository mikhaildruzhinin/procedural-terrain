from ursina import (
    Entity,
    load_model,
    Mesh,
    Vec2,
    Vec3,
)


class MeshTerrain:
    def __init__(self):
        self.block = load_model('block.obj')
        self.texture_atlas = 'texture_atlas.png'

        self.subsets = []
        self.num_subsets = 1
        self.subset_width = 128

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
            [Vec3(x, 0, z) + vertex for vertex in self.block.vertices]
        )

        # texture atlas coordinates for grass
        uu = 8
        uv = 7

        model.uvs.extend(
            [Vec2(uu, uv) + u for u in self.block.uvs]
        )

    def generate_terrain(self):
        x = 0
        z = 0
        distance = int(self.subset_width / 2)

        for i in range(-distance, distance):
            for j in range(-distance, distance):
                self.generate_block(x + i, 0, z + j)
        
        self.subsets[0].model.generate()
