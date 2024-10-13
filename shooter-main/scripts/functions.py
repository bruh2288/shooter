import pygame

def load_image(path, size, colorkey):
        '''
        -path: путь к картинке
        -size: размер картинки
        -colorkey: цвет, который отвечает за прозрачность
        '''
        image = pygame.image.load(path).convert()
        image = pygame.transform.scale(image, size)
        image.set_colorkey(colorkey)
        return image