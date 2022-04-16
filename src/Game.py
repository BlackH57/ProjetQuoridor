from src import Player
from src import Board
# import pygame



imageP1 = "assets/Player1.png"
imageP2 = "assets/Player2.png"
imageCase = "assets/Case.png"
imageWall = "assets/Wall.png"
imageBoard = "assets/Board.png"


class Game:

    def __init__(self, board: Board, p1: Player, p2: Player):
        self.board = board
        self.p1 = p1
        self.p2 = p2

        self.board.placePlayer(self.p1.coordX, self.p1.coordY, self.p1)
        self.board.placePlayer(self.p2.coordX, self.p2.coordY, self.p2)

        self.turn = 0


    def isWin(self, player: Player):
        """
        player : Player
        If the player is on his winning line, return True, otherwise return False
        """
        return (player.coordY == 0 and player.noPlayer == 2) or (player.coordY == self.board.length and player.noPlayer == 1)


    def movePlay(self, player: Player, coordX: int, coordY: int):
        """
        player : Player
        coordX : int
        coordY : int
        Try to move the player to coords
        """
        self.board.movePlayer(player, self.board.plateau[coordX][coordY])
        # reachableCase = self.board.reachableCase(player.coordX, player.coordY)


    def wallPlay(self, player: Player, coordX: int, coordY: int, orientation: str):
        """
        player : Player
        coordX : int
        coordY : int
        orientation : str
        Try to place a wall. Return true if succeeded, false otherwise
        """
        if player.nbWall > 0 and self.board.placeWall(coordX, coordY, orientation):
            player.useWall()
            return True
        return False


    def playerPlay(self, player: Player, choice: int):
        """
        player : Player
        choice : int
        Make the player play, if choice = 0 it moves, if choice = 1 place a wall
        Return True if succeeded to play, False otherwise
        """
        if choice == 0:
            reachable = self.board.reachableCase(player.coordX, player.coordY)
            i = 0
            # print("  reachable:\n", reachable)
            for case in reachable:
                print(i, ": ", case.getCoords())
                i += 1
            print(i, ": return")

            nextCase = int(input("Where do you want to go : "))
            while nextCase > i:
                nextCase = int(input("Where do you want to go : "))

            if nextCase == i:
                return False

            coordX, coordY = reachable[nextCase].getCoords()
            self.movePlay(player, coordX, coordY)
            return True

        else:
            coordX, coordY, orientation = input("Where do you want to place the wall : ").split()


            while not self.wallPlay(player, int(coordX), int(coordY), orientation):
                print("Invalid input")
                c = int(input("Do you want to continue : (y:0, n:1"))
                if c == 0:
                    coordX, coordY, orientation = input("Where do you want to place the wall : ").split()
                else:
                    return False

            return True


    def start(self):
        """
        Initiate two players, one board and cases, and simulate (for now) on the terminal a game of Quoridor
        """

        print("----------- Debut partie -----------")
        winner = None

        while True:
            self.turn += 1
            # print board
            print(self.board.strPlateau())
            choice = int(input(self.p1.name + ", What do you want to do:\n0: move\n1: wall\n"))
            while not self.playerPlay(self.p1, choice):
                choice = int(input(self.p1.name + ", What do you want to do:\n0: move\n1: wall\n"))
                continue
            if self.isWin(self.p1):
                winner = self.p1
                break

            print(self.board.strPlateau())
            choice = int(input(self.p2.name + ", What do you want to do:\n0: move\n1: wall\n"))
            while not self.playerPlay(self.p2, choice):
                choice = int(input(self.p1.name + ", What do you want to do:\n0: move\n1: wall\n"))
                continue
            if self.isWin(self.p2):
                winner = self.p2
                break

        print("The winner is", winner.name, "!")
        print("----------- Fin partie -----------")


        return winner
