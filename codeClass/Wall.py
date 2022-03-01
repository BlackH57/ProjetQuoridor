import pygame

class Wall:

    def __init__(self, num, coordX, coordY, direction, imageFileName):
        self.num = num
        self.placed = False
        self.coordX = coordX
        self.coordY = coordY
        self.direction = direction
        self.image = pygame.image.load(imageFileName)

    def place(self, coordX, coordY, direction):
        """
        Set coordX, coordY and direction attribute
        """
        self.placed = True
        self.coordX = coordX
        self.coordY = coordY
        self.direction = direction

    def getPlaced(self):
        """
        Return the value of placed. True if it is placed, if not False
        """
        return self.placed

    def getCoord(self):
        """
        return a tuple as (x,y,direction)
        """
        return self.coordX, self.coordY, self.direction

    def __str__(self):
        """
        return the position of the wall.
        """
        return "("+str(self.coordX)+","+str(self.coordY)+") direction: " + self.direction