import pygame


class Player:

    def __init__(self, noPlayer: int, name: str, coordX: int, coordY: int, nbWall: int, imageFileName: str):
        self.noPlayer = noPlayer
        self.name = name
        self.nbWall = nbWall
        self.coordX = coordX
        self.coordY = coordY
        self.imageFileName = imageFileName
        self.image = pygame.image.load(imageFileName)
        self.rect = self.image.get_rect()


    def move(self, coordX: int, coordY: int):
        """
        coordX : int
        coordY : int
        Change the player's coordinate
        """
        self.coordX = coordX
        self.coordY = coordY


    def getCoords(self):
        """
        Return coordinate of the player as a tuple : (coordX, coordY)
        """
        return self.coordX, self.coordY


    def useWall(self):
        """
        Try to decrement nbWall. If nbWall superior to 0 succeed and return True, otherwise fail and return False.
        """
        if self.nbWall > 0:
            self.nbWall -= 1
            print(self.nbWall, " wall(s) left.")
            return True

        return False


    def __str__(self):
        np = str(self.noPlayer)
        nw = str(self.nbWall)
        c = str(self.getCoords())
        return "No player : " + np + " Name:" + self.name + "nb wall(s) left : " + nw + " coords :" + c


    def draw(self, screen, imageLength):
        screen.blit(self.image, ((self.coordX + 1) * imageLength, (self.coordY + 1) * imageLength))
