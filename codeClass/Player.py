import pygame
window_length = 1000

class Player:

    def __init__(self, name="Player", nbWall=9, noPlayer = 1, mapLength=9 * 2 - 1, imageFileName = "assets/Joueur1.png"):
        """
        name : str, nbWall: int, noPlayer: 0 or 1, mapLength : int
        """
        self.name = name
        self.nbWall = nbWall
        self.noPlayer = noPlayer
        self.image = pygame.image.load(imageFileName)
        self.image = pygame.transform.scale(self.image,(window_length*0.065,window_length*0.065))
        self.rect = self.image.get_rect()
        self.coordX = int(mapLength / 2)
        if self.noPlayer == 1:
            self.coordY = 0
        else:
            self.coordY = int(mapLength - 1)
        self.rect.x = window_length*0.074+window_length*0.098*self.coordX/2  # les nombres pas rond au debut c'est vraiment parceque je sais pas coder mais c'est normal
        self.rect.y = window_length*0.075+window_length*0.098*self.coordY/2  # ca tombe a peu pres juste mais y a des ajustements a faire

    def getCoord(self):
        """
        Return coordinate of the player as a tuple : (coordX, coordY) 
        """
        return self.coordX, self.coordY

    def move(self, coordX: int, coordY: int):
        """
        Coords ust be between 0 and Plateau.computerLength
        Set coordX and coordY attribute.
        """
        self.coordX = coordX
        self.coordY = coordY
        self.rect.x = window_length * 0.074 + window_length * 0.098 * self.coordX / 2 # toujours le meme pb mais trkl
        self.rect.y = window_length * 0.075 + window_length * 0.098 * self.coordY / 2
        return True

    def setNoPlayer(self, noPlayer : int):
        self.noPlayer = noPlayer
        if noPlayer == 1:
            self.image = pygame.image.load("assets/Player1.png")
        elif noPlayer == 2:
            self.image = pygame.image.load("assets/Player2.png")
        else:
            print(str(noPlayer) + " is not a valid number")


    def useWall(self):
        if self.nbWall>0:
            self.nbWall -= 1
        else:
            print("Tu n'as plus de mur !")
        
        

    def __str__(self):
        return "No player : "+ str(self.noPlayer)+" Name:"+ self.name +"nb wall(s) left : "+self.nbWall+" coords :" + str(self.getCoord())





