import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

gravity_vector = pygame.math.Vector2(0, 0.5)
jump_vector = pygame.math.Vector2(0, -10)

character = pygame.image.load("pixilart-drawing.png").convert_alpha()
character = pygame.transform.scale(character, (100, 100))
char_rect = character.get_rect(center=(400, 150))

v = pygame.math.Vector2(0, 0)
lim = 0
timer = clock.tick(60) / 1000.00
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                v += pygame.math.Vector2(-5, 0)
            elif event.key == pygame.K_d:
                v += pygame.math.Vector2(5, 0)
            elif event.key == pygame.K_w:
                if lim < 1:
                    v += jump_vector
                    lim += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                v += pygame.math.Vector2(5, 0)
            elif event.key == pygame.K_d:
                v += pygame.math.Vector2(-5, 0)

    if char_rect.bottom >= 800:
        lim = 0
    v += gravity_vector
    char_rect.move_ip(v)

    if char_rect.bottom >= 800:
        char_rect.bottom = 800
        if v.y > 0:
            v -= pygame.math.Vector2(0, v.y)


    screen.fill((0, 0, 0))
    screen.blit(character, char_rect)

    pygame.display.update()
    clock.tick(60)