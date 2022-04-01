import pygame
import codeClass.Player as Player
import codeClass.Plateau as Plateau
import codeClass.Game as Game
import codeClass.Wall as Wall

pygame.init()


def main():
    print("--- Debut partie ---")
    p1 = Player.Player("Joueur1", 9, 1, 17, "assets/Joueur1.png")
    p2 = Player.Player("Joueur1", 9, 2, 17, "assets/Joueur2.png")
    plateau = Plateau.Plateau(9, p1, p2, "assets/Plateau.png")
    game = Game.Game(plateau, p1, p2)

    width, height = 1000, 1000
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Quoridor")

    bgImage = pygame.image.load("assets/Plateau.png")
    bgImage = pygame.transform.scale(bgImage, window.get_size())
    background = bgImage.convert()

    run = True
    while run:
        window.blit(background, (0, 0))

        window.blit(game.player1.image, game.player1.rect)
        window.blit(game.player2.image, game.player2.rect)
        #print(game.plateau.affichagePlateau())


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

                if event.key == pygame.K_s:
                    p1.move(p1.coordX, p1.coordY + 2)
                if event.key == pygame.K_q:
                    p1.move(p1.coordX-2, p1.coordY)
                if event.key == pygame.K_z:
                    p1.move(p1.coordX, p1.coordY-2)
                if event.key == pygame.K_d:
                    p1.move(p1.coordX+2, p1.coordY)




        # Rafraichissement de l'ecran
        pygame.display.flip()

    pygame.quit()
    print("--- Fin partie ---")


if __name__ == "__main__":
    main()

try:
    pygame.quit()
finally:
    print(" --- Fin du main ---")
