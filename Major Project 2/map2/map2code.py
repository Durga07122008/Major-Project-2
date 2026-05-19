import pygame
import pytmx
from pytmx.util_pygame import load_pygame


pygame.init()


screen = pygame.display.set_mode((1000, 800))
map2_background = pygame.image.load('map2.webp').convert_alpha()
clock = pygame.time.Clock()

tiled_map = load_pygame("map2.tmx")
map_width = tiled_map.width * tiled_map.tilewidth
map_height = tiled_map.height * tiled_map.tileheight
background = pygame.Surface((map_width, map_height)).convert_alpha()
map2_background = pygame.transform.scale(map2_background, (map_width, map_height))

gravity_vector = pygame.math.Vector2(0, 0.5)
jump_vector = pygame.math.Vector2(0, -10)

character = pygame.image.load("pixilart-drawing.png").convert_alpha()
character = pygame.transform.scale(character, (32, 32))
char_rect = character.get_rect(center=(400, 150))

v = pygame.math.Vector2(0, 0)
lim = 0

wall = []
object_layer = tiled_map.get_layer_by_name("Ground")
for obj in object_layer:
    wall.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

def draw_image_layers():
    for layer in tiled_map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile_image = tiled_map.get_tile_image_by_gid(gid)
                if tile_image:
                    pixel_x = x * tiled_map.tilewidth
                    pixel_y = y * tiled_map.tileheight
                    background.blit(tile_image, (pixel_x, pixel_y))
background.blit(map2_background, (0, 0))
draw_image_layers()

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
                if lim < 2:
                    v += jump_vector
                    lim += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                v += pygame.math.Vector2(5, 0)
            elif event.key == pygame.K_d:
                v += pygame.math.Vector2(-5, 0)
        

    v.y += gravity_vector.y

    char_rect.x += v.x
    for block in wall:
        if char_rect.colliderect(block):
            if v.x > 0:  
                char_rect.right = block.left
            elif v.x < 0:  
                char_rect.left = block.right

    char_rect.y += v.y
    for block in wall:
        if char_rect.colliderect(block):
            if v.y > 0:
                char_rect.bottom = block.top
                v.y = 0
            elif v.y < 0:
                char_rect.top = block.bottom
                v.y = 0
                lim = 0

    if char_rect.top > 800:
        char_rect.topleft = (400, 150)
        v = pygame.math.Vector2(0, 0)

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(character, char_rect)
    pygame.display.update()
    clock.tick(60)