import pygame
pygame.init()

# Basic color
blackRGB = (0, 0, 0)
whiteRGB = (255, 255, 255)
greenRGB = (0, 255, 0)
blueRGB = (0, 0, 128)
orangeRGB = (255, 100, 0)
smoothColorRGB = (150, 10, 20)
lightGreyColor = pygame.Color("lightgrey")

# Basic Font
FONT16 = pygame.font.Font(None, 16)
FONT32 = pygame.font.Font(None, 32)

# Button config
BUTTON_COLOR_INACTIVE_IN = pygame.Color("lightgrey")
BUTTON_COLOR_ACTIVE_IN = pygame.Color("grey")

BUTTON_COLOR_INACTIVE_OUT = pygame.Color("grey")
BUTTON_COLOR_ACTIVE_OUT = pygame.Color("black")

# InputBox config
INPUTBOX_COLOR_INACTIVE = pygame.Color('lightskyblue3')
INPUTBOX_COLOR_ACTIVE = pygame.Color('dodgerblue2')


# WINDOW CONFIG

# parameters
paramWindSize = 500, 400
paramMenuBouton = 25, 25, 50, 25
paramBoardLengthtxt = 20, 350, 103, 25, 25
paramBoardLengthButtonSub = 325, 100, 25, 25
paramBoardLengthButtonAdd = 375, 100, 25, 25
minBoardLength = 0
maxBoardLength = 15

# game
gameWindSize = 900, 700
gameBoardSurface = 50, 50, 500, 500
gameForfaitButton = 50, 600, 150, 50
gameSuggestButton = 300, 600, 150, 50
gameMoveBox = 650, 50, 200, 400, 12
gameSaveButton = 650, 475, 75, 25
gameLoadButton = 775, 475, 75, 25
gameRotateButton = 725, 550, 50, 50

# end
endWindSize = 1000, 500


# board configuration
boardLength = 9
boardLengthWindow = gameWindSize[1] # Will be changed later for gameBoardSurface[3]
caseLength = boardLengthWindow / (boardLength + 2)
defaultbWall = 9