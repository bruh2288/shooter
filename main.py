import pygame

flags = pygame.RESIZABLE | pygame.SCALED
window = pygame.display.set_mode((800, 600), flags)
clock = pygame.time.Clock()

FPS = 60

background = pygame.image.load('images\\background.png')
background = pygame.transform.scale(background, (800, 600))
bullet = pygame.image.load('images\\bullet.png')
enemy = pygame.image.load('images\\enemy.png')
player = pygame.image.load('images\\player.png')

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.blit(background, (0,0))
    pygame.display.update()
    clock.tick(FPS)