from scripts.sprite import *

class Enemy(Sprite):
    def __init__(self, x, y, image, speed, health):
        super().__init__(x, y, image, speed)
        self.health = health

    def update(self):
        self.rect.y += self.speed

    def get_damage(self):
        self.health -= 1