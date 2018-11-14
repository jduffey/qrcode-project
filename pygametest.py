import pygame
from pygame.locals import *
import time
import jedhash
from pygame_config import config

SECRET = config['SECRET']
PERIOD_IN_SECONDS = config['PERIOD_IN_SECONDS']
WINDOW_TITLE = config['WINDOW_TITLE']
BORDER_THICKNESS = config['BORDER_THICKNESS']
ICON_SIZE_X = config['ICON_SIZE_X']
ICON_SIZE_Y = config['ICON_SIZE_Y']
NUMBER_OF_COLUMNS = config['NUMBER_OF_COLUMNS']
NUMBER_OF_ROWS = config['NUMBER_OF_ROWS']
MY_RED = config['MY_RED']
MY_ORANGE = config['MY_ORANGE']
MY_YELLOW = config['MY_YELLOW']
MY_GREEN = config['MY_GREEN']
MY_BLUE = config['MY_BLUE']
MY_VIOLET = config['MY_VIOLET']
MY_BROWN = config['MY_BROWN']
MY_GREY = config['MY_GREY']
MY_BLACK = config['MY_BLACK']
MY_WHITE = config['MY_WHITE']


def getColor(digitToUseForCurrentColor):
    digitToAssess = digitToUseForCurrentColor

    case1 = digitToAssess == '0' or digitToAssess == '8'
    case2 = digitToAssess == '1' or digitToAssess == '9'
    case3 = digitToAssess == '2' or digitToAssess == 'a'
    case4 = digitToAssess == '3' or digitToAssess == 'b'
    case5 = digitToAssess == '4' or digitToAssess == 'c'
    case6 = digitToAssess == '5' or digitToAssess == 'd'
    case7 = digitToAssess == '6' or digitToAssess == 'e'
    case8 = digitToAssess == '7' or digitToAssess == 'f'

    if case1:
        nextColor = MY_RED
    if case2:
        nextColor = MY_ORANGE
    if case3:
        nextColor = MY_YELLOW
    if case4:
        nextColor = MY_GREEN
    if case5:
        nextColor = MY_BLUE
    if case6:
        nextColor = MY_VIOLET
    if case7:
        nextColor = MY_BROWN
    if case8:
        nextColor = MY_GREY
    return nextColor

def drawHorizontalBorders():
    for i in range(0, NUMBER_OF_ROWS + 1):
        topLeftX = 0
        topLeftY = i * ( BORDER_THICKNESS + ICON_SIZE_Y )
        bottomRightX = APP_X_SIZE
        bottomRightY = BORDER_THICKNESS
        theRectangleToDraw = (topLeftX, topLeftY, bottomRightX, bottomRightY)
        pygame.draw.rect(screen, MY_BLACK, theRectangleToDraw)

def drawVerticalBorders():
    for i in range(0, NUMBER_OF_COLUMNS + 1):
        topLeftX = i * ( BORDER_THICKNESS + ICON_SIZE_X )
        topLeftY = 0
        bottomRightX = BORDER_THICKNESS
        bottomRightY = APP_Y_SIZE
        theRectangleToDraw = (topLeftX, topLeftY, bottomRightX, bottomRightY)
        pygame.draw.rect(screen, MY_BLACK, theRectangleToDraw)

def drawColorIcon(whichColumn, whichRow, digitToUseForCurrentColor):
    topLeftX = BORDER_THICKNESS + whichColumn * ( ICON_SIZE_X + BORDER_THICKNESS )
    topLeftY = BORDER_THICKNESS + whichRow * ( ICON_SIZE_Y + BORDER_THICKNESS )
    bottomRightX = ICON_SIZE_X
    bottomRightY = ICON_SIZE_Y
    theRectangleToDraw = (topLeftX, topLeftY, bottomRightX, bottomRightY)
    pygame.draw.rect(screen, getColor(digitToUseForCurrentColor), theRectangleToDraw)

def generateDigest(timeOffset):
    return jedhash.returnTheHash(SECRET, PERIOD_IN_SECONDS, timeOffset)


APP_X_SIZE = BORDER_THICKNESS + NUMBER_OF_COLUMNS * ( ICON_SIZE_X + BORDER_THICKNESS )
APP_Y_SIZE = BORDER_THICKNESS + NUMBER_OF_ROWS * ( ICON_SIZE_Y + BORDER_THICKNESS )

screen = pygame.display.set_mode((APP_X_SIZE, APP_Y_SIZE))
pygame.display.set_caption(WINDOW_TITLE)
pygame.mouse.set_visible(True)
rectangleThatIsTheSizeOfTheScreen = pygame.Surface(screen.get_size())
rectangleThatIsTheSizeOfTheScreen.fill(MY_WHITE)
screen.blit(rectangleThatIsTheSizeOfTheScreen, (0, 0))
pygame.display.flip()

pygame.init()
isDrawingActive = True


while isDrawingActive:

    print()
    print(time.time())

    for whichColumn in range(0, NUMBER_OF_COLUMNS):

        for whichRow in range(0, NUMBER_OF_ROWS):

            digestTimeOffset = PERIOD_IN_SECONDS * (whichColumn - whichRow)

            digestToUseForCurrentIcon = generateDigest(digestTimeOffset)

            digitToUseForCurrentColor = digestToUseForCurrentIcon[0]

            drawColorIcon(whichColumn, whichRow, digitToUseForCurrentColor)

    drawHorizontalBorders()
    drawVerticalBorders()

    pygame.display.flip()

    # if the 'X' button is pressed the window should close:
    Geesh = pygame.event.get()
    if len(Geesh) > 0:
        if Geesh[0].type == QUIT: isDrawingActive = False

    time.sleep(PERIOD_IN_SECONDS)