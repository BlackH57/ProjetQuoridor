import pygame
import config

class Text:

    def __init__(self, text, size, x, y, width, heigth):
        self.text = text
        self.rect = pygame.Rect(x, y, width, heigth)
        self.size = size
        FONT = pygame.font.Font(None, size)
        self.txt_surface = FONT.render(text, True, config.blackRGB)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

    def setText(self, text):
        self.text = text
        FONT = pygame.font.Font(None, self.size)
        self.txt_surface = FONT.render(text, True, config.blackRGB)



    def digitTextAdd(self, number, minNum = None, maxNum = None):
        if self.text.isdigit():
            new = int(self.text) + number
            if minNum <= new <= maxNum:
                self.setText(str(new))

    # Do nothing, for coherence purpose only
    def eventHandler(self, event):
        return
