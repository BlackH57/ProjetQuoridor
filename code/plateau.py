class Plateau:
    __init__(self, length, player1, player2):
        self.length = length
        self.computerLength = 2*length
        self.plateau = []
        self.player1 = player1
        self.player2 = player2
        self.placedWall = []
        for i in range(0,length):
            self.plateau.append([0 for i in range(0,length)])

        def setPlayeur(noPlayer, player):

            if(not isinstanceof(noPlayer, int):
                print("Argument <noPlayer> non valide.")
                if(not isinstanceof(player, Player):
                    print("Argument <player> non valide.")
                return
            if (noPlayer == 1):
                self.player1 = player
            if (noPlayer == 2):
                self.player2 = player
            else:
                print("f{noPplayer} n'est pas un chiffre valide")
        
        def placeWall(wall):
            self.placedWall.append(wall)

        def affichagePlateau():
            for i in range(0,computerLength):
                res = ""
                for j in range(0, computerLength):
                    res = res + str(plateau[i][j])
                print(res)