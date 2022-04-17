import pygame

from src import Board
from src import Player
from src import Wall
from src import Game
from src import Case

blackRGB = (0, 0, 0)
whiteRGB = (255, 255, 255)
greenRGB = (0, 255, 0)
blueRGB = (0, 0, 128)


def test():
    print("----------- DEBUT TEST -----------\n")

    board = Board.Board(9, "assets/Board.png")

    p0 = Player.Player(0, "Yanni", 0, 0, 9, "assets/Player1.png")
    p1 = Player.Player(1, "Yanni", 1, 0, 9, "assets/Player1.png")
    p2 = Player.Player(2, "Yanni", 2, 0, 9, "assets/Player1.png")
    p3 = Player.Player(3, "Yanni", 3, 0, 9, "assets/Player1.png")
    p4 = Player.Player(4, "Yanni", 4, 0, 9, "assets/Player1.png")
    p5 = Player.Player(5, "Yanni", 5, 0, 9, "assets/Player1.png")
    p6 = Player.Player(6, "Yanni", 6, 0, 9, "assets/Player1.png")
    p7 = Player.Player(7, "Yanni", 7, 0, 9, "assets/Player1.png")
    p8 = Player.Player(8, "Yanni", 8, 0, 9, "assets/Player1.png")

    lWall = []

    w1 = Wall.Wall(1, 1, "d", "assets/Wall.png")
    w2 = Wall.Wall(3, 3, "u", "assets/Wall.png")
    w3 = Wall.Wall(5, 5, "r", "assets/Wall.png")
    w4 = Wall.Wall(7, 7, "l", "assets/Wall.png")
    w5 = Wall.Wall(8, 0, "d", "assets/Wall.png")

    lWall.append(w1)
    lWall.append(w2)
    lWall.append(w3)
    lWall.append(w4)

    board.placePlayer(p0.coordX, p0.coordY, p0)
    board.placePlayer(p1.coordX, p1.coordY, p1)
    board.placePlayer(p2.coordX, p2.coordY, p2)
    board.placePlayer(p3.coordX, p3.coordY, p3)
    board.placePlayer(p4.coordX, p4.coordY, p4)
    board.placePlayer(p5.coordX, p5.coordY, p5)
    board.placePlayer(p6.coordX, p6.coordY, p6)
    board.placePlayer(p7.coordX, p7.coordY, p7)
    board.placePlayer(p8.coordX, p8.coordY, p8)

    print("w1 has been placed : ", board.placeWall(w1.coordX, w1.coordY, w1.orientation))
    print("w2 has been placed : ", board.placeWall(w2.coordX, w2.coordY, w2.orientation))
    print("w3 has been placed : ", board.placeWall(w3.coordX, w3.coordY, w3.orientation))
    print("w4 has been placed : ", board.placeWall(w4.coordX, w4.coordY, w4.orientation))
    print("w5 has been placed : ", board.placeWall(w5.coordX, w5.coordY, w5.orientation))

    print(board.strPlateau())

    print("\n   Wall:")
    for wall in lWall:
        print(wall)
    print("\n")

    print("\n----------- FIN TEST -----------")


def launchGame():
    p1 = Player.Player(1, "Henri", 5, 0, 9, "assets/Joueur1.png")
    p2 = Player.Player(2, "Zichun", 5, 8, 9, "assets/Joueur1.png")
    board = Board.Board(Board.boardLength, "assets/Board.png")

    game = Game.Game(board, p1, p2)
    game.start()


def launchWindowGame():
    board = Board.Board(9, "assets/Board.png")

    # Initialisation des variables de jeu
    p1 = Player.Player(1, "Henri", board.length // 2, 0, 9, "assets/Player1.png")
    p2 = Player.Player(2, "Zichun", board.length // 2, board.length - 1, 9, "assets/Player2.png")

    iLen = Board.windowsLength / (board.length + 2)
    p1.image = pygame.transform.scale(p1.image, (iLen, iLen))
    p2.image = pygame.transform.scale(p2.image, (iLen, iLen))

    game = Game.Game(board, p1, p2)

    pygame.init()
    screen = Board.initBoardDisplay()

    running = True
    mainPlayer = p1
    winner = None

    while running:
        # Affiche les cases
        game.board.updateScreen(screen)

        # Affichage player
        screen.blit(game.p1.image, ((p1.coordX + 1) * iLen, (p1.coordY + 1) * iLen))
        screen.blit(game.p2.image, ((p2.coordX + 1) * iLen, (p2.coordY + 1) * iLen))

        # Handler event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Default exit for pygame
                running = False

            # Sortie de jeu avec ECHAP
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            # Affichage
            winner, played = game.eventHandler(screen, event, mainPlayer)

            # Change tour joueur
            if played:
                if mainPlayer == p1:
                    mainPlayer = p2
                else:
                    mainPlayer = p1

            if winner is not None:
                running = False

        pygame.display.flip()


    pygame.quit()
    return winner


def winnerShow(player: Player.Player):
    pygame.init()
    x, y = 400, 100
    screen = pygame.display.set_mode((x, y))

    screen.fill(whiteRGB)
    pygame.display.set_caption("Congratulation !")

    font = pygame.font.Font('freesansbold.ttf', 25)
    msg = player.name + " a gagné !"
    text = font.render(msg, True, blackRGB, whiteRGB)
    textRect = text.get_rect()
    textRect.center = (x // 2, y // 2)

    running = True
    while running:
        screen.blit(text, textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

    pygame.quit()


def testWinnerShow():
    p1 = Player.Player(1, " winner", 0, 0, 0, "assets/Player1.png")
    winnerShow(p1)


if __name__ == "__main__":
    player = launchWindowGame()
    if player is not None:
        winnerShow(player)

    else:
        p1 = Player.Player(3, "NONE", 0, 0, 0, "assets/Player1.png")
        winnerShow(p1)
