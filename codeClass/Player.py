import pygame

class Player:

    def __init__(self, name = "Player", nbWall = 9, noPlayer = None, mapLength = 9*2-1, imageFileName = None):
        """
        name : str, nbWall: int, noPlayer: 0 or 1, mapLength : int
        """
        self.name = name
        self.nbWall = nbWall
        self.noPlayer = noPlayer
        if imageFileName != None:
            self.image = pygame.image.load(imageFileName)
        self.coordX = mapLength/2
        if(self.noPlayer == 1):
            self.coordY = 0
        else:
            self.coordY = int(mapLength-1)

    def getCoord(self):
        """
        Return coordinate of the player as a tuple : (coordX, coordY) 
        """
        return self.coordX, self.coordY

    def move(self, coordX: int, coordY: int):
        """
        Coords ust be between 0 and Plateau.computerLength
        Set coordX and coordY attribute.
        """
        self.coordX = coordX
        self.coordY = coordY
        return True

    def setNoPlayer(self, noPlayer : int):
        self.noPlayer = noPlayer
        if noPlayer == 1:
            self.image = pygame.image.load("assets/Player1.png")
        elif noPlayer == 2:
            self.image = pygame.image.load("assets/Player2.png")
        else:
            print(str(noPlayer) + " is not a valid number")


    def useWall(self):
        self.nbWall -= 1
        

    def __str__(self):
        return "No player : "+ str(self.noPlayer)+" Name:"+ self.name +"nb wall(s) left : "+self.nbWall+" coords :" + str(self.getCoord())





