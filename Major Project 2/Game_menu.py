import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 552))
mainmenu_background = pygame.image.load('mainmenubackground.jpg').convert()
mainmenu_background = pygame.transform.scale(mainmenu_background, (1000,552))

cursor = pygame.image.load("cursorgun.png").convert_alpha()
cursor = pygame.transform.scale(cursor, (32,32))
pygame.mouse.set_cursor((0,0), cursor)

clickSound = pygame.mixer.Sound("gunshot.mp3")

Leftbutton = pygame.image.load("Leftbutton.png").convert_alpha()
Leftbutton = pygame.transform.scale(Leftbutton, (50, 44.20))

Rightbutton = pygame.image.load("Rightbutton.png").convert_alpha()
Rightbutton = pygame.transform.scale(Rightbutton, (50, 50.49))

Selectbutton = pygame.image.load("Selectbutton.png").convert_alpha()
Selectbutton = pygame.transform.scale(Selectbutton, (300, 203.32))

class Chara():
    def __init__(self, name, image, location):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = image.get_rect(center = location)

backbutton = pygame.image.load('backbutton.png').convert_alpha()
backbutton = pygame.transform.scale(backbutton, (200, 133.33))
clickback = Chara("Back", backbutton, (50, 50))

ingame_music = pygame.mixer.Sound("ingame_music.mp3")

def start_clicked():
    active = True
    while active:
        for event in pygame.event.get():
            ingame_music.play(-1)
            if event.type == pygame.QUIT:
                ingame_music.stop()
                raise SystemExit
        screen.blit(mainmenu_background, (0,0))
        pygame.display.update()
        pygame.time.Clock().tick(60)

def characters_clicked():
    characterselectionbar = pygame.image.load("characterselectionbar.png").convert_alpha()
    characterselectionbar = pygame.transform.scale(characterselectionbar, (375, 500))

    clickleftp1 = Chara("Left", Leftbutton, (125, 450))
    clickleftp2 = Chara("Left", Leftbutton, (625, 450))
    clickrightp1 = Chara("Right", Rightbutton, (375, 450))
    clickrightp2 = Chara("Right", Rightbutton, (875, 450))
    clickselectp1 = Chara("Select", Selectbutton, (250, 450))
    clickselectp2 = Chara("Select", Selectbutton, (750, 450))

    play1title = pygame.image.load("Player1title.png").convert_alpha()
    play1title = pygame.transform.scale(play1title, (182, 80))
    play2title = pygame.image.load("Player2title.png").convert_alpha()
    play2title = pygame.transform.scale(play2title, (182, 80))

    Adventurer_idle = pygame.image.load("idle-ezgif.com-gif-to-sprite-converter.png").convert_alpha()
    Battlemage_idle = pygame.image.load("Battlemage Idle.png").convert_alpha()
    Owlet_idle = pygame.image.load("Owlet_Monster_Idle_4.png").convert_alpha()
    Pink_idle = pygame.image.load("Pink_Monster_Idle_4.png").convert_alpha()

    def load_framesy(sheet, total_frames):
        frames = []
        sheet_w, sheet_h = sheet.get_size()
        frame_w = sheet_w
        frame_h = sheet_h // total_frames
        for i in range(total_frames):
            x = 0
            y = i * frame_h
            img = sheet.subsurface(pygame.Rect(x, y, frame_w, frame_h))
            img = pygame.transform.scale(img, (200, 200))
            frames.append(img)
        return frames

    def load_framesx(sheet, total_frames):
        frames = []
        sheet_w, sheet_h = sheet.get_size()
        frame_w = sheet_w // total_frames
        frame_h = sheet_h 
        for i in range(total_frames):
            x = i * frame_w
            y = 0 
            img = sheet.subsurface(pygame.Rect(x, y, frame_w, frame_h))
            img = pygame.transform.scale(img, (150, 150))
            frames.append(img)
        return frames

    animations = {
        'Adventurer': load_framesx(Adventurer_idle, total_frames=8),
        'Battlemage': load_framesy(Battlemage_idle, total_frames=8),
        'Owlet Monster': load_framesx(Owlet_idle, total_frames=4),
        'Pink Monster': load_framesx(Pink_idle, total_frames=4)
    }

    current_statep1 = 'Adventurer'
    current_statep2 = 'Battlemage'

    char_rectp1 = animations[current_statep1][0].get_rect(center=(250, 250))
    char_rectp2 = animations[current_statep2][0].get_rect(center=(725, 250))

    frame_indexp1 = 0
    frame_indexp2 = 0
    frame_timer = 0
    ani_speed = 5

    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if clickback.rect.collidepoint(event.pos):
                    clickSound.play()
                    return 0
                if clickleftp1.rect.collidepoint(event.pos):
                    clickSound.play()
                    if current_statep1 == "Adventurer":
                        current_statep1 = "Pink Monster"
                    elif current_statep1 == "Battlemage":
                        current_statep1 = "Adventurer"
                    elif current_statep1 == "Owlet Monster":
                        current_statep1 = "Battlemage"
                    elif current_statep1 == "Pink Monster":
                        current_statep1 = "Owlet Monster"
                    frame_indexp1 = 0
                if clickleftp2.rect.collidepoint(event.pos):
                    clickSound.play()
                    if current_statep2 == "Adventurer":
                        current_statep2 = "Pink Monster"
                    elif current_statep2 == "Battlemage":
                        current_statep2 = "Adventurer"
                    elif current_statep2 == "Owlet Monster":
                        current_statep2 == "Battlemage"
                    elif current_statep2 == "Pink Monster":
                        current_statep2 = "Owlet Monster"
                    frame_indexp2 = 0
                if clickrightp1.rect.collidepoint(event.pos):
                    clickSound.play()
                    if current_statep1 == "Adventurer":
                        current_statep1 = "Battlemage"
                    elif current_statep1 == "Battlemage":
                        current_statep1 = "Owlet Monster"
                    elif current_statep1 == "Owlet Monster":
                        current_statep1 = "Pink Monster"
                    elif current_statep1 == "Pink Monster":
                        current_statep1 = "Adventurer"
                    frame_indexp1 = 0
                if clickrightp2.rect.collidepoint(event.pos):
                    clickSound.play()
                    if current_statep2 == "Adventurer":
                        current_statep2 = "Battlemage"
                    elif current_statep2 == "Battlemage":
                        current_statep2 = "Owlet Monster"
                    elif current_statep2 == "Owlet Monster":
                        current_statep2 = "Pink Monster"
                    elif current_statep2 == "Pink Monster":
                        current_statep2 = "Adventurer"
                    frame_indexp2 = 0
        
        current_animation_listp1 = animations[current_statep1]
        current_animation_listp2 = animations[current_statep2]

        frame_timer += 1
        if frame_timer >= ani_speed:
            frame_indexp1 = (frame_indexp1 + 1) % len(current_animation_listp1)
            frame_indexp2 = (frame_indexp2 + 1) % len(current_animation_listp2)
            frame_timer = 0
        
        current_imagep1 = current_animation_listp1[frame_indexp1]
        current_imagep2 = current_animation_listp2[frame_indexp2]
        
        
        screen.blit(mainmenu_background, (0,0))
        screen.blit(characterselectionbar, (60,20))
        screen.blit(characterselectionbar, (560,20))
        screen.blit(backbutton, clickback.rect)
        screen.blit(play1title, (140,50))
        screen.blit(play2title, (650,50))
        screen.blit(Leftbutton, clickleftp1.rect)
        screen.blit(Rightbutton, clickrightp1.rect)
        screen.blit(Selectbutton, clickselectp1.rect)
        screen.blit(Leftbutton, clickleftp2.rect)
        screen.blit(Rightbutton, clickrightp2.rect)
        screen.blit(Selectbutton, clickselectp2.rect)
        screen.blit(current_imagep1, char_rectp1)
        screen.blit(current_imagep2, char_rectp2)
        pygame.display.update()
        pygame.time.Clock().tick(60)

def settings_clicked():
    characterselectionbar = pygame.image.load("characterselectionbar.png").convert_alpha()
    characterselectionbar = pygame.transform.scale(characterselectionbar, (950, 500))

    maptitle = pygame.image.load("Mapstitle.png").convert_alpha()
    maptitle = pygame.transform.scale(maptitle, (300, 80))

    map1image = pygame.image.load("map1image.png").convert_alpha()
    map1image = pygame.transform.scale(map1image, (800, 400))

    map2image = pygame.image.load("Map2image.png").convert_alpha()
    map2image = pygame.transform.scale(map2image, (800, 400))
    
    clickleft = Chara("Left", Leftbutton, (125, 450))
    clickright = Chara("Right", Rightbutton, (375, 450))
    clickselect = Chara("Select", Selectbutton, (250, 450))

    current_map = "Greenery"

    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if clickback.rect.collidepoint(event.pos):
                    clickSound.play()
                    return 0
                if clickleft.rect.collidepoint(event.pos):
                    clickSound.play()
                    if current_map == "Greenery":
                        current_map = "Dessert"
                    elif current_map == "Dessert":
                        current_map = "Greenery"
                if clickright.rect.collidepoint(event.pos):
                    clickSound.play()
                    if current_map == "Greenery":
                        current_map = "Dessert"
                    elif current_map == "Dessert":
                        current_map = "Greenery"
                if clickselect.rect.collidepoint(event.pos):
                    clickSound.play()
                    return current_map

        screen.blit(mainmenu_background, (0,0))
        screen.blit(characterselectionbar, (30,20))
        screen.blit(Leftbutton, clickleft.rect)
        screen.blit(Rightbutton, clickright.rect)
        screen.blit(Selectbutton, clickselect.rect)
        screen.blit(backbutton, clickback.rect)
        pygame.display.update()
        pygame.time.Clock().tick(60)
