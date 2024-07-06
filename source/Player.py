import sys
import pygame
from pygame.locals import *

class Player:
    def __init__(self, x, y):
        self.imagesRight = []
        self.imagesLeft = []
        self.imagesStay = []
        self.index = 0
        self.counter = 0
        self.tickCounter = 0
        self.uploadImages(2)
        self.image = self.imagesStay[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.xSpeed = 3
        self.ySpeed = 0
        self.inAir = False
        self.direction = 0
        self.jumpStrenght = 15
        self.gravity = 1

    def uploadImages(self, n):
        for number in range(1, 3):
            imageStay = pygame.image.load(f'images/person{number}.png')
            imageStay = pygame.transform.scale(imageStay, (30, 54))
            imageRight  = pygame.image.load(f'images/person_right{number}.png')
            imageRight = pygame.transform.scale(imageRight, (30, 54))
            imageLeft = pygame.image.load(f'images/person_left{number}.png')
            imageLeft = pygame.transform.scale(imageLeft, (30, 54))
            self.imagesRight.append(imageRight)
            self.imagesStay.append(imageStay)
            self.imagesLeft.append(imageLeft)

    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.xSpeed = 4
        self.ySpeed = 0
        self.direction = 0
        self.inAir = False
        self.index = 0
        self.tickCounter = 0

    def update(self, world, keys, screen):
        dx = 0
        dy = 0

        self.counter += 1
        if (self.counter == 5):
            self.counter = 0
            self.index += 1

        if (self.index > 1):
            self.index = 0

        dx += (keys[pygame.K_d] - keys[pygame.K_a]) * self.xSpeed

        if (keys[pygame.K_d]):
            self.direction = 1
        elif (keys[pygame.K_a]):
            self.direction = -1
        else:
            self.direction = 0

        if ((not self.inAir) and (keys[pygame.K_SPACE])):
            self.ySpeed = -self.jumpStrenght
            self.inAir = True

        self.ySpeed += 1 * self.gravity
        dy += self.ySpeed
        
        if ((not keys[pygame.K_a]) and (not keys[pygame.K_d])):
            self.counter = 0
            self.index = 0
            self.direction = 0

        if (self.direction == 1):
            self.image = self.imagesRight[self.index]
        if (self.direction == -1):
            self.image = self.imagesLeft[self.index]
        if (self.direction == 0):
            self.image = self.imagesStay[self.index]
       
        for tile in world.tileList:
            if (tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height)):
                dx = 0
            if (tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height)):
                if (self.ySpeed < 0):
                    dy = tile[1].bottom - self.rect.top
                    self.ySpeed = 0
                else:
                    dy = tile[1].top - self.rect.bottom
                    self.ySpeed = 0
                    self.inAir = False

        if (self.ySpeed != 0):
            self.inAir = True

        self.rect.x += dx
        self.rect.y += dy
        
        if (self.rect.top < 0):
            self.rect.top = 0
        if (self.rect.bottom > 800):
            self.rect.bottom = 800
        if (self.rect.right > 800):
            self.rect.right = 800
        if (self.rect.left < 0):
            self.rect.left = 0
        
        screen.blit(self.image, self.rect)
