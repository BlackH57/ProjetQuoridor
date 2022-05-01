import pygame
import config
pygame.init()


COLOR_TEXT = pygame.Color("black")

COLOR_WHITE = (255, 255, 255)


class Button:

    def __init__(self, function, x, y,  width, heigth, state, text ="button"):
        self.rect = pygame.Rect(x, y, width, heigth)

        self.color_out = config.BUTTON_COLOR_INACTIVE_OUT
        self.color_in = config.BUTTON_COLOR_INACTIVE_IN

        self.text = text
        self.txt_surface = config.FONT16.render(text, True, pygame.Color("black"))

        self.state = state
        self.function = function

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state


    def eventHandler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.rect.collidepoint(event.pos):
                self.color_out = config.BUTTON_COLOR_ACTIVE_OUT
                self.color_in = config.BUTTON_COLOR_ACTIVE_IN

                if self.function is not None:
                    self.function()

        if event.type == pygame.MOUSEBUTTONUP:
            self.color_out = config.BUTTON_COLOR_INACTIVE_OUT
            self.color_in = config.BUTTON_COLOR_INACTIVE_IN


    def draw(self, screen):
        # Blit the rect.
        pygame.draw.rect(screen, self.color_in, self.rect)
        pygame.draw.rect(screen, self.color_out, self.rect, 2)

        # Blit the text.
        decalage = len(self.text)
        absCoord = self.rect.x + self.rect.width // 2 - decalage*4
        ordCoord = self.rect.y + self.rect.height // 2 - 5
        screen.blit(self.txt_surface, (absCoord, ordCoord))


def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("test button")
    clock = pygame.time.Clock()
    button1 = Button(100, 100, 140, 32, "button1")
    button2 = Button(100, 300, 140, 32, "button2")
    buttons_list = [button1, button2]

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in buttons_list:
                box.eventHandler(event)

        screen.fill((30, 30, 30))
        for box in buttons_list:
            box.draw(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pygame.quit()
