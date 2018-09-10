class PetrifiedBricks(object):
    def __init__(self, size=[10,30]):
        self.__matrix = [[0] * size[0]] * size[1]
        self.__size = size
        #self.__matrix = [[i] * size[0] for i in range(size[1])]

    def setCell(self, cell, value):
        if not isinstance(cell,list):
            raise TypeError('Parameter Cell has to be of type list')
        if false in [isinstance(i,int) for i in cell]:
            raise TypeError("All elements in parameter cell have to be of type integer")
        if not isinstance(value,int):
            raise TypeError("Parameter value has to be of type int")

        self.__matrix[cell] = value

    def getMatrix(self):
        return self.__matrix

    def getCell(self, cell):
        if not isinstance(cell,list):
            raise TypeError('Parameter Cell has to be of type list')
        if false in [isinstance(i,int) for i in cell]:
            raise TypeError("All elements in parameter cell have to be of type integer")

        return self.__matrix[cell]

    def removeLine(self, line):
        if line > len(self.__matrix):
            raise ValueError("Line number exceeds existing amount of lines")
        if not isinstance(line, int):
            raise ValueError("Param line has to be of type integer")

        self.__matrix.pop(line)
        self.__matrix.insert(0, [0] * self.__size[0])

    def __repr__(self):
        returnStr = ""
        for i in self.__matrix:
            returnStr += ','.join(str(e) for e in i) + "\n"
        return returnStr