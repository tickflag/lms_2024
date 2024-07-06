import pygame

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/exit.png')
        self.image = pygame.transform.scale(
            img, (32, 48))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
