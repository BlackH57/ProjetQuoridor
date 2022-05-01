import pygame
import config
import functools

from src.widget import Button
from src.widget import InputBox
from src.widget import Text
from src.widget import PlayBox
from src.widget import Surface

class Window:

    def __init__(self, name, lenght, width, color = config.whiteRGB):
        self.components = []
        self.name = name
        self.lenght = lenght
        self.width = width
        self.color = color

    def addComponents(self, component):
        self.components.append(component)


    # pygame
    def eventHandler(self, event):
        for component in self.components:
            component.eventHandler(event)

    def draw(self, screen):
        for component in self.components:
            component.draw(screen)

    def display(self):
        pygame.init()
        screen = pygame.display.set_mode((self.lenght, self.width))
        pygame.display.set_caption(self.name)

        run = True
        while run:
            if self.color is not None:
                screen.fill(self.color)
            self.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        break

                for component in self.components:
                    component.eventHandler(event)


            pygame.display.flip()

        pygame.quit()


def menuWindow():
    menuWind = Window("menu", 500, 500, config.smoothColorRGB)

    nomBox = InputBox.InputBox(150, 100, 200, 50, "")

    launchGame = functools.partial(Window.display, gameWindow())
    openParam = functools.partial(Window.display, parametersWindow(menuWind))
    pvpButton = Button.Button(launchGame, 150, 175, 200, 50, "PvP", "contre Joueur")
    pvjButton = Button.Button(launchGame, 150, 250, 200, 50, "PvA", "contre Agent")

    paramButton = Button.Button(openParam, 425, 25, 50, 50, "parametre", "Parametre")
    quoridor_text = Text.Text("QUORIDOR", 45, 5, 5, 200, 100)

    menuWind.addComponents(quoridor_text)
    menuWind.addComponents(pvpButton)
    menuWind.addComponents(pvjButton)
    menuWind.addComponents(nomBox)
    menuWind.addComponents(paramButton)

    return menuWind


def parametersWindow(screen):
    parametersWind = Window("parameters", config.paramWindSize[0], config.paramWindSize[1], config.lightGreyColor)
    if screen is not None:
        returnMenu = functools.partial(Window.display, screen)
        menuButton = Button.Button(returnMenu, config.paramMenuBouton[0], config.paramMenuBouton[1], config.paramMenuBouton[2], config.paramMenuBouton[3], None, "Back")
    else:
        menuButton = Button.Button(None, config.paramMenuBouton[0], config.paramMenuBouton[1], config.paramMenuBouton[2], config.paramMenuBouton[3], None, "Back")

    #boardLengthDescTxt = Text.Text("Longueur du plateau", )
    boardLengthtxt = Text.Text("9", config.paramBoardLengthtxt[0], config.paramBoardLengthtxt[1], config.paramBoardLengthtxt[2], config.paramBoardLengthtxt[3], config.paramBoardLengthtxt[4])

    minus = functools.partial(boardLengthtxt.digitTextAdd, -1, config.minBoardLength, config.maxBoardLength)
    plus = functools.partial(boardLengthtxt.digitTextAdd, +1, config.minBoardLength, config.maxBoardLength)

    boardLengthButtonSub = Button.Button(minus, config.paramBoardLengthButtonSub[0], config.paramBoardLengthButtonSub[1], config.paramBoardLengthButtonSub[2], config.paramBoardLengthButtonSub[3], None, "-")

    boardLengthButtonAdd = Button.Button(plus, config.paramBoardLengthButtonAdd[0], config.paramBoardLengthButtonAdd[1], config.paramBoardLengthButtonAdd[2], config.paramBoardLengthButtonAdd[3], None, "+")

    parametersWind.addComponents(boardLengthButtonSub)
    parametersWind.addComponents(boardLengthtxt)
    parametersWind.addComponents(boardLengthButtonAdd)

    parametersWind.addComponents(menuButton)

    return parametersWind


def gameWindow():
    gameWind = Window("game", config.gameWindSize[0], config.gameWindSize[1])

    # Left side
    boardSurface = Surface.Surface(config.gameBoardSurface[0], config.gameBoardSurface[1], config.gameBoardSurface[2], config.gameBoardSurface[3], config.orangeRGB, "board")  # Will contain the game
    # Init the game
    
    
    forfaitButton = Button.Button(None, config.gameForfaitButton[0], config.gameForfaitButton[1], config.gameForfaitButton[2], config.gameForfaitButton[3], None, "ABANDON")  # To give up
    suggestButton = Button.Button(None, config.gameSuggestButton[0], config.gameSuggestButton[1], config.gameSuggestButton[2], config.gameSuggestButton[3], None, "SUGGEST")     # To see what an agent would play

    # Right side
    moveBox = PlayBox.PlayBox(config.gameMoveBox[0], config.gameMoveBox[1], config.gameMoveBox[2], config.gameMoveBox[3], config.gameMoveBox[4])    # Show the previous play
    saveButton = Button.Button(None, config.gameSaveButton[0], config.gameSaveButton[1], config.gameSaveButton[2], config.gameSaveButton[3], None, "SAVE")  # Button to save a game
    loadButton = Button.Button(None, config.gameLoadButton[0], config.gameLoadButton[1], config.gameLoadButton[2], config.gameLoadButton[3], None, "LOAD")  # Button to load a game

    rotateButton = Button.Button(None, config.gameRotateButton[0], config.gameRotateButton[1], config.gameRotateButton[2], config.gameRotateButton[3], "horizontal", "ROTATE")  # Button to rotate the walls

    # Add all components in the window
    gameWind.addComponents(boardSurface)
    gameWind.addComponents(forfaitButton)
    gameWind.addComponents(suggestButton)
    gameWind.addComponents(moveBox)
    gameWind.addComponents(saveButton)
    gameWind.addComponents(loadButton)
    gameWind.addComponents(rotateButton)


    return gameWind


def endWindow():
    endWind = Window("end", config.endWindSize[0], config.endWindSize[1])

    return endWind


menu = menuWindow()
parameters = parametersWindow(None)
game = gameWindow()
end = endWindow()

mainWindows = [menu, parameters, game, end]


if __name__ == "__main__":
    mainWindows[0].display()
