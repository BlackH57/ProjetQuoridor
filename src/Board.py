import pygame
from src import Case
from src import Wall
from src import Player

boardLength = 9
windowsLength = 1000

class Board:

    def __init__(self, length: int, imageFileName: str):
        """
        Initiate an instance of plateau.
        length is the length of the plate, imageFileName is the name of the file containing the assets
        """

        self.length = length
        self.plateau = []
        for i in range(length):
            self.plateau.append([Case.Case(i, j, "assets/Case.png") for j in range(length)])

        # imageFileName may be removed later because it would be automatically generated
        if imageFileName is not None:
            self.image = pygame.image.load(imageFileName)


    def placeWall(self, coordX: int, coordY: int, orientation: str):
        """
        coordX : int must be between 0 and self.length according to orientation
        coordY : int must be between 0 and self.length
        orientation : str must be in "r", "l", "u", "d"
        Try to put a wall in the case at coordinates coordX, coordY. Return True if succeeded and False otherwise
        """
        if not(0 <= coordX < self.length - 1 and 0 <= coordY < self.length - 1):
            return False
        mainCase = self.plateau[coordX][coordY]

        # On the vertical line
        if orientation in ["r", "l"] and mainCase.underWall is None:
            # if it is facing to the right, must be one away from the end of the board and the case right to the right must be free
            if orientation == "r" and coordX < self.length - 1 and self.plateau[coordX + 1][coordY].underWall is None:
                distantCase = self.plateau[coordX + 1][coordY]
                # if the other wall on the case is looking downward we can't place the wall
                if mainCase.rightWall is None or mainCase.rightWall.orientation == "u":
                    wall1 = Wall.Wall(coordX, coordY, "r", "assets/Wall.png")
                    wall2 = Wall.Wall(coordX + 1, coordY, "l", "assets/Wall.png")
                    mainCase.placeWall(wall1)
                    distantCase.placeWall(wall2)

                    # print(1, mainCase, distantCase)
                    return True

            elif orientation == "l" and coordX > 1 and self.plateau[coordX - 1][coordY].underWall is None:
                distantCase = self.plateau[coordX - 1][coordY]
                if distantCase.rightWall is None or distantCase.rightWall.orientation == "u":
                    wall1 = Wall.Wall(coordX, coordY, "l", "assets/Wall.png")
                    wall2 = Wall.Wall(coordX - 1, coordY, "r", "assets/Wall.png")
                    mainCase.placeWall(wall1)
                    distantCase.placeWall(wall2)

                    # print(2, mainCase, distantCase)
                    return True

        # On the horizontal line
        elif orientation in ["u", "d"] and mainCase.rightWall is None:
            # if it is facing to the down, must be one away from the end of the board and the case just below  must be free
            if orientation == "d" and coordY < self.length - 1 and self.plateau[coordX][coordY + 1].rightWall is None:
                distantCase = self.plateau[coordX][coordY + 1]
                # if the other wall on the case is looking to the right we can't place the wall
                if mainCase.underWall is None or mainCase.underWall.orientation == "r":
                    wall1 = Wall.Wall(coordX, coordY, "d", "assets/Wall.png")
                    wall2 = Wall.Wall(coordX, coordY + 1, "u", "assets/Wall.png")
                    mainCase.placeWall(wall1)
                    distantCase.placeWall(wall2)

                    # print(3, mainCase, distantCase)
                    return True

            elif orientation == "u" and coordY > 1 and self.plateau[coordX][coordY - 1].rightWall is None:
                distantCase = self.plateau[coordX][coordY - 1]
                if distantCase.underWall is None or distantCase.underWall.orientation == "r":
                    wall1 = Wall.Wall(coordX, coordY, "u", "assets/Wall.png")
                    wall2 = Wall.Wall(coordX, coordY - 1, "d", "assets/Wall.png")
                    mainCase.placeWall(wall1)
                    distantCase.placeWall(wall2)

                    # print(4, mainCase, distantCase)
                    return True

        return False


    def placePlayer(self, coordX: int, coordY: int, player: Player):
        """
        coordX : int must be between 0 and self.length
        coordY : int must be between 0 and self.length
        player : Player
        Try to place a player on the board. If there's already a player on the case, he's removed.
        Return True if succeed, False otherwise
        """
        if 0 <= coordX < self.length and 0 <= coordY < self.length:
            self.plateau[coordX][coordY].setPlayer(player)
            player.move(coordX, coordY)
            return True
        return False


    def removePlayer(self, coordX: int, coordY: int):
        """
        coordX : int must be between 0 and self.length
        coordY : int must be between 0 and self.length
        Remove the player at coords
        Return True if succeed, False otherwise
        """
        if 0 <= coordX < self.length and 0 <= coordY < self.length:
            self.plateau[coordX][coordY].removePlayer()
            return True
        return False


    def movePlayer(self, player: Player, case: Case):
        """
        player : Player
        case : Case
        move player to case
        """
        # stock coordinate
        cx, cy = case.getCoords()
        px, py = player.getCoords()

        # Move the player on the grid and update player coords
        self.removePlayer(px, py)
        self.placePlayer(cx, cy, player)


    def reachableCase(self, coordX: int, coordY: int):
        """
        coordX : int must be between 0 and self.length
        coordY : int must be between 0 and self.length
        Return a list of case that are reachable from coordX, coordY
        """
        if not (0 <= coordX < self.length and 0 <= coordY < self.length):
            print("Wrong coordinate")
            return []

        res = []
        # If we want to go left
        # If we are one case afar from the edge and there's no wall between
        if coordX < self.length - 1 and self.plateau[coordX][coordY].rightWall is None:
            # print("looking for : ", coordX + 1, ",", coordY)
            # If the case is free we add
            if self.plateau[coordX + 1][coordY].player is None:
                res.append(self.plateau[coordX + 1][coordY])
                # print(coordX + 1, ",", coordY, "has been append")

            # If the case is already taken by a player
            # Check if the next case is free and there's no wall
            elif coordX < self.length - 2:
                # and there's no wall nor players behind the player
                if self.plateau[coordX + 1][coordY].rightWall is None:
                    if self.plateau[coordX + 2][coordY].player is None:
                        res.append(self.plateau[coordX + 2][coordY])

                # and there's a wall behind the player
                else:
                    if coordY >= 1:
                        upperCase = self.plateau[coordX + 1][coordY - 1]
                        if upperCase.underWall is None and upperCase.player is None:
                            res.append(upperCase)
                    if coordY < self.length - 1:
                        lowerCase = self.plateau[coordX + 1][coordY + 1]
                        if self.plateau[coordX + 1][coordY].underWall is None and lowerCase.player is None:
                            res.append(lowerCase)
            # else:
                # print("Nothing has been append")
        # If we want to go right
        # If we are one case afar from the edge and there's no wall between
        if coordX >= 1 and self.plateau[coordX - 1][coordY].rightWall is None:
            # If the case is free we add
            if self.plateau[coordX - 1][coordY].player is None:
                res.append(self.plateau[coordX - 1][coordY])

            # If the case is already taken by a player
            # Check if the next case is free and there's no wall
            elif coordX >= 2:
                # and there's no wall behind the player
                if self.plateau[coordX - 1][coordY].rightWall is None:
                    if self.plateau[coordX - 2][coordY].player is None:
                        res.append(self.plateau[coordX - 2][coordY])
                else:
                    if coordX >= 1:
                        upperCase = self.plateau[coordX - 1][coordY - 1]
                        if upperCase.underWall is None and upperCase.player is None:
                            res.append(upperCase)
                    if coordY < self.length - 1:
                        lowerCase = self.plateau[coordX - 1][coordY + 1]
                        if self.plateau[coordX - 1][coordY].underWall is None and lowerCase.player is None:
                            res.append(lowerCase)

        # If we want to go up
        # If we are one case afar from the edge and there's no wall between
        if coordY >= 1 and self.plateau[coordX][coordY - 1].underWall is None:
            # If the case is free we add
            if self.plateau[coordX][coordY - 1].player is None:
                res.append(self.plateau[coordX][coordY - 1])

            # If the case is already taken by a player
            # Check if the next case is free and there's no wall
            elif coordY >= 2:
                # and there's no wall behind the player
                if self.plateau[coordX][coordY - 1].underWall is None:
                    if self.plateau[coordX][coordY - 2].player is None:
                        res.append(self.plateau[coordX][coordY - 2])
                else:
                    if coordX >= 1:
                        leftCase = self.plateau[coordX - 1][coordY - 1]
                        if leftCase.rightWall is None and leftCase.player is None:
                            res.append(leftCase)
                    if coordX < self.length - 1:
                        rightCase = self.plateau[coordX + 1][coordY - 1]
                        if self.plateau[coordX][coordY - 1].rightWall is None and rightCase.player is None:
                            res.append(rightCase)

        # If we want to go down
        # If we are one case afar from the edge and there's no wall between
        if coordY < self.length - 1 and self.plateau[coordX][coordY].underWall is None:
            # If the case is free we add
            if self.plateau[coordX][coordY + 1].player is None:
                res.append(self.plateau[coordX][coordY + 1])

            # If the case is already taken by a player
            # Check if the next case is free and there's no wall
            elif coordY < self.length - 2:
                # and there's no wall nor players behind the player
                if self.plateau[coordX][coordY + 1].underWall is None:
                    if self.plateau[coordX][coordY + 2].player is None:
                        res.append(self.plateau[coordX][coordY + 2])

                # and there's a wall behind the player
                else:
                    if coordX >= 1:
                        leftCase = self.plateau[coordX - 1][coordY + 1]
                        if leftCase.rightWall is None and leftCase.player is None:
                            res.append(leftCase)
                    if coordX < self.length - 1:
                        rightCase = self.plateau[coordX + 1][coordY + 1]
                        if self.plateau[coordX][coordY + 1].rightWall is None and rightCase.player is None:
                            res.append(rightCase)

        res = list(set(res))
        # print("  reachable:\n", res)
        return res   # Delete the cases that appears several times.


    def strPlateau(self):
        """
        Return a string representing the actual disposition of the board
        """
        res = ""

        for i in range(self.length+1):
            res += "__"

        res += "\n"

        for lCases in self.plateau:
            res += "|"
            for case in lCases:
                if case.player is None:
                    res += " "
                else:
                    res += str(case.player.noPlayer)
                if case.underWall is None:
                    res += " "
                else:
                    res += "+"
            res += "|\n|"

            for case in lCases:
                # x, y = case.getCoords()
                if case.rightWall is None and case.underWall is None:
                    res += "  "  # str(y) +

                elif case.underWall is not None:
                    if case.underWall.orientation == "r":  # and case.underWall.orientation == "d":
                        res += " +"
                    else:
                        res += "  "  # str(y) +

                elif case.rightWall.orientation == "d":
                    res += "++"
                else:
                    res += "+ "

            res += "|\n"

        for i in range(self.length+1):
            res += "__"
        return res


    def __str__(self):
        """
        For now is strPlateau but should be something like
        #length#/p1(x,y,nbWall)//p2(x,y,nbWall)/w(x,y,orientation) ...
        :return:
        """
        return self.strPlateau()


    def updateScreen(self, window: pygame.Surface):
        """
        Update appearence of lisf of all cases in the window
        """

        caseLength = windowsLength / (self.length + 2)

        for cases in self.plateau:
            for case in cases:
                x, y = case.getCoords()

                image = case.image
                image = pygame.transform.scale(image, (caseLength, caseLength))

                # imageTest = pygame.image.load("assets/CaseReachable.png")
                # imageTest = pygame.transform.scale(imageTest, (caseLength, caseLength))

                window.blit(image, ((x + 1) * caseLength, (y + 1) * caseLength))


    def mPosConvert(self, coordX: int, coordY: int):
        caseLength = windowsLength / (self.length + 2)
        return int(coordX//caseLength) - 1, int(coordY//caseLength) - 1


    def switchAppearanceReachable(self, window: pygame.surface, coordX, coordY):
        # x, y = self.mPosConvert(coordX, coordY)
        reachableCase = self.reachableCase(coordX, coordY)
        for case in reachableCase:
            case.switchAppearanceDefault()
        # return reachableCase # not used


def initBoard():
    size = windowsLength, windowsLength
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Quoridor project")
    screen.fill((150, 50, 10))
    return screen
