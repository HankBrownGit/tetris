import Brick


class BrickHandler(object):
    def __init__(self):
        self._bricks = []

    def insert(self, brick: Brick):
        self._bricks.append(brick)
