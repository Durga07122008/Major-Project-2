import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 552))
mainmenu_background = pygame.image.load('mainmenubackground.jpg').convert()
mainmenu_background = pygame.transform.scale(mainmenu_background, (1000,552))

cursor = pygame.image.load("cursorgun.png").convert_alpha()
cursor = pygame.transform.scale(cursor, (32,32))
pygame.mouse.set_cursor((0,0), cursor)

class Chara():
    def __init__(self, name, image, location):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = image.get_rect(center = location)

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
    characterselectionbar = pygame.image.load("characterselectionbar.png").convert_alpha()
    characterselectionbar = pygame.transform.scale(characterselectionbar, (375, 500))
    play1title = pygame.image.load("Player1title.png").convert_alpha()
    play1title = pygame.transform.scale(play1title, (182, 80))
    play2title = pygame.image.load("Player2title.png").convert_alpha()
    play2title = pygame.transform.scale(play2title, (182, 80))
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        screen.blit(mainmenu_background, (0,0))
        screen.blit(characterselectionbar, (60,20))
        screen.blit(characterselectionbar, (560,20))
        screen.blit(play1title, (140,50))
        screen.blit(play2title, (650,50))
        pygame.display.update()
        pygame.time.Clock().tick(60)

def settings_clicked():
    characterselectionbar = pygame.image.load("characterselectionbar.png").convert_alpha()
    characterselectionbar = pygame.transform.scale(characterselectionbar, (950, 500))
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        screen.blit(mainmenu_background, (0,0))
        screen.blit(characterselectionbar, (30,20))
        pygame.display.update()
        pygame.time.Clock().tick(60)
