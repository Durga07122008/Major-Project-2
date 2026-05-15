import pygame

def get_animation_dictionary(sheet_path, scale_size):
    sheet = pygame.image.load(sheet_path).convert_alpha()
    
    rows = 4
    cols = 10
    frame_width = sheet.get_width() // cols
    frame_height = sheet.get_height() // rows
    
    directions = ["left", "up", "right"]
    animations = {dir: [] for dir in directions}
    
    for r in range(rows):
        for c in range(cols):
            rect = pygame.Rect(c * frame_width, r * frame_height, frame_width, frame_height)
            frame = pygame.Surface(rect.size, pygame.SRCALPHA)
            frame.blit(sheet, (0, 0), rect)
            frame = pygame.transform.scale(frame, scale_size)
            animations[directions[r]].append(frame)
    return animations

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

player_animations = get_animation_dictionary("character.png", (64, 64))

velocity = pygame.math.Vector2(0,0)

class Soldier(pygame.sprite.Sprite):
    def __init__(self, animations, spawning_location):
        super().__init__()
        self.animations = animations
        self.current_direction = "down"
        self.current_frame = 0
        self.animation_speed = 0.2  
        self.image = self.animations[self.current_direction][0]
        self.hp = 100
        self.damage = 20
        self.rect = self.image.get_rect(center=spawning_location)

    def update(self):
        self.rect.move_ip(velocity)
        if velocity.y > 0:
            self.current_direction = "down"
        elif velocity.y < 0:
            self.current_direction = "up"
        elif velocity.x > 0: 
            self.current_direction = "right"
        elif velocity.x < 0:
            self.current_direction = "left"

        if velocity.length() > 0:
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.animations[self.current_direction]):
                self.current_frame = 0
            self.image = self.animations[self.current_direction][int(self.current_frame)]
        else:
            self.image = self.animations[self.current_direction][0]