import pygame

import config


class Wall:

    def __init__(self, coordX: int, coordY: int, orientation: str, imageFileName: str):
        # may be removed later. Coords are already given by the case the wall is in
        self.coordX = coordX
        self.coordY = coordY

        self.orientation = orientation  # can be u (upward), d (downward), l (leftward), r (rightward)
        self.image = pygame.image.load(imageFileName)


    def setCoords(self, coordX, coordY):
        """
        Change coords attributes.
        """
        self.coordX, self.coordY = coordX, coordY

    # may be obsolete
    def getCoords(self):
        """
        Return the wall's coords
        """
        return self.coordX, self.coordY


    def setOrientation(self, orientation):
        """
        Change orientation attribute.
        """
        # Try if the orientation is valid
        if orientation in ["u", "d", "l", "r"]:
            self.orientation = orientation
            return True

        return False


    def __str__(self):
        """
        Return wall coordinates and orientation
        """
        x, y = str(self.coordX), str(self.coordY)
        return "(" + x + "," + y + ") orientation: " + self.orientation

    def draw(self, screen):
        caseLength = config.caseLength
        if self.orientation == "r":
            imageUnderWall = self.image
            decalage = caseLength * 85 / 100
            centrage = caseLength * 10 / 100
            imageUnderWall = pygame.transform.scale(imageUnderWall, (caseLength * 2 * 90 / 100, caseLength * 15 / 100))  # caseLength * 2 * 85 / 100, caseLength * 30 / 100
            screen.blit(imageUnderWall, (self.coordX * caseLength + caseLength * 25 / 100 + decalage, (self.coordY + 1) * caseLength + decalage + centrage))