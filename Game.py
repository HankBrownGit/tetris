import sys

import BrickPattern
from Gfx import *
from Matrix import *
from Timer import *


class Game():

    def __init__(self, **kwargs):
        self._size = kwargs.get('size', [20, 30])
        self._brick_size = kwargs.get('brickSize', 20)
        self._windowSize = [self._size[0] * self._brick_size, self._size[1] * self._brick_size + 50]
        self._cps = kwargs.get('speed', 1)
        self._screen = pygame.display.set_mode(self._windowSize)
        self._timer = Timer()
        self._matrix = Matrix(self._size)
        self._brickPattern = BrickPattern.BrickPattern(0, [5, 0])
        self._gfx = Gfx(surface=self._screen, brickSize=self._brick_size, size=self._size, timer=self._timer,
                        brickPattern=self._brickPattern)
        self._delay = 1 / self._cps

    def run(self):
        """"
        Game main loop
        """
        self._timer.start()

        exitGame = False

        while not exitGame:

            if self._timer.getTotalTime() >= self._delay:
                self._brickPattern.moveDown()
                self._timer.reset()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT]:
                print("Right key pressed")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type is pygame.KEYDOWN:
                    key = pygame.key.name(event.key)

                    if key == "escape":
                        exitGame = True

                    if key == "up":
                        self._brickPattern.rotate()

                    if key == "right":
                        if self._brickPattern.getMaxX() < self._size[1]:
                            self._brickPattern.moveRight()

                    if key == "down":
                        self._brickPattern.moveDown()

                    if key == "left":
                        if self._brickPattern.getMinY() > 0:
                            self._brickPattern.moveLeft()


            self._gfx.draw()