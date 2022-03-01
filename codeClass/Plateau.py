from codeClass import Player

class Plateau:
    length =9
    def __init__(self, length, player1, player2):
        self.length = length
        self.computerLength = 2*length-1
        self.plateau = []
        self.player1 = player1
        self.player2 = player2
        self.placedWall = []
        for i in range(0,self.computerLength):
            self.plateau.append([0 for i in range(0,length)])

    def setPlayeur(self,noPlayer, player):

        if(not isinstance(noPlayer, int)):
            print("Argument <noPlayer> non valide.")
            if(not isinstance(player, Player)):
                print("Argument <player> non valide.")
                return
        if (noPlayer == 1):
            self.player1 = player
        if (noPlayer == 2):
            self.player2 = player
        else:
            print("f{noPplayer} n'est pas un chiffre valide")
        
    def placeWall(self, wall):
        self.placedWall.append(wall)

    def affichagePlateau(self):
        for i in range(0, self.computerLength):
            res = ""
            for j in range(0, self.computerLength):
                res = res + str(self.plateau[i][j])
            print(res)
            return res

    def __str__(self):
        return self.affichagePlateau()