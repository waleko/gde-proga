from Game import Game
import sys

argv = sys.argv

field_size = (10, 11)

if len(argv) > 2:
    field_size = (int(argv[1]), int(argv[2]))

myGame = Game(field_size)
myGame.play()
