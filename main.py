import pygame

pygame.init()

def main():
    print("--- Debut partie ---")

    width, height = 750, 750
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Quoridor")

    bgImage = pygame.image.load("assets/Plateau.png")
    bgImage = pygame.transform.scale(bgImage, window.get_size())
    background = bgImage.convert()

    run = True
    while run:

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False
           if event.type == pygame.K_ESCAPE:
               run = False

       window.blit(background, (0,0))

       # Rafraîchissement de l'écran
       pygame.display.flip()

    pygame.quit()
    print("--- Fin partie ---")

if __name__ == "__main__":
    main()