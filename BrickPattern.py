class BrickPattern(object):
    def __init__(self, brickType, anchor):
        self._pattern = []
        self._rotatable = True
        self._activePattern = 0
        self._anchor = anchor
        self._brickType = brickType

        if self._brickType == 0:
            self._patterns = [[[-1, 0], [0, 0], [1, 0], [0, 1]],
                              [[-1, 0], [0, 0], [0, -1], [0, 1]],
                              [[0, -1], [-1, 0], [0, 0], [1, 0]],
                              [[0, -1], [0, 0], [1, 0], [0, 1]]]

    def getPattern(self):
        return self._patterns[self._activePattern]

    def getAnchor(self):
        return self._anchor

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
        retList = []
        for i in self._patterns:
            for j in i:
                retList.append(j[0])
        return self._anchor[0] + max(retList)

    def getMinY(self):
        retList = []
        for i in self._patterns:
            for j in i:
                retList.append(j[1])
        return self._anchor[1] + min(retList)

    def getMaxY(self):
        retList = []
        for i in self._patterns:
            for j in i:
                retList.append(j[1])
        return self._anchor[1] + max(retList)
