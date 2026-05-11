import pygame
import csv
import os




class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))




class Tilemap:
    def __init__(self, filename):
        self.tile_size = 32
        self.start_x = 100
        self.start_y = 100
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()


    def draw_map(self, surface):
        surface.blit(self.map_surface, (0, 0))


    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)


    def read_csv(self, filename):
        game_map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                game_map.append(list(row))
        return game_map


    def load_tiles(self, filename):
        tiles = []
        game_map = self.read_csv(filename)
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
                if tile == '0':
                    tiles.append(Tile("Grassblock.png",x * self.tile_size,y * self.tile_size))
                elif tile == '1':
                    tiles.append(Tile("Grassdirtblock.png", x * self.tile_size, y * self.tile_size))
                    x += 1
            y += 1
        self.map_w = x * self.tile_size
        self.map_h = y * self.tile_size
        return tiles