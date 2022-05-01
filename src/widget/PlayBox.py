import pygame

import config

pygame.init()
FONT = pygame.font.Font(None, 32)


class PlayBox:

    def __init__(self, x, y, width, height, nbCellule):
        self.rect = pygame.Rect(x, y, width, height)
        self.nbMaxCellule = nbCellule
        self.nbCellule = 0
        self.cellule = []
        self.celluleLength = (height-10) / nbCellule

    def addText(self, text):
        if self.nbCellule >= self.nbMaxCellule:
            self.cellule.pop(0)
        else:
            self.nbCellule = self.nbCellule + 1
        self.cellule.append(FONT.render(text, True, pygame.Color("black")))

    # Do nothing, for coherence purpose only
    def eventHandler(self, event):
        return

    def draw(self, screen):
        pygame.draw.rect(screen, config.lightGreyColor, self.rect)

        for i in range(self.nbCellule):
            screen.blit(self.cellule[i], (self.rect.x+5, self.rect.y+5 + i*self.celluleLength))
            # pygame.draw.rect(screen, config.whiteRGB, self.cellule[i].rect)