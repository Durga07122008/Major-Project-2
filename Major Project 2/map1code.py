import pygame
import pytmx


pygame.init()


screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

tiled_map = pytmx.load_pygame("Map1.tmx", pixelalpha=True)

background = pygame.Surface((tiled_map.width * tiled_map.tilewidth, tiled_map.height * tiled_map.tileheight)).convert_alpha()

def draw_image_layers():
    for layer in tiled_map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile_image = tiled_map.get_tile_image_by_gid(gid)
                if tile_image:
                    pixel_x = x * tiled_map.tilewidth
                    pixel_y = y * tiled_map.tileheight
                    background.blit(tile_image, (pixel_x, pixel_y))
draw_image_layers()

game_active = True
while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    pygame.display.update()
    clock.tick(60)
pygame.quit()