from Game import *
if __name__ == "__main__":
    tetrisGame = Game()

    pattern = BrickPattern.BrickPattern(0, [0, 0])
    pattern.rotate()
    print(pattern.getMaxX(), pattern.getMaxY(), pattern.getMinY())
    tetrisGame.run()
    # tetrisGame.run()
