import pygame
from codeClass import Plateau
from codeClass import Player
from codeClass import Wall

class Game:

    def __init__(self, plateau: list[list[int]], player1 : Player, player2 : Player):
        self.plateau = plateau
        self.player1 = player1
        self.player2 = player2
        self.turn = 0
    
    def isWin(self, player : Player):
        """
        player : Player
        If the player is on his winning line, return True. Else return False
        """
        return (player.coordY == 0 and player.noPlayer == 2) or (player.coordY == self.plateau.computerLength and player.noPlayer == 1) 

    def play(self, plateau : Plateau, player : Player, noPlay : int):
        """
        noPlay must be 0 or 1
        If noPlay = 0, the player move, if noPlay = 1, the  player place a Wall
        For now use direct input with terminal
        """

        if noPlay == 0:
            cases = plateau.reachableFrom(player.coordX, player.coordY)
            
            for i in range(0, len(cases)):
                x, y = cases[i]
                print(i,": ", cases[i])
            
            nextMove = int(input("where do you want to go ? \n"))
            while not(nextMove>=0 and next < len(cases)):
                next = int(input("Not valid, where do you want to go ? \n"))
            
            x , y = cases[nextMove]
            plateau.movePlayer(player,cases[nextMove])  # Move player on the map
            player.move(x, y)   # Modifiate player attribute
            
    
        if noPlay == 1:
            coords = input("Give coordX, coordY and direction\n").split()
            coordX, coordY, direction = coords[0], coords[1], coords[2]
            if direction not in ["vertical", "horizontal"]:
                direction = "vertical"
            newWall = Wall()
            newWall.place(int(coordX), int(coordY), direction)
            player.useWall()

            while not plateau.placeWall(newWall):
                coords = input("Not valid\nGive another coordX, coordY and direction\n").split()
                coordX, coordY, direction = int(coords[0]), int(coords[1]), coords[2]
                if direction not in ["vertical", "horizontal"]:
                    direction = "vertical"
                newWall = Wall()
                newWall.place(int(coordX), int(coordY), direction)
                player.useWall()
    
    def start(self):
        i=0
        while(True):
            self.turn = i/2 + 1 
            
            print(self.plateau.affichagePlateau())
            choice = int(input(self.player1.name +", what do you want to do :\n 0 : move, 1 : place a wall"))
            self.play(self.plateau, self.player1, choice)
            if self.isWin(self.player1):
                return self.player1
            
            choice = int(input(self.player2.name +"What do you want to do :\n 0 : move, 1 : place a wall"))
            self.play(self.plateau, self.player2, choice)
            if self.isWin(self.player2):
                return self.player2
            
                        
