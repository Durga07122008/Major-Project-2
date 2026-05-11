import pygame
import Game_menu

pygame.init()
state = 0

screen = pygame.display.set_mode((1000, 550))
mainmenu_background = pygame.image.load('mainmenubackground.jpg').convert()
mainmenu_background = pygame.transform.scale(mainmenu_background, (1000,550))

cursor = pygame.image.load("cursorgun.png").convert_alpha()
cursor = pygame.transform.scale(cursor, (32,32))
pygame.mouse.set_cursor((0,0), cursor)

game_active = True

game_title = pygame.image.load("Game Title.png").convert_alpha()
game_title = pygame.transform.scale(game_title, (650,450))

startbutton = pygame.image.load("startbutton2.0.png").convert_alpha()
startbutton = pygame.transform.scale(startbutton, (250, 90))

charactersbutton = pygame.image.load("Characters.png").convert_alpha()
charactersbutton = pygame.transform.scale(charactersbutton, (250, 90))

settingsbutton = pygame.image.load("Settings.png").convert_alpha()
settingsbutton = pygame.transform.scale(settingsbutton, (250, 90))

quitbutton = pygame.image.load("quitbutton.png").convert_alpha()
quitbutton = pygame.transform.scale(quitbutton, (250, 90))

clickSound = pygame.mixer.Sound("gunshot.mp3")

pygame.display.toggle_fullscreen()
class Chara():
    def __init__(self, name, image, location):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = image.get_rect(center = location)

clickstart = Chara("Start", startbutton, (800, 250))
clickcharacters = Chara("Character", charactersbutton, (800,350))
clicksettings = Chara("Settings", settingsbutton, (800,450))
clickquit = Chara("Quit", quitbutton, (800,550))

while game_active:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if clickstart.rect.collidepoint(event.pos):
                clickSound.play()
                state = 1
            elif clickcharacters.rect.collidepoint(event.pos):
                clickSound.play()
                state = 2
            elif clicksettings.rect.collidepoint(event.pos):
                clickSound.play()
                state = 3
            elif clickquit.rect.collidepoint(event.pos):
                clickSound.play()
                state = 0
                raise SystemExit
            
        if state == 1:
            Game_menu.start_clicked()
        elif state == 2:
            Game_menu.characters_clicked()
        elif state == 3:
            Game_menu.settings_clicked()

    screen.blit(mainmenu_background, (0,0))
    screen.blit(game_title, (75,150))
    screen.blit(startbutton, clickstart.rect)
    screen.blit(charactersbutton, clickcharacters.rect)
    screen.blit(settingsbutton, clicksettings.rect)
    screen.blit(quitbutton, clickquit.rect)

    pygame.display.update()
    pygame.time.Clock().tick(60)