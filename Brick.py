class Brick(object):
    def __init__(self, type: int, isAnchor: bool = False):
        self._type = type
        self._isAnchor = isAnchor
