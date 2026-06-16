import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 400))
clock = pygame.time.Clock()

run_sheet = pygame.image.load('Pink_Monster_Run_6.png').convert_alpha()
idle_sheet = pygame.image.load('Pink_Monster_Idle_4.png').convert_alpha()
jump_sheet = pygame.image.load('Pink_Moster_Jump.png').convert_alpha()
fall_sheet = pygame.image.load('Pink_Monster_Fall.png').convert_alpha()


def load_frames(sheet, total_frames):
    frames = []
    sheet_w, sheet_h = sheet.get_size()
    frame_w = sheet_w // total_frames
    frame_h = sheet_h 
    for i in range(total_frames):
        x = i * frame_h
        y = 0
        img = sheet.subsurface(pygame.Rect(x, y, frame_w, frame_h))
        img = pygame.transform.scale(img, (100, 100))
        frames.append(img)
    return frames

animations = {
    'run': load_frames(run_sheet, total_frames=6),
    'idle': load_frames(idle_sheet, total_frames=4), 
    'jump': load_frames(jump_sheet, total_frames=3),
    'fall': load_frames(fall_sheet, total_frames=3)
}
current_state = 'idle'
flip_x = False

gravity = pygame.math.Vector2(0, 0.5)
jump_speed = -20
v = pygame.math.Vector2(0, 0)

char_rect = animations['idle'][0].get_rect(center=(400, 150))

frame_index = 0
frame_timer = 0
ani_speed = 5
lim = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        v.x = -6
        flip_x = True
    elif keys[pygame.K_d]:
        v.x = 6
        flip_x = False
    else:
        v.x = 0

    if keys[pygame.K_w] and char_rect.bottom >= 400:
        v.y += jump_speed
        lim += 1

    v.y += gravity.y
    char_rect.move_ip(v)

    if char_rect.bottom >= 400:
        char_rect.bottom = 400
        v.y = 0

    if char_rect.bottom < 400:
        if v.y < 0:
            new_state = 'jump'
        else:
            new_state = 'fall'
    else:
        if v.x != 0:
            new_state = 'run'
        else:
            new_state = 'idle'

    if new_state != current_state:
        current_state = new_state
        frame_index = 0
        frame_timer = 0

    current_animation_list = animations[current_state]
    frame_timer += 1
    if frame_timer >= ani_speed:
        frame_index = (frame_index + 1) % len(current_animation_list)
        frame_timer = 0

    current_image = current_animation_list[frame_index]
    if flip_x:
        current_image = pygame.transform.flip(current_image, True, False)

    screen.fill((30, 30, 30))
    screen.blit(current_image, char_rect)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()