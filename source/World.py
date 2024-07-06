import pygame
from Diamond import Diamond
from Exit import Exit
from Lava import Lava
from Witch import Witch

class World:
    def __init__(self, data):
        self.blueDiamondGroup = pygame.sprite.Group()
        self.redDiamondGroup = pygame.sprite.Group()
        self.lavaGroup = pygame.sprite.Group()
        self.waterGroup = pygame.sprite.Group()
        self.exits = pygame.sprite.Group()
        self.tileList = []
        self.uploadImages()
        rowCount = 0
        for row in data:
            column = 0
            for tile in row:
                if (tile == 1):
                    self.createTile(self.block1Image, column, rowCount)
                if (tile == 2):
                    self.createTile(self.block2Image, column, rowCount)
                if (tile == 22):
                    self.createTile(self.block3Image, column, rowCount)
                if (tile == 23):
                    self.createTile(self.block4Image, column, rowCount)
                if (tile == 24):
                    self.createTile(self.block5Image, column, rowCount)
                if (tile == 25):
                    self.createTile(self.block6Image, column, rowCount)
                if (tile == 26):
                    self.createTile(self.block7Image, column, rowCount)
                if (tile == 5):
                    coin = Diamond(column * 32 + 16, rowCount * 32 + 16, 'blue_diamond')
                    self.blueDiamondGroup.add(coin)
                if (tile == 6):
                    coin = Diamond(column * 32 + 16, rowCount * 32 + 16, 'red_diamond')
                    self.redDiamondGroup.add(coin)
                if (tile == 7):
                    exitMark = Exit(column * 32, rowCount * 32 - 16)
                    self.exits.add(exitMark)
                if (tile == 8):
                    exitMark = Witch(column * 32, rowCount * 32 - 16)
                    self.exits.add(exitMark)
                if (tile == 3):
                    lavaMark = Lava(column * 32 + 16, rowCount * 32 + 16, 'lava')
                    self.lavaGroup.add(lavaMark)
                if (tile == 4):
                    waterMark = Lava(column * 32 + 16, rowCount * 32 + 16, 'water')
                    self.waterGroup.add(waterMark)
                column += 1
            rowCount += 1

    def createTile(self, imageName, columnCount, rowCount):
        image = pygame.transform.scale(imageName, (32, 32))
        imageRect = image.get_rect()
        imageRect.x = columnCount * 32
        imageRect.y = rowCount * 32
        tile = (image, imageRect)
        self.tileList.append(tile)

    def uploadImages(self):
        self.block1Image = pygame.image.load('images/stone1.png')
        self.block2Image = pygame.image.load('images/block_1.png')
        self.block3Image = pygame.image.load('images/block_2.png')
        self.block4Image = pygame.image.load('images/block_3.png')
        self.block5Image = pygame.image.load('images/block_4.png')
        self.block6Image = pygame.image.load('images/block_5.png')
        self.block7Image = pygame.image.load('images/block_6.png')

    def draw(self, screen):
        for tile in self.tileList:
            screen.blit(tile[0], tile[1])


