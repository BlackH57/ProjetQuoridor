class Player:

    def __init__(self, name, nbWall, noPlayer, mapLength):
        self.name = name
        self.nbWall = nbWall
        self.noPlayer = noPlayer

        self.coordX = 5
        if(self.noPlayer == 0):
            self.coordY = 0
        else:
            self.coordY = mapLength

    def getCoord(self):
        return "("+str(self.coordX)+","+str(self.coordY)+")"

    def move(self, direction):
        if (direction == "N"):
            self.coordY += 1
        if (direction == "S"):
            self.coordY -= 1
        if (direction == 'E'):
            self.coordX -= 1
        if (direction == 'N'):
            self.coordX += 1



    def jouer(self, typePlay):
        if(typePlay == 0): #place wall
            if(self.nbWall>0):
                self.nbWall-=1

            else:
                print("Tu n'as plus de mur !")

        if(typePlay == 1): #move player
            direction = input("north : N, east : E, ouest : O, south : S ")
            self.move(direction)


    def __str__(self):
        return "No player : "+ self.noPlayer+" Name: f{self.name} nbBrick : "+self.nbWall+" coord :" + self.getCoord()





