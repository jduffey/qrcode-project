###
### The "Watchgirl" project has been moved to https://github.com/jduffey/watchgirl
### 

# import pygame
# from pygame.locals import *
# import time
# import jedhash
# from pygame_config import config

# SECRET = config['SECRET']
# PERIOD_IN_SECONDS = config['PERIOD_IN_SECONDS']
# WINDOW_TITLE = config['WINDOW_TITLE']
# BORDER_THICKNESS = config['BORDER_THICKNESS']
# ICON_SIZE_X = config['ICON_SIZE_X']
# ICON_SIZE_Y = config['ICON_SIZE_Y']
# NUMBER_OF_COLUMNS = config['NUMBER_OF_COLUMNS']
# NUMBER_OF_ROWS = config['NUMBER_OF_ROWS']
# MY_RED = config['MY_RED']
# MY_ORANGE = config['MY_ORANGE']
# MY_YELLOW = config['MY_YELLOW']
# MY_GREEN = config['MY_GREEN']
# MY_BLUE = config['MY_BLUE']
# MY_VIOLET = config['MY_VIOLET']
# MY_BROWN = config['MY_BROWN']
# MY_GREY = config['MY_GREY']
# MY_BLACK = config['MY_BLACK']
# MY_WHITE = config['MY_WHITE']


# def getColor(digitToUseForColor):

#     if digitToUseForColor in {'0', '8'}:
#         nextColor = MY_RED
#     if digitToUseForColor in {'1', '9'}:
#         nextColor = MY_ORANGE
#     if digitToUseForColor in {'2', 'a'}:
#         nextColor = MY_YELLOW
#     if digitToUseForColor in {'3', 'b'}:
#         nextColor = MY_GREEN
#     if digitToUseForColor in {'4', 'c'}:
#         nextColor = MY_BLUE
#     if digitToUseForColor in {'5', 'd'}:
#         nextColor = MY_VIOLET
#     if digitToUseForColor in {'6', 'e'}:
#         nextColor = MY_BROWN
#     if digitToUseForColor in {'7', 'f'}:
#         nextColor = MY_GREY
#     return nextColor

# def drawHorizontalBorders():
#     for i in range(0, NUMBER_OF_ROWS + 1):
#         topLeftX = 0
#         topLeftY = i * ( BORDER_THICKNESS + ICON_SIZE_Y )
#         bottomRightX = APP_X_SIZE
#         bottomRightY = BORDER_THICKNESS
#         theRectangleToDraw = (topLeftX, topLeftY, bottomRightX, bottomRightY)
#         pygame.draw.rect(screen, MY_BLACK, theRectangleToDraw)

# def drawVerticalBorders():
#     for i in range(0, NUMBER_OF_COLUMNS + 1):
#         topLeftX = i * ( BORDER_THICKNESS + ICON_SIZE_X )
#         topLeftY = 0
#         bottomRightX = BORDER_THICKNESS
#         bottomRightY = APP_Y_SIZE
#         theRectangleToDraw = (topLeftX, topLeftY, bottomRightX, bottomRightY)
#         pygame.draw.rect(screen, MY_BLACK, theRectangleToDraw)

# def drawColorIcon(whichColumn, whichRow, digitToUseForColor):
#     topLeftX = BORDER_THICKNESS + whichColumn * ( ICON_SIZE_X + BORDER_THICKNESS )
#     topLeftY = BORDER_THICKNESS + whichRow * ( ICON_SIZE_Y + BORDER_THICKNESS )
#     bottomRightX = ICON_SIZE_X
#     bottomRightY = ICON_SIZE_Y
#     theRectangleToDraw = (topLeftX, topLeftY, bottomRightX, bottomRightY)
#     pygame.draw.rect(screen, getColor(digitToUseForColor), theRectangleToDraw)

# def generateDigest(timeOffset):
#     return jedhash.returnTheHash(SECRET, PERIOD_IN_SECONDS, timeOffset)


# APP_X_SIZE = BORDER_THICKNESS + NUMBER_OF_COLUMNS * ( ICON_SIZE_X + BORDER_THICKNESS )
# APP_Y_SIZE = BORDER_THICKNESS + NUMBER_OF_ROWS * ( ICON_SIZE_Y + BORDER_THICKNESS )

# screen = pygame.display.set_mode((APP_X_SIZE, APP_Y_SIZE))
# pygame.display.set_caption(WINDOW_TITLE)
# pygame.mouse.set_visible(True)
# rectangleThatIsTheSizeOfTheScreen = pygame.Surface(screen.get_size())
# rectangleThatIsTheSizeOfTheScreen.fill(MY_WHITE)
# screen.blit(rectangleThatIsTheSizeOfTheScreen, (0, 0))
# pygame.display.flip()

# pygame.init()
# isDrawingActive = True


# while isDrawingActive:

#     print()
#     digestsGeneratedThisLoop = 0
#     startTime = time.time()
#     print('Loop start: ' + str(startTime))

#     for whichColumn in range(0, NUMBER_OF_COLUMNS):

#         for whichRow in range(0, NUMBER_OF_ROWS):

#             digestTimeOffset = PERIOD_IN_SECONDS * (whichColumn - whichRow)

#             digestToUseForCurrentIcon = generateDigest(digestTimeOffset)
#             digestsGeneratedThisLoop += 1

#             digitToUseForColor = digestToUseForCurrentIcon[0]

#             drawColorIcon(whichColumn, whichRow, digitToUseForColor)

#     millisecondsOfLoop = 1000 * (time.time() - startTime)

#     drawHorizontalBorders()
#     drawVerticalBorders()

#     pygame.display.flip()

#     print('  ms taken: ' + str(millisecondsOfLoop))
#     print('   Digests: ' + str(digestsGeneratedThisLoop))

#     # if the 'X' button is pressed the window should close:
#     Geesh = pygame.event.get()
#     if len(Geesh) > 0:
#         if Geesh[0].type == QUIT: isDrawingActive = False

#     time.sleep(PERIOD_IN_SECONDS)