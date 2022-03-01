import pygame

class Player:

    def __init__(self, name, nbWall, noPlayer, mapLength, imageFileName):
        """
        name : str, nbWall: int, noPlayer: 0 or 1, mapLength : int
        """
        self.name = name
        self.nbWall = nbWall
        self.noPlayer = noPlayer
        self.image = pygame.image.load(imageFileName)
        self.coordX = mapLength/2
        if(self.noPlayer == 1):
            self.coordY = 0
        else:
            self.coordY = mapLength

    def getCoord(self):
        """
        Return coordinate of the player as a tuple : (coordX, coordY) 
        """
        return self.coordX, self.coordY

    def move(self, coordX, coordY):
        """
        coordX : int, coordY. 
        Must be between 0 and Plateau.computerLength
        Set coordX and coordY attribute.
        """
        self.coordX = coordX
        self.coordY = coordY

    def __str__(self):
        return "No player : "+ str(self.noPlayer)+" Name:"+ self.name +"nb wall(s) left : "+self.nbWall+" coords :" + str(self.getCoord())





