import pygame
import functools

import config
from src import Window
from src.widget import Button
from src.widget import InputBox
from src.widget import PlayBox
from src.widget import Surface
from src.widget import Text
from src import Player
from src import Board
from src import Game

def test():
    pygame.init()
    window = Window.game

    board = Board.Board(9, "assets/Board.png")

    p1 = Player.Player(1, "Henri", board.length // 2, 0, config.defaultbWall, "assets/Player1.png")
    p2 = Player.Player(2, "Nino", board.length // 2, board.length - 1, config.defaultbWall, "assets/Player2.png")

    game = Game.Game(board, p1, p2)
    window.components[0].addComponents(game)
    window.display()

    pygame.quit()

if __name__ == "__main__":
    test()