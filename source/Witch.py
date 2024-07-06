import pygame

class Witch(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/witch.png')
        self.image = pygame.transform.scale(
            img, (128, 128))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

