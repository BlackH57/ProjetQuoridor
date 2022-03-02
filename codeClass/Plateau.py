import pygame
from codeClass.Player import Player
from codeClass.Wall import Wall

class Plateau:
    length =9
    def __init__(self, length = 9, player1 = None, player2 = None, imageFileName = "assets/Plateau.png"):
        """
        Initiate an instance of plateau.
        length : int, player1 : Player, player2 : Player, imageFileName : str
        """
        self.length = length    #for now must always be 9
        self.computerLength = 2*length -1
        self.plateau = []
        self.player1 = player1
        self.player2 = player2
        self.wallPlaced = []

        self.image = pygame.image.load(imageFileName)

        #init plateau
        for i in range(0,self.computerLength):
            self.plateau.append([0 for i in range(0,self.computerLength)])

        self.plateau[player1.coordX][player1.coordY] = 1
        print("("+str(player2.coordX)+","+str(player2.coordY)+" computerLength:"+ str(self.computerLength))
        self.plateau[player2.coordX][player2.coordY] = 2

    def setPlayeur(self,noPlayer : int, player : Player):
        """
        player : Player, noPlayer : 1 or 2
        set one of the player.
        """
        if (noPlayer == 1):
            self.player1 = player
        elif (noPlayer == 2):
            self.player2 = player
        else:
            print(noPlayer, "n'est pas un chiffre valide")

    def placeWall(self, wall : Wall):
        """
        place a Wall on the map.
        wall: Wall. Must have direction, and coordonate initiate.
        """
        coordX, coordY, direction = wall.coordX, wall.coordY, wall.direction
        if not((coordX%2 == 1 and direction == "vertical") or (coordY%2 == 1 and direction == "horizontal")):
            return False

        if wall.direction == "horizontal" and self.plateau[coordX][coordY] == 0 and self.plateau[coordX+1][coordY] == 0 and self.plateau[coordX+2][coordY] == 0 and coordX<=self.computerLength-3:
            self.wallPlaced.append(wall)
            self.plateau[coordX][coordY] = 3
            self.plateau[coordX+1][coordY] = 3
            self.plateau[coordX+2][coordY] = 3
            return True
        elif wall.direction == "vertical" and self.plateau[coordX][coordY] == 0 and self.plateau[coordX][coordY+1] == 0 and self.plateau[coordX][coordY+2] == 0 and coordY<=self.computerLength-3:
            self.wallPlaced.append(wall)
            self.plateau[coordX][coordY] = 3
            self.plateau[coordX][coordY+1] = 3
            self.plateau[coordX][coordY+2] = 3
            return True
        
        return False

    def reachableFrom(self, coordX, coordY):
        """
        coords : (int,int)
        Return a set of case accessible from coords
        """
        # coordX, coordY = coords
        res = []

        if coordX<= self.computerLength-2 and self.plateau[coordX+1][coordY] == 0 and self.plateau[coordX+2][coordY] == 0:
            res.append((coordX + 2, coordY))

        elif coordX<= self.computerLength-4 and self.plateau[coordX+1][coordY] == 0 and self.plateau[coordX+2][coordY] in [1,2]:
            if self.plateau[coordX+3][coordY] == 0:
                res.append((coordX+4, coordY))
            else:
                if coordY<= self.computerLength - 2 and self.plateau[coordX+2][coordY+1] == 0:
                    res.append((coordX+2, coordY+2))
                if coordY>=2 and self.plateau[coordX+2][coordY-1] ==  0:
                    res.append((coordX+2, coordY-2))


        if coordY<= self.computerLength-2 and self.plateau[coordX][coordY+1] == 0 and self.plateau[coordX][coordY+2] == 0:
            res.append((coordX, coordY + 2))

        elif coordY<= self.computerLength-4 and self.plateau[coordX][coordY+1] == 0 and self.plateau[coordX][coordY+2] in [1,2]:
            if self.plateau[coordX][coordY+3] == 0:
                res.append((coordX, coordY+4))
            else:
                if coordX<= self.computerLength - 2 and self.plateau[coordX+1][coordY+2] == 0:
                    res.append((coordX+2, coordY+2))
                if coordX>=2 and self.plateau[coordX-1][coordY+2] ==  0:
                    res.append((coordX-2, coordY+2))


        if coordX>= 2 and self.plateau[coordX-1][coordY] == 0 and self.plateau[coordX-2][coordY] == 0:
            res.append((coordX - 2, coordY))

        elif coordX>=4 and self.plateau[coordX-1][coordY] == 0 and self.plateau[coordX-2][coordY] in [1,2]:
            if self.plateau[coordX-3][coordY] == 0:
                res.append((coordX-4, coordY))
            else:
                if coordY>= 2 and self.plateau[coordX-2][coordY-1] == 0:
                    res.append((coordX-2,coordY-2))
                if coordY<= self.computerLength -2 and self.plateau[coordX-2][coordY+1] == 0:
                    res.append((coordX-2, coordY+2))

        if coordY>= 2 and self.plateau[coordX][coordY - 1] == 0 and self.plateau[coordX][coordY - 2] == 0:
            res.append((coordX, coordY - 2))
        
        elif coordY>=4 and self.plateau[coordX][coordY-1] == 0 and self.plateau[coordX][coordY-2] in [1,2]:
            if self.plateau[coordX][coordY-3] == 0:
                res.append((coordX, coordY-4))
            else:
                if coordY>= 2 and self.plateau[coordX-1][coordY-2] == 0:
                    res.append((coordX-2,coordY-2))
                if coordY<= self.computerLength -2 and self.plateau[coordX+1][coordY-2] == 0:
                    res.append((coordX+2, coordY-2))

        return list(set(res))
    
    
    def movePlayer(self, player, coords):
        self.plateau[player.coordX][player.coordY] = 0
        self.plateau[coords[0]][coords[1]] = player.noPlayer

    def affichagePlateau(self):
        """
        Return a string representing the actual disposition of the board
        """
        res = ""
        for i in range(0,self.computerLength):
            res+= '---'
        res+='\n'
        for i in range(0, self.computerLength):
            res+='|'
            for j in range(0, self.computerLength):
                # print("coords = ("+str(i)+","+str(j)+")" + "computerLength ="+str(self.computerLength))
                if self.plateau[j][i] == 0: # nothing
                    res += " ■ "
                if self.plateau[j][i] == 1: # player1
                    res += " M "
                if self.plateau[j][i] == 2: # player2
                    res += " A "
                if self.plateau[j][i] == 3: # wall
                    res += "+++"

            res+='|\n'

        for i in range(0,self.computerLength):
            res+= '---'
        return res

    def __str__(self):
        """
        For now print affichagePlateau but later will print the code for the map.
        Exemple : P1(9,0)P2(9,17)w(9,7,H)w(15,5,V)
        """
        
        return self.affichagePlateau()
