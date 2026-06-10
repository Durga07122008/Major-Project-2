import pygame
import Gunsinven
import map1code

pygame.init()

Screen1 = pygame.display.set_mode((1000, 800))
Game_Active = True

player = pygame.image.load("player.png").convert_alpha()
player = pygame.transform.scale(player, (50, 50))
player1 = pygame.image.load("player1.png").convert_alpha()
player1 = pygame.transform.scale(player1, (50, 50))

gravity_vector = pygame.math.Vector2(0, 0.5)
jump_vector = pygame.math.Vector2(0, -10)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, spawn_location, direction, gun):
        super().__init__()

        self.image_full = pygame.image.load("bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image_full, (60, 10))

        self.rect = self.image.get_rect(center=spawn_location)

        self.direction = direction

        self.speed = Gunsinven.Guns_Dictionary[gun].bullet_speed
        self.push_back = Gunsinven.Guns_Dictionary[gun].push_back

    def update(self):
        self.rect.move_ip(self.direction * self.speed)

        if self.rect.top < 0 or self.rect.left < 0 or self.rect.right > 1000 or self.rect.bottom > 800:
            self.kill()


bullet_group = pygame.sprite.Group()


class Characters(pygame.sprite.Sprite):
    def __init__(self, name, image, location, gun):
        super().__init__()

        self.name = name
        self.image = image

        self.rect = image.get_rect(center=location)

        self.location = location

        self.v = pygame.math.Vector2(0, 0)

        self.gun = gun

        self.Turn = "right"

        self.gun_object = Gunsinven.Guns_Dictionary[self.gun]

    def update(self):
        self.rect.move_ip(self.v)

        self.gun_object.rect.move_ip(self.v)

    def draw_gun(self, screen):
        screen.blit(self.gun_object.image, self.gun_object.rect)

    def fire(self, bullet_group):

        if self.Turn == "right":
            spawn_location = self.gun_object.rect.midright
            direction = pygame.math.Vector2(1, 0)

        elif self.Turn == "left":
            spawn_location = self.gun_object.rect.midleft
            direction = pygame.math.Vector2(-1, 0)

        bullet_group.add(Bullet(spawn_location, direction, self.gun))


P1 = Characters("PLAYER 1", player, (300, 200), "Kar98")
P2 = Characters("PLAYER 2", player1, (500, 200), "AWP")

Character_Group = pygame.sprite.Group()

Character_Group.add(P1)
Character_Group.add(P2)

Player_Direction1 = 0
Player_Direction2 = 0

P2lim = 0
P1lim = 0

clock = pygame.time.Clock()

while Game_Active:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            Game_Active = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:

                P1.v -= (5, 0)

                P1.Turn = "left"

                if Player_Direction1 == 0:
                    P1.image = pygame.transform.flip(P1.image, 1, 0)

                    P1.gun_object.image = pygame.transform.flip(P1.gun_object.image, 1, 0)

                    Player_Direction1 = 1

            elif event.key == pygame.K_d:

                P1.v += (5, 0)

                P1.Turn = "right"

                if Player_Direction1 == 1:
                    P1.image = pygame.transform.flip(P1.image, 1, 0)

                    P1.gun_object.image = pygame.transform.flip(P1.gun_object.image, 1, 0)

                    Player_Direction1 = 0

            elif event.key == pygame.K_w:

                if P1lim < 1:
                    P1.v += jump_vector
                    P1lim += 1

            elif event.key == pygame.K_LEFT:

                P2.v -= (5, 0)

                P2.Turn = "left"

                if Player_Direction2 == 1:
                    P2.image = pygame.transform.flip(P2.image, 1, 0)

                    P2.gun_object.image = pygame.transform.flip(P2.gun_object.image, 1, 0)

                    Player_Direction2 = 0

            elif event.key == pygame.K_RIGHT:

                P2.v += (5, 0)

                P2.Turn = "right"

                if Player_Direction2 == 0:
                    P2.image = pygame.transform.flip(P2.image, 1, 0)

                    P2.gun_object.image = pygame.transform.flip(P2.gun_object.image, 1, 0)

                    Player_Direction2 = 1

            elif event.key == pygame.K_UP:

                if P2lim < 1:
                    P2.v += jump_vector
                    P2lim += 1

            elif event.key == pygame.K_SPACE:
                P1.fire(bullet_group)

            elif event.key == pygame.K_RCTRL:
                P2.fire(bullet_group)

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                P1.v += (5, 0)

            elif event.key == pygame.K_d:
                P1.v -= (5, 0)

            elif event.key == pygame.K_LEFT:
                P2.v += (5, 0)

            elif event.key == pygame.K_RIGHT:
                P2.v -= (5, 0)

    P1.v.y += gravity_vector.y

    P1.rect.x += P1.v.x

    for block in map1code.wall:

        if P1.rect.colliderect(block):

            if P1.v.x > 0:
                P1.rect.right = block.left

            elif P1.v.x < 0:
                P1.rect.left = block.right

    P1.rect.y += P1.v.y

    for block in map1code.wall:

        if P1.rect.colliderect(block):

            if P1.v.y > 0:
                P1.rect.bottom = block.top
                P1.v.y = 0
                P1lim = 0

            elif P1.v.y < 0:
                P1.rect.top = block.bottom
                P1.v.y = 0

    P2.v.y += gravity_vector.y

    P2.rect.x += P2.v.x

    for block in map1code.wall:

        if P2.rect.colliderect(block):

            if P2.v.x > 0:
                P2.rect.right = block.left

            elif P2.v.x < 0:
                P2.rect.left = block.right

    P2.rect.y += P2.v.y

    for block in map1code.wall:

        if P2.rect.colliderect(block):

            if P2.v.y > 0:
                P2.rect.bottom = block.top
                P2.v.y = 0
                P2lim = 0

            elif P2.v.y < 0:
                P2.rect.top = block.bottom
                P2.v.y = 0

    map1code.draw_map(Screen1)

    bullet_group.update()

    Character_Group.draw(Screen1)

    for character in Character_Group:
        character.draw_gun(Screen1)

    bullet_group.draw(Screen1)

    for bullet in bullet_group:

        if P1.rect.colliderect(bullet.rect):
            P1.rect.move_ip(bullet.direction * bullet.push_back)

            bullet.kill()

        if P2.rect.colliderect(bullet.rect):
            P2.rect.move_ip(bullet.direction * bullet.push_back)

            bullet.kill()

    pygame.display.update()

    clock.tick(60)

pygame.quit()
