import pygame

class Diamond(pygame.sprite.Sprite):
    def __init__(self, x, y, fileName):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(f'images/{fileName}.png')
        self.image = pygame.transform.scale(image, (16, 16))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

