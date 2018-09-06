from Game import *
if __name__ == "__main__":
    tetrisGame = Game()

    pattern = BrickPattern.BrickPattern(0)
    print(pattern.getPattern())
    pattern.rotate()
    print(pattern.getPattern())
    tetrisGame.run()
    # tetrisGame.run()
