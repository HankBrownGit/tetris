import pygame


class Gfx(object):

    def __init__(self, **kwargs):

        self._surface = kwargs.get('surface')
        self._size = kwargs.get('size')
        self._brickSize = kwargs.get('brickSize', 20)
        self._brickPattern = kwargs.get('brickPattern')
        self._petrifiedBricks = kwargs.get('petrifiedBricks')

    def draw(self):
        self._surface.fill((255, 255, 255))
        for i in range(self._size[0]+1):
            pygame.draw.line(self._surface, (0, 0, 0), (i * self._brickSize, 0),
                             (i * self._brickSize, self._size[1] * self._brickSize), 1)
        for i in range(self._size[1]+1):
            pygame.draw.line(self._surface, (0, 0, 0), (0, i * self._brickSize), (self._size[0] * self._brickSize, i * self._brickSize), 1)

        anchor = self._brickPattern.getAnchor()
        pattern = self._brickPattern.getPattern()

        for brick in pattern:
            pos = (int((anchor[0] + brick[0]) * self._brickSize + self._brickSize / 2),
                   int((anchor[1] + brick[1]) * self._brickSize + self._brickSize / 2))
            pygame.draw.circle(self._surface, (0, 0, 0), pos, int(self._brickSize / 2))

        for brick in self._petrifiedBricks:
            pos = (int(brick[0] * self._brickSize + self._brickSize / 2),
                   int(brick[1] * self._brickSize + self._brickSize / 2))
            pygame.draw.circle(self._surface, (0, 0, 0), pos, int(self._brickSize / 2))

        pygame.display.update()