import pygame
import Game_menu

pygame.init()
state = 0

screen = pygame.display.set_mode((1000, 552))
mainmenu_background = pygame.image.load('mainmenubackground.jpg').convert()
mainmenu_background = pygame.transform.scale(mainmenu_background, (1000,552))

backbutton = pygame.image.load('backbutton.png').convert_alpha()
backbutton = pygame.transform.scale(backbutton, (100, 100))

cursor = pygame.image.load("cursorgun.png").convert_alpha()
cursor = pygame.transform.scale(cursor, (32,32))
pygame.mouse.set_cursor((0,0), cursor)

game_active = True

game_title = pygame.image.load("Game Title.png").convert_alpha()
game_title = pygame.transform.scale(game_title, (550,450))

startbutton = pygame.image.load("startbutton2.0.png").convert_alpha()
startbutton = pygame.transform.scale(startbutton, (200, 70))

charactersbutton = pygame.image.load("Characters.png").convert_alpha()
charactersbutton = pygame.transform.scale(charactersbutton, (200, 70))

settingsbutton = pygame.image.load("Settings.png").convert_alpha()
settingsbutton = pygame.transform.scale(settingsbutton, (200, 70))

quitbutton = pygame.image.load("quitbutton.png").convert_alpha()
quitbutton = pygame.transform.scale(quitbutton, (200, 70))

clickSound = pygame.mixer.Sound("gunshot.mp3")
mainmenumusic = pygame.mixer.Sound("mainmenumusic.mp3")
mainmenumusic.play()

class Chara():
    def __init__(self, name, image, location):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = image.get_rect(center = location)

clickstart = Chara("Start", startbutton, (800, 150))
clickcharacters = Chara("Character", charactersbutton, (800,250))
clicksettings = Chara("Settings", settingsbutton, (800,350))
clickquit = Chara("Quit", quitbutton, (800,450))

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
            mainmenumusic.fadeout(2000)
            state = Game_menu.start_clicked()
        elif state == 2:
            state = Game_menu.characters_clicked()
        elif state == 3:
            state = Game_menu.settings_clicked()
        elif state == 0:
            continue

    screen.blit(mainmenu_background, (0,0))
    screen.blit(game_title, (75,100))
    screen.blit(startbutton, clickstart.rect)
    screen.blit(charactersbutton, clickcharacters.rect)
    screen.blit(settingsbutton, clicksettings.rect)
    screen.blit(quitbutton, clickquit.rect)

    pygame.display.update()
    pygame.time.Clock().tick(60)