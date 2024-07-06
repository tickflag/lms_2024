import sys
import pygame
from pygame.locals import *
import json

from Player import Player
from Button import Button
from World import World
from Diamond import Diamond
from data import *

#setting

screenWidth = 800
screenHeight = 800
fps = 60
fontName = "Bauhaus"
fontSize = 70
def drawText(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Огонь и Вода финал')
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
font = pygame.font.SysFont('Bauhaus 93', 70)
#colors
white = (255, 255, 255)

#images
backGroundImage = pygame.image.load('images/back_ground.jpg')
buttonStartImage = pygame.image.load('images/start_btn.png')
buttonStartImage = pygame.transform.scale(buttonStartImage, (256, 128))
buttonExitImage = pygame.image.load('images/exit_btn.png')
buttonExitImage = pygame.transform.scale(buttonExitImage, (256, 128))
buttonRestartImage = pygame.image.load('images/restart_btn.png')
buttonRestartImage = pygame.transform.scale(buttonRestartImage, (256, 128))

#
player = Player(736, 736)
startButton = Button(screenWidth // 2 - 250, screenHeight // 2 - 100, buttonStartImage)
exitButton = Button(screenWidth // 2 + 50, screenHeight // 2 - 100, buttonExitImage)
restartButton = Button(screenWidth // 2 - 250, screenHeight // 2 - 100, buttonRestartImage)
firstLevel = World(readDataFromTxt('maps/map1.txt'))
secondLevel = World(readDataFromTxt('maps/map2.txt'))
thirdLevel = World(readDataFromTxt('maps/map3.txt'))
fourthLevel = World(readDataFromTxt('maps/map4.txt'))
fifthLevel = World(readDataFromTxt('maps/map5.txt'))

blueDiamondGroup = firstLevel.blueDiamondGroup
redDiamondGroup = firstLevel.redDiamondGroup
lavaGroup = firstLevel.lavaGroup
waterGroup = firstLevel.waterGroup
exits = firstLevel.exits

#
blueScore = 0
redScore = 0
isMainMenu = True
currentLevel = 1
maxLevel = 5
isAlive = True
isWin = False

def prepareWorlds():
    global firstLevel 
    firstLevel = World(readDataFromTxt('maps/map1.txt'))
    global secondLevel 
    secondLevel = World(readDataFromTxt('maps/map2.txt'))
    global thirdLevel
    thirdLevel = World(readDataFromTxt('maps/map3.txt'))
    global fourthLevel
    fourthLevel = World(readDataFromTxt('maps/map4.txt'))
    global fifthLevel
    fifthLevel = World(readDataFromTxt('maps/map5.txt'))
    global blueDiamondGroup 
    blueDiamondGroup = firstLevel.blueDiamondGroup
    global redDiamondGroup 
    redDiamondGroup = firstLevel.redDiamondGroup
    global lavaGroup
    lavaGroup = firstLevel.lavaGroup
    global waterGroup
    waterGroup = firstLevel.waterGroup
    global exits
    exits = firstLevel.exits

while True:
    clock.tick(fps)
    keys = pygame.key.get_pressed()

    if (not isAlive):
        screen.fill(white)
        if (isWin):
            drawText('YOU WIN!', font, (0, 0, 0), 300, 200)
        if (restartButton.draw(screen)):
            isAlive = True
            isMainMenu = False
            isWin = False
            player.reset(736, 736)
            redScore = 0
            blueScore = 0
            currentLevel = 1
            prepareWorlds()
        if (exitButton.draw(screen)):
            pygame.quit()
            sys.exit()
            break

    elif (isMainMenu):
        screen.fill(white)
        if (startButton.draw(screen)):
            isMainMenu = False
        if (exitButton.draw(screen)):
            pygame.quit()
            sys.exit()
            break   

    elif (currentLevel == 1):
        screen.blit(backGroundImage, (0, 0))
        firstLevel.draw(screen)
        player.update(firstLevel, keys, screen)
        
        if (pygame.sprite.spritecollide(player, blueDiamondGroup, True)):
            blueScore += 1
        if (pygame.sprite.spritecollide(player, redDiamondGroup, True)):
            redScore += 1

            
        if (pygame.sprite.spritecollide(player, lavaGroup, True)):
            isAlive = False
        if (pygame.sprite.spritecollide(player, waterGroup, True)):
            isAlive = False
        blueDiamondGroup.draw(screen)
        redDiamondGroup.draw(screen)
        lavaGroup.draw(screen)
        waterGroup.draw(screen)
        exits.draw(screen)

        if (pygame.sprite.spritecollide(player, exits, True)):
            currentLevel += 1
            blueDiamondGroup = secondLevel.blueDiamondGroup
            redDiamondGroup = secondLevel.redDiamondGroup
            exits = secondLevel.exits
            lavaGroup = secondLevel.lavaGroup
            waterGroup = secondLevel.waterGroup
            player.reset(32, 736)
        
        

    elif (currentLevel == 2):
        screen.blit(backGroundImage, (0, 0))
        secondLevel.draw(screen)
        player.update(secondLevel, keys, screen)
        
        if (pygame.sprite.spritecollide(player, blueDiamondGroup, True)):
            blueScore += 1
        if (pygame.sprite.spritecollide(player, redDiamondGroup, True)):
            redScore += 1

        blueDiamondGroup.draw(screen)
        redDiamondGroup.draw(screen)
        lavaGroup.draw(screen)
        waterGroup.draw(screen)
        exits.draw(screen)

        if (pygame.sprite.spritecollide(player, lavaGroup, True)):
            isAlive = False
        if (pygame.sprite.spritecollide(player, waterGroup, True)):
            isAlive = False

        if (pygame.sprite.spritecollide(player, exits, True)):
            currentLevel += 1
            blueDiamondGroup = thirdLevel.blueDiamondGroup
            redDiamondGroup = thirdLevel.redDiamondGroup
            exits = thirdLevel.exits
            lavaGroup = thirdLevel.lavaGroup
            waterGroup = thirdLevel.waterGroup
            player.reset(32, 736)

    elif (currentLevel == 3):
        screen.blit(backGroundImage, (0, 0))
        thirdLevel.draw(screen)
        player.update(thirdLevel, keys, screen)

        if (pygame.sprite.spritecollide(player, blueDiamondGroup, True)):
            blueScore += 1

        if (pygame.sprite.spritecollide(player, redDiamondGroup, True)):
            redScore += 1


        blueDiamondGroup.draw(screen)
        redDiamondGroup.draw(screen)
        lavaGroup.draw(screen)
        waterGroup.draw(screen)
        exits.draw(screen)

        if (pygame.sprite.spritecollide(player, lavaGroup, True)):
            isAlive = False
        if (pygame.sprite.spritecollide(player, waterGroup, True)):
            isAlive = False

        if (pygame.sprite.spritecollide(player, exits, True)):
            currentLevel += 1
            blueDiamondGroup = fourthLevel.blueDiamondGroup
            redDiamondGroup = fourthLevel.redDiamondGroup
            exits = fourthLevel.exits
            lavaGroup = fourthLevel.lavaGroup
            waterGroup = fourthLevel.waterGroup
            player.reset(32, 736)

    elif (currentLevel == 4):
        screen.blit(backGroundImage, (0, 0))
        fourthLevel.draw(screen)
        player.update(fourthLevel, keys, screen)

        if (pygame.sprite.spritecollide(player, blueDiamondGroup, True)):
            blueScore += 1
        if (pygame.sprite.spritecollide(player, redDiamondGroup, True)):
            redScore += 1


        blueDiamondGroup.draw(screen)
        redDiamondGroup.draw(screen)
        lavaGroup.draw(screen)
        waterGroup.draw(screen)
        exits.draw(screen)

        if (pygame.sprite.spritecollide(player, lavaGroup, True)):
            isAlive = False
        if (pygame.sprite.spritecollide(player, waterGroup, True)):
            isAlive = False

        if (pygame.sprite.spritecollide(player, exits, True)):
            currentLevel += 1
            blueDiamondGroup = fifthLevel.blueDiamondGroup
            redDiamondGroup = fifthLevel.redDiamondGroup
            exits = fifthLevel.exits
            lavaGroup = fifthLevel.lavaGroup
            waterGroup = fifthLevel.waterGroup
            player.reset(32, 736)
    
    elif (currentLevel == 5):
        screen.blit(backGroundImage, (0, 0))
        fifthLevel.draw(screen)
        player.update(fifthLevel, keys, screen)

        if (pygame.sprite.spritecollide(player, blueDiamondGroup, True)):
            blueScore += 1
        if (pygame.sprite.spritecollide(player, redDiamondGroup, True)):
            redScore += 1


        blueDiamondGroup.draw(screen)
        redDiamondGroup.draw(screen)
        lavaGroup.draw(screen)
        waterGroup.draw(screen)
        exits.draw(screen)

        if (pygame.sprite.spritecollide(player, lavaGroup, True)):
            isAlive = False
        if (pygame.sprite.spritecollide(player, waterGroup, True)):
            isAlive = False

        if (pygame.sprite.spritecollide(player, exits, True)):
            isWin = True
            isAlive = False

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
            break
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                isMainMenu = True

    pygame.display.update()

pygame.quit()

