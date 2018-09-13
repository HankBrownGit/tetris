import random
class BrickPattern(object):
    _brickPatternDict = {0: [[[-1, 0], [0, 0], [1, 0], [0, 1]],
                             [[-1, 0], [0, 0], [0, -1], [0, 1]],
                             [[0, -1], [-1, 0], [0, 0], [1, 0]],
                             [[0, -1], [0, 0], [1, 0], [0, 1]]],
                         1: [[[-1, 0], [0, 0], [0, 1], [1, 1]],
                             [[0, -1], [0, 0], [1, 0], [1, 1]]],
                         2: [[[0, -1], [0, 0], [0, 1], [0, 2]],
                             [[-1, 0], [0, 0], [1, 0], [2, 0]]]}

    def __init__(self, anchor):
        self._pattern = []
        self._rotatable = True
        self._activePattern = 0
        self._nextPattern = 1
        self._permaAnchor = anchor[:]
        self._anchor = anchor
        self._randMin = min(self._brickPatternDict.keys())
        self._randMax = max(self._brickPatternDict.keys())
        self.setPattern()

    def respawn(self):
        self._anchor = self._permaAnchor[:]
        self.setPattern()

    def setPattern(self):
        self._pattern = self._brickPatternDict.get(random.randrange(self._randMin, self._randMax + 1))
        # self._pattern = self._brickPatternDict.get(1)
        self._activePattern = 0

    def getPattern(self):
        return self._pattern[self._activePattern]

    def getNextPattern(self):
        return self._pattern[self._nextPattern]

    def getAnchor(self):
        return self._anchor

    def rotate(self):
        if self._activePattern == len(self._pattern) - 1:
            self._activePattern = 0
        else:
            self._activePattern += 1

        if len(self._pattern) == 1:
            self._nextPattern = 0
        elif self._activePattern == len(self._pattern) - 1:
            self._nextPattern = 0
        else:
            self._nextPattern += 1

    def moveDown(self):
        self._anchor[1] += 1

    def moveRight(self):
        self._anchor[0] += 1

    def moveLeft(self):
        self._anchor[0] -= 1

    def getMaxX(self, next=False):
        retList = []
        p = self._nextPattern if next else self._activePattern
        for i in self._pattern[p]:
            retList.append(i[1])
        return self._anchor[0] + max(retList)

    def getMinX(self, next=False):
        retList = []
        p = self._nextPattern if next else self._activePattern
        for i in self._pattern[p]:
            retList.append(i[1])
        return self._anchor[0] + min(retList)

    def getMinY(self, next=False):
        p = self._nextPattern if next else self._activePattern
        retList = []
        for i in self._pattern[p]:
            retList.append(i[1])
        return self._anchor[1] + min(retList)

    def getMaxY(self, next=False):
        p = self._nextPattern if next else self._activePattern
        retList = []
        for i in self._pattern[p]:
            retList.append(i[1])
        return self._anchor[1] + max(retList)
