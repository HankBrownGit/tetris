class BrickPattern(object):
    def __init__(self, type, anchor):
        self._pattern = []
        self._rotatable = True
        self._activePattern = 0
        self._anchor = anchor

        if type == 0:
            self._patterns = [[[-1, 0], [0, 0], [1, 0], [0, 1]],
                              [[-1, 0], [0, 0], [0, -1], [0, 1]],
                              [[0, -1], [-1, 0], [0, 0], [1, 0]],
                              [[0, -1], [0, 0], [1, 0], [0, 1]]]

    def getPattern(self):
        return self._patterns[self._activePattern]

    def rotate(self):
        if self._activePattern == 3:
            self._activePattern = 0
        else:
            self._activePattern += 1

    def moveDown(self):
        self._anchor[1] += 1

    def moveRight(self):
        self._anchor[0] += 1

    def moveLeft(self):
        self._anchor[0] -= 1

    def getMaxX(self):
        pass

    def getMinY(self):
        pass

    def getMaxY(self):
        pass
