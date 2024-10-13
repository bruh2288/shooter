from scripts.sprite import *
import pygame

class Bullet(Sprite):
    def update(self):
        self.rect.y -= self.speed
        