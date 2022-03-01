import pygame

class Game:

    def __init__(self, plateau, player1, player2):
        self.plateau = plateau
        self.player1 = player1
        self.player2 = player2
        self.turn = 0
    
    def isWin(self, joueur):
        return (joueur.coordY == 0 and joueur.noPlayer == 2) or (joueur.coordY == self.plateau.computerLength and joueur.noPlayer == 1) 

    