import sys

import BrickPattern
from Gfx import *
from Timer import *


class Game():

    def __init__(self, **kwargs):
        self._size = kwargs.get('size', [20, 30])
        self._brick_size = kwargs.get('brickSize', 10)
        self._windowSize = [self._size[0] * self._brick_size, self._size[1] * self._brick_size + 50]
        self._cps = kwargs.get('speed', 1)
        self._screen = pygame.display.set_mode(self._windowSize)
        self._timer = Timer()
        self._petrifiedBricks = []
        self._brickPattern = BrickPattern.BrickPattern([5, 0])
        self._gfx = Gfx(surface=self._screen, brickSize=self._brick_size, size=self._size, timer=self._timer,
                        brickPattern=self._brickPattern, petrifiedBricks=self._petrifiedBricks)
        self._delay = 1 / self._cps

    def _checkLines(self):
        pass

    def _petrifyBricks(self):
        anchor = self._brickPattern.getAnchor()
        for brick in self._brickPattern.getPattern():
            self._petrifiedBricks.append([anchor[0] + brick[0], anchor[1] + brick[1]])
        self._brickPattern.respawn()

    def _checkBricks(self):

        collide = False
        anchor = self._brickPattern.getAnchor()
        anchor = [anchor[0], anchor[1] + 1]
        futureBrick = [[anchor[0] + b[0], anchor[1] + b[1]] for b in self._brickPattern.getPattern()]

        for brick in futureBrick:
            for petriBrick in self._petrifiedBricks:
                if brick == petriBrick:
                    collide = True

        if collide:
            self._petrifyBricks()
            return 0

        if self._brickPattern.getMaxY() >= self._size[1] - 1:
            self._petrifyBricks()
            return 0


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

            self._checkBricks()

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
                        print("next max: {}, nextMin {}".format(self._brickPattern.getMaxX(True),
                                                                self._brickPattern.getMinX(True)))
                        if self._brickPattern.getMaxX(True) < self._size[1] and self._brickPattern.getMinX(True) >= 0:
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