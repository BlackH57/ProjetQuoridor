import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("test button")



COLOR_INACTIVE_IN = pygame.Color("lightgrey")
COLOR_ACTIVE_IN = pygame.Color("grey")

COLOR_INACTIVE_OUT = pygame.Color("grey")
COLOR_ACTIVE_OUT = pygame.Color("black")

COLOR_TEXT = pygame.Color("black")

COLOR_WHITE = (255, 255, 255)

FONT = pygame.font.Font(None, 32)

class Button:

    def __init__(self, x: int, y: int, w: int, h: int, text = "button"):
        self.rect = pygame.Rect(x, y, w, h)

        self.color_out = COLOR_INACTIVE_OUT
        self.color_in = COLOR_INACTIVE_IN

        self.text = text
        self.txt_surface = FONT.render(text, True, pygame.Color("black"))

    def eventHandler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.rect.collidepoint(event.pos):
                self.color_out = COLOR_ACTIVE_OUT
                self.color_in = COLOR_ACTIVE_IN

                print(self.text)

        if event.type == pygame.MOUSEBUTTONUP:
            self.color_out = COLOR_INACTIVE_OUT
            self.color_in = COLOR_INACTIVE_IN



    def draw(self, screen):
        # Blit the rect.
        pygame.draw.rect(screen, self.color_in, self.rect)
        pygame.draw.rect(screen, self.color_out, self.rect, 2)

        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))


def main():
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

        screen.fill(COLOR_WHITE)
        for box in buttons_list:
            box.draw(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pygame.quit()
