import pygame


class Surface:
    def __init__(self, x, y, width, heigth, color, name = "Surface"):
        self.rect = pygame.rect.Rect(x, y, width, heigth)
        self.components = []
        self.name = name

        self.color = color


    def addComponents(self, component):
        self.components.append(component)

    def eventHandler(self, event):
        for component in self.components:
            component.eventHandler(event)

    def draw(self, screen):
        if self.color is not None:
            pygame.draw.rect(screen, self.color, self.rect)

        for component in self.components:
            component.draw(screen, self)
