import pygame
import pytmx
from pytmx.util_pygame import load_pygame

pygame.init()

screen = pygame.display.set_mode((1000, 800))

map_background = pygame.image.load("map1.png").convert_alpha()
map_background = pygame.transform.scale(map_background, (1000,800))

tiled_map = load_pygame("Map1updated.tmx")

map_width = tiled_map.width * tiled_map.tilewidth
map_height = tiled_map.height * tiled_map.tileheight

background = pygame.Surface((map_width, map_height)).convert_alpha()

map_background = pygame.transform.scale(map_background, (map_width, map_height))

wall = []

object_layer = tiled_map.get_layer_by_name("groundcollision")

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


background.blit(map_background, (0, 0))
draw_image_layers()


def draw_map(screen):
    screen.blit(background, (0, 0))
