import pygame

class Button:

    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.isClicked = False

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()

        if (self.rect.collidepoint(pos)):
            if (pygame.mouse.get_pressed()[0] == 1 and (not self.isClicked)):
                action = True
                self.isClicked = True

        if (pygame.mouse.get_pressed()[0] == 0):
            self.isClicked = False

        screen.blit(self.image, self.rect)

        return action
