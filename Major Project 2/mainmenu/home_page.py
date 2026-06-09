import pygame
import Game_menu

pygame.init()
state = 0

screen = pygame.display.set_mode((1000, 552))
mainmenu_background = pygame.image.load('mainmenubackground.jpg').convert()
mainmenu_background = pygame.transform.scale(mainmenu_background, (1000,552))

player1charc = pygame.image.load('Player1mainmenu.png').convert_alpha()
player1charc = pygame.transform.scale(player1charc, (150, 34))

player2charc = pygame.image.load('Player2mainmenu.png').convert_alpha()
player2charc = pygame.transform.scale(player2charc, (150, 33))

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

selected_characters = ["Adventurer", "Battlemage"]
menu_frame_p1 = 0
menu_frame_p2 = 0
menu_timer = 0
menu_ani_speed = 5

while game_active:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        
        if state == 0: 
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
                    raise SystemExit
            
    if state == 1:
        mainmenumusic.fadeout(2000)
        state = Game_menu.start_clicked()
        
    elif state == 2:
        menu_result = Game_menu.characters_clicked()
        if menu_result == 0:
            state = 0
        else:
            selected_characters = menu_result
            state = 0
            
    elif state == 3:
        state = Game_menu.settings_clicked()

    if state == 0:
        current_anim_p1 = Game_menu.animations[selected_characters[0]]
        current_anim_p2 = Game_menu.animations[selected_characters[1]]
        
        if menu_frame_p1 >= len(current_anim_p1):
            menu_frame_p1 = 0
        if menu_frame_p2 >= len(current_anim_p2):
            menu_frame_p2 = 0

        menu_timer += 1
        if menu_timer >= menu_ani_speed:
            menu_frame_p1 = (menu_frame_p1 + 1) % len(current_anim_p1)
            menu_frame_p2 = (menu_frame_p2 + 1) % len(current_anim_p2)
            menu_timer = 0
            
        img_p1 = current_anim_p1[menu_frame_p1]
        img_p2 = current_anim_p2[menu_frame_p2]
        
        title_rect = game_title.get_rect(center = (300, 300))
        if selected_characters[0] == "Battlemage":
            rect_p1 = img_p1.get_rect(center=(75, 450))
            rect_p2 = img_p2.get_rect(center=(325, 475))
        elif selected_characters[1] == "Battlemage": 
            rect_p2 = img_p2.get_rect(center=(325, 450))
            rect_p1 = img_p1.get_rect(center=(75, 475))
        elif selected_characters[0] and selected_characters[1] == "Battlemage":
            rect_p1 = img_p1.get_rect(center=(75, 450))
            rect_p2 = img_p2.get_rect(center=(325, 425))
        else:
            rect_p1 = img_p1.get_rect(center=(75, 475))
            rect_p2 = img_p2.get_rect(center=(325, 475))

        p1_banner_rect = player1charc.get_rect(center=(75, 375))
        p2_banner_rect = player2charc.get_rect(center=(325, 375))

        screen.blit(mainmenu_background, (0,0))
        screen.blit(game_title, title_rect)

        screen.blit(player1charc, p1_banner_rect)
        screen.blit(player2charc, p2_banner_rect)
        screen.blit(img_p1, rect_p1)
        screen.blit(img_p2, rect_p2) 

        screen.blit(startbutton, clickstart.rect)
        screen.blit(charactersbutton, clickcharacters.rect)
        screen.blit(settingsbutton, clicksettings.rect)
        screen.blit(quitbutton, clickquit.rect)

        pygame.display.update()

    pygame.time.Clock().tick(60)