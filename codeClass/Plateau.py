class Plateau:
    length =9
    def __init__(self, length, player1, player2, imageFileName):
        """
        Initiate an instance of plateau.
        length : int, player1 : Player, player2 : Player, imageFileName : str
        """
        self.length = length    #for now must always be 9
        self.computerLength = 2*length-1
        self.plateau = []
        self.player1 = player1
        self.player2 = player2
        self.wallPlaced = []

        #init plateau
        for i in range(0,self.computerLength):
            self.plateau.append([0 for i in range(0,length)])


    def setPlayeur(self,noPlayer, player):
        """
        player : Player, noPlayer : 1 or 2
        set one of the player.
        """
        if (noPlayer == 1):
            self.player1 = player
        elif (noPlayer == 2):
            self.player2 = player
        else:
            print("f{noPplayer} n'est pas un chiffre valide")

    def placeWall(self, wall):
        """
        place a Wall on the map.
        wall: Wall. Must have direction, and coordonate initiate.
        """
        coordX, coordY, direction = wall.coordX, wall.coordY, wall.direction
        self.plateau[coordX][coordY] = 2
        self.placeWall.append(wall)

    def reachableFrom(self,coords):
        """
        coords : (int,int)
        Return a set of case accessible from coords
        """
        coordX, coordY = coords
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

        return {case for case in res}

    def affichagePlateau(self):
        """
        Return a string representing the actual disposition of the board
        """
        res = ""
        for i in range(0,self.computerLength):
            res+= '-'

        for i in range(0, self.computerLength):
            res+='|'
            for j in range(0, self.computerLength):
                if self.plateau[i][j] == 0: # nothing
                    res += " ■ "
                if self.plateau[i][j] == 1: # player1
                    res += " M "
                if self.plateau[i][j] == 2: # player2
                    res += " A "
                if self.plateau[i][j] == 3: # wall
                    res += "+++"

            res+='|\n'

        for i in range(0,self.computerLength+2):
            res+= '-'
        return res

    def __str__(self):
        """
        For now print affichagePlateau but later will print the code for the map.
        Exemple : P1(9,0)P2(9,17)w(9,7,H)w(15,5,V)
        """
        
        return self.affichagePlateau()