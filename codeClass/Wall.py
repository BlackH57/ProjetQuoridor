class Wall:

    def __init__(self, num):
        self.num = num
        self.placed = False
        self.coordX = None
        self.coordY = None

    def place(self, coordX, coordY):
        self.placed = True
        self.coordX = coordX
        self.coordY = coordY

    def getPlaced(self):
        return self.placed

    def getCoord(self):
        return "("+self.coordX+","+self.coordY+")"