class Sprite():
    def __init__(self, x, y, image, speed):
        self.image = image
        self.rect = image.get_rect(center=(x,y))
        self.speed = speed

    def is_colide(self, other):
        return self.rect.colliderect(other.rect)
        
    def render(self, window):
        window.blit(self.image, self.rect)
