from ursina import Vec2


class SwirlEngine:
    def __init__(
        self,
        chunk_width: int,
    ):
        self.chunk_width = chunk_width

        # tracking position of generated chunk
        self.position = Vec2(0, 0)

        self.reset(self.position)

        self.directions = [
            Vec2(0, 1),
            Vec2(1, 0),
            Vec2(0, -1),
            Vec2(-1, 0),
        ]

    def change_direction(self):
        if self.current_direction < 3:
            self.current_direction += 1
        else:
            self.current_direction = 0
            self.iteration += 1

        if self.current_direction < 2:
            self.run = self.iteration * 2 - 1
        else:
            self.run = self.iteration * 2

    def move(self):
        if self.count < self.run:
            self.position.x += self.directions[self.current_direction].x * self.chunk_width
            self.position.y += self.directions[self.current_direction].y * self.chunk_width
            self.count += 1
        else:
            self.count = 0
            self.change_direction()
            self.move()

    def reset(
        self,
        position: Vec2,
    ):
        self.position = position
        self.run = 1
        self.iteration = 1
        self.count = 0
        self.current_direction = 0
