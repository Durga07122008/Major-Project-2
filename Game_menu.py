import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 550))
mainmenu_background = pygame.image.load('mainmenubackground.jpg').convert()

cursor = pygame.image.load("cursorgun.png").convert_alpha()
cursor = pygame.transform.scale(cursor, (32,32))
pygame.mouse.set_cursor((0,0), cursor)

def start_clicked():
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        screen.blit(mainmenu_background, (0,0))
        pygame.display.update()
        pygame.time.Clock().tick(60)
def characters_clicked():
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        screen.blit(mainmenu_background, (0,0))
        pygame.display.update()
        pygame.time.Clock().tick(60)
def settings_clicked():
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        screen.blit(mainmenu_background, (0,0))
        pygame.display.update()
        pygame.time.Clock().tick(60)
