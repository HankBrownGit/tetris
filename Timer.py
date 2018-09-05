import datetime

class Timer(object):
    """This class is used as a time tracker for the game. Each cykle through the main loop the time difference is
    measure. The object is then passed into different game objects that require time deltas and their calculations are
    based on the time delta received from the Timer game instance.
    """
    def __init__(self):
        self.__old_time = None
        self.__new_time = None
        self.__delta = None

    def start(self):
        self.__old_time = datetime.datetime.now()
        self.__delta = 0

    def time(self):
        new_time = datetime.datetime.now()
        self.__delta = (new_time-self.__old_time).total_seconds()
        self.__old_time = new_time

    def get_delta(self):
        return self.__delta

    def reset(self):
        self.__old_time = datetime.datetime.now()
        self.__delta = 0
