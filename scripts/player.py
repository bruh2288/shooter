from scripts.sprite import *
import pygame

class Player(Sprite):
    def update(self):
        super().__init__()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def get_damage(self):
        self.health -= 1