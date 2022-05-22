import pygame

from src import Wall
from src import Player



class Case:

    def __init__(self, coordX: int, coordY: int, imageFileName: str):
        self.rightWall = None
        self.underWall = None
        self.player = None

        # Coordinate shouldn't be changed
        # May be removed later
        self._coordX = coordX
        self._coordY = coordY
        self.imageFileName = imageFileName
        self.image = pygame.image.load(imageFileName)
        self.rect = self.image.get_rect()


    def placeWall(self, wall: Wall):
        """
        wall : Wall
        Try to place a wall in the case. If failed return False, if succeeded return True.
        """

        if wall.orientation in ["r", "l"]:
            # Test if there's already a wall
            if self.underWall is not None:
                return False
            self.underWall = wall
            # print("underWall :", self.underWall.orientation)
            return True

        elif wall.orientation in ["u", "d"]:
            # Test if there's already a wall
            if self.rightWall is not None:
                return False
            self.rightWall = wall

            # print("rightWall :", self.rightWall.orientation)
            return True

        else:
            # If there's already a wall placed or the wall's orientation isn't good
            print("Error in wall orientation")
            return False


    def getCoords(self):
        """
        Return the case coords
        """
        return self._coordX, self._coordY


    def getWall(self):
        """
        Return the wall attached to the case
        """
        return self.rightWall, self.underWall


    def setPlayer(self, player: Player):
        """
        player : Player
        Try to place a Player in the case. If failed return False, if succeeded return True.
        """
        # Test if there's already a Player
        if self.player is not None:
            # print("Il y a deja un joueur ici")
            print(self.player)
            return False

        self.player = player
        # print("Le player", player.noPlayer, "a ete set")
        return True


    def removePlayer(self):
        """
        If there's a player, remove him.
        """
        self.player = None


    def switchAppearance(self, imageFileName: str):
        """
        imageFileName : str
        Change the appearance of the case
        """
        # tmp
        x = self.rect.x
        y = self.rect.y

        # load new image
        self.image = pygame.image.load(imageFileName)
        self.imageFileName = imageFileName
        self.rect = self.image.get_rect()

        # set new image coordinate
        self.rect.x = x
        self.rect.y = y


    def switchAppearanceDefault(self):
        if self.imageFileName == "assets/Case.png":
            self.switchAppearance("assets/CaseReachable.png")
        else:
            self.switchAppearance("assets/Case.png")

    def draw(self, screen, surface):
        return
        #screen.blit()

#    def eventHandler(self, screen, event):
#        if event.type == pygame.KEYDOWN:


    def __str__(self):
        """
        Return the str form of the case
        """

        x = str(self._coordX)

        y = str(self._coordY)

        p = "None"
        if self.player is not None:
            p = str(self.player.noPlayer)

        rw = "None"
        uw = "None"

        if self.rightWall is not None:
            if self.rightWall.orientation == "d":
                rw = "downward"
            elif self.rightWall.orientation == "u":
                rw = "upward"
            else:
                rw = "unknown"
        if self.underWall is not None:
            if self.underWall.orientation == "r":
                uw = "rightward"
            elif self.underWall.orientation == "l":
                uw = "leftward"
            else:
                uw = "unknown"

        return "(x,y): (" + x + "," + y + "), Player: " + p + ", rightWall: " + rw + ", underWall:" + uw
