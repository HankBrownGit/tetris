import pygame

class Gfx(object):

    def __init__(self, **kwargs):

        self._surface = kwargs.get('surface')
        self._size = kwargs.get('size')
        self._brickSize = kwargs.get('brickSize', 20)
        self._timer = kwargs.get('timer')

    def draw(self):
        #self._surface.fill((255,255,255))
        self._surface.fill((255,255,255))
        for i in range(self._size[0]+1):
            #self._surface.fill((255,255,255))
            pygame.draw.line(self._surface, (0, 0, 0), (i * self._brickSize, 0) , (i * self._brickSize, self._size[1] * self._brickSize), 1)
        for i in range(self._size[1]+1):
            pygame.draw.line(self._surface, (0, 0, 0), (0, i * self._brickSize), (self._size[0] * self._brickSize, i * self._brickSize), 1)
        pygame.display.update()