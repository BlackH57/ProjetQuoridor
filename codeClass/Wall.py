import pygame

class Wall:

    def __init__(self, coordX = None, coordY = None, direction = None, imageFileName = "assets/Wall.png"):
        self.placed = False
        self.coordX = coordX
        self.coordY = coordY
        self.direction = direction
        self.image = pygame.image.load(imageFileName)

    def place(self, coordX : int, coordY : int, direction : str):
        """
        Set coordX, coordY and direction attribute
        """
        if not self.placed:
            self.placed = True
            self.coordX = coordX
            self.coordY = coordY
            self.direction = direction
    

    def rotate(self):
        if self.direction == "vertical":
            self.direction = "horizontal"
        else:
            self.direction = "vertical"
            
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
