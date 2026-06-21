import pygame

class Guns_Class:
    def __init__(self, image, name, type, push_back, bullet_speed, ammo):
        self.name = name
        self.rect = image.get_rect(center=(300, 200))
        self.image = image
        self.type = type
        self.push_back = push_back
        self.bullet_speed = bullet_speed
        self.ammo = ammo

pygame.init()
pygame.display.set_mode((1000, 800))


Kar98_surface1 = pygame.image.load("Kar98.png").convert_alpha()
Kar98_surface1 = pygame.transform.scale(Kar98_surface1, (80, 30))
Kar98_surface2 = pygame.image.load("Kar98.png").convert_alpha()
Kar98_surface2 = pygame.transform.scale(Kar98_surface2, (80, 30))

AWP_surface1 = pygame.image.load("AWP.png").convert_alpha()
AWP_surface1 = pygame.transform.scale(AWP_surface1, (80, 30))
AWP_surface2 = pygame.image.load("AWP.png").convert_alpha()
AWP_surface2 = pygame.transform.scale(AWP_surface2, (80, 30))

Operator_surface1 = pygame.image.load("Operator.png").convert_alpha()
Operator_surface1 = pygame.transform.scale(Operator_surface1, (80, 30))
Operator_surface2 = pygame.image.load("Operator.png").convert_alpha()
Operator_surface2 = pygame.transform.scale(Operator_surface2, (80, 30))

Bazooka_surface1 = pygame.image.load("Bazooka.jpg").convert_alpha()
Bazooka_surface1 = pygame.transform.scale(Bazooka_surface1, (80, 30))
Bazooka_surface2 = pygame.image.load("Bazooka.jpg").convert_alpha()
Bazooka_surface2 = pygame.transform.scale(Bazooka_surface2, (80, 30))

RPG_surface1 = pygame.image.load("RPG.png").convert_alpha()
RPG_surface1 = pygame.transform.scale(RPG_surface1, (80, 30))
RPG_surface2 = pygame.image.load("RPG.png").convert_alpha()
RPG_surface2 = pygame.transform.scale(RPG_surface2, (80, 30))

Classic_surface1 = pygame.image.load("Classic.png").convert_alpha()
Classic_surface1 = pygame.transform.scale(Classic_surface1, (80, 30))
Classic_surface2 = pygame.image.load("Classic.png").convert_alpha()
Classic_surface2 = pygame.transform.scale(Classic_surface2, (80, 30))


Kar98_1 = Guns_Class(Kar98_surface1, "Kar98", "Sniper", 150, 10, 5)
Kar98_2 = Guns_Class(Kar98_surface2, "Kar98", "Sniper", 150, 10, 5)

AWP_1 = Guns_Class(AWP_surface1, "AWP", "Sniper", 110, 20, 5)
AWP_2 = Guns_Class(AWP_surface2, "AWP", "Sniper", 110, 20, 5)

Operator_1 = Guns_Class(Operator_surface1, "Operator", "Sniper", 130, 15, 5)
Operator_2 = Guns_Class(Operator_surface2, "Operator", "Sniper", 130, 15, 5)

Bazooka_1 = Guns_Class(Bazooka_surface1, "Bazooka", "Explosion", 1000, 10, 1)
Bazooka_2 = Guns_Class(Bazooka_surface2, "Bazooka", "Explosion", 1000, 10, 1)

RPG_1 = Guns_Class(RPG_surface1, "RPG", "Explosion", 1000, 7, 2)
RPG_2 = Guns_Class(RPG_surface2, "RPG", "Explosion", 1000, 7, 2)

Classic_1 = Guns_Class(Classic_surface1, "Classic", "Hand Gun", 20, 25, 10**10000)
Classic_2 = Guns_Class(Classic_surface2, "Classic", "Hand Gun", 20, 25, 10**10000)


Guns_Dictionary1 = {}

Guns_Dictionary1["Kar98"] = Kar98_1
Guns_Dictionary1["AWP"] = AWP_1
Guns_Dictionary1["Operator"] = Operator_1
Guns_Dictionary1["Bazooka"] = Bazooka_1
Guns_Dictionary1["RPG"] = RPG_1
Guns_Dictionary1["Classic"] = Classic_1



Guns_Dictionary2 = {}

Guns_Dictionary2["Kar98"] = Kar98_2
Guns_Dictionary2["AWP"] = AWP_2
Guns_Dictionary2["Operator"] = Operator_2
Guns_Dictionary2["Bazooka"] = Bazooka_2
Guns_Dictionary2["RPG"] = RPG_2
Guns_Dictionary2["Classic"] = Classic_2