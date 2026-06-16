import pygame
import Gunsinven as Gunsinven
import map2codeupdated as map2codeupdated 
import random


pygame.init()

def start_gamemap2():

    Screen1 = pygame.display.set_mode((1000, 800))
    Game_Active = True

    player1 = pygame.image.load("player.png").convert_alpha()
    player1 = pygame.transform.scale(player1, (50, 50))
    player2 = pygame.image.load("player1.png").convert_alpha()
    player2 = pygame.transform.scale(player2, (50, 50))

    gravity_vector = pygame.math.Vector2(0, 0.5)
    jump_vector = pygame.math.Vector2(0, -15)

    DROP_EVENT_DROP = pygame.USEREVENT + 1
    pygame.time.set_timer(DROP_EVENT_DROP, 5000)

    DROP_EVENT_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(DROP_EVENT_SPEED, random.randint(5000, 10000))


    class Bullet(pygame.sprite.Sprite):
        def __init__(self, spawn_location, direction, gun_object):
            super().__init__()

            self.image_full = pygame.image.load("bullet.png").convert_alpha()
            self.image = pygame.transform.scale(self.image_full, (60, 10))

            self.rect = self.image.get_rect(center=spawn_location)

            self.direction = direction

            self.speed = gun_object.bullet_speed
            self.push_back = gun_object.push_back

        def update(self):
            self.rect.move_ip(self.direction * self.speed)

            if self.rect.top < 0 or self.rect.left < 0 or self.rect.right > 1000 or self.rect.bottom > 800:
                self.kill()


    class Drop(pygame.sprite.Sprite):
        def __init__(self, gun_inside):
            super().__init__()

            self.image = pygame.image.load("drop.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (50, 50))

            self.rect = self.image.get_rect(center=(random.randint(100, 900), 0))

            self.v = pygame.math.Vector2(0, 0)

            self.gun_inside = gun_inside

            self.spawn_time = pygame.time.get_ticks()

        def update(self):
            self.v += gravity_vector

            self.rect.y += self.v.y

            for block in map2codeupdated.wall:

                if self.rect.colliderect(block):

                    if self.v.y > 0:
                        self.rect.bottom = block.top
                        self.v.y = 0

            if pygame.time.get_ticks() - self.spawn_time > 5000:
                self.kill()

    class Speed(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()

            self.image = pygame.image.load("speed.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (50, 50))

            self.rect = self.image.get_rect(center=(random.randint(100, 900), 0))

            self.v = pygame.math.Vector2(0, 0)

            self.spawn_time = pygame.time.get_ticks()

        def update(self):
            self.v += gravity_vector

            self.rect.y += self.v.y

            for block in map2codeupdated.wall:

                if self.rect.colliderect(block):

                    if self.v.y > 0:
                        self.rect.bottom = block.top
                        self.v.y = 0

            if pygame.time.get_ticks() - self.spawn_time > 5000:
                self.kill()


    bullet_group = pygame.sprite.Group()
    drop_group = pygame.sprite.Group()
    Speed_Group = pygame.sprite.Group()

    class Characters(pygame.sprite.Sprite):
        def __init__(self, name, image, location, gun, gun_dictionary):
            super().__init__()

            self.name = name
            self.base_image = image
            self.image = image
            self.rect = image.get_rect(center=location)
            self.gun_dictionary = gun_dictionary
            self.location = location
            self.v = pygame.math.Vector2(0, 0)
            self.move_speed = 5
            self.speed_boost_timer = 0
            self.starting_gun = gun
            self.gun = gun
            self.gun_object = self.gun_dictionary[self.gun]
            self.ammo = self.gun_object.ammo
            self.Turn = "right"

        def update(self):
            if self.speed_boost_timer > 0:
                self.speed_boost_timer -= 1

            if self.Turn == "left":
                self.image = pygame.transform.flip(self.base_image, True, False)
            else:
                self.image = self.base_image

            if self.Turn == "right":
                self.gun_object.rect.midleft = self.rect.midright
            elif self.Turn == "left":
                self.gun_object.rect.midright = self.rect.midleft

            if self.Turn == "right":
                self.gun_object.rect.midleft = self.rect.midright
            elif self.Turn == "left":
                self.gun_object.rect.midright = self.rect.midleft

        def draw_gun(self, screen):
            if self.Turn == "left":
                flipped_gun = pygame.transform.flip(self.gun_object.image, True, False)
                screen.blit(flipped_gun, self.gun_object.rect)
            else:
                screen.blit(self.gun_object.image, self.gun_object.rect)

        def change_gun(self, new_gun):

            self.gun = new_gun

            self.gun_object = self.gun_dictionary[self.gun]

            self.ammo = self.gun_object.ammo

        def return_starting_gun(self):

            self.gun = self.starting_gun

            self.gun_object = self.gun_dictionary[self.gun]

            self.ammo = self.gun_object.ammo

        def fire(self, bullet_group):

            if self.ammo <= 0:
                self.return_starting_gun()

            if self.Turn == "right":

                spawn_location = self.gun_object.rect.midright

                direction = pygame.math.Vector2(1, 0)

            elif self.Turn == "left":

                spawn_location = self.gun_object.rect.midleft

                direction = pygame.math.Vector2(-1, 0)

            bullet_group.add(Bullet(spawn_location, direction, self.gun_object))

            self.ammo -= 1

            if self.ammo <= 0 and self.gun != self.starting_gun:
                self.return_starting_gun()


    P1 = Characters("PLAYER 1", player1, (300, 200), "Classic", Gunsinven.Guns_Dictionary1)
    P2 = Characters("PLAYER 2", player2, (500, 200), "Classic", Gunsinven.Guns_Dictionary2)

    Character_Group = pygame.sprite.Group()

    Character_Group.add(P1)
    Character_Group.add(P2)

    Player_Direction1 = 0
    Player_Direction2 = 0

    P2lim = 0
    P1lim = 0
    timer = 0


    clock = pygame.time.Clock()

    while Game_Active:
        timer += 1 / 60 
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Game_Active = False
                return 0

            elif event.type == DROP_EVENT_DROP:

                gun_list = list(P1.gun_dictionary.keys())

                if P1.starting_gun in gun_list:
                    gun_list.remove(P1.starting_gun)

                random_gun = random.choice(gun_list)

                drop_group.empty()

                drop_group.add(Drop(random_gun))

                Speed_Group.add(Speed())

            elif event.type == pygame.KEYDOWN:

                keys = pygame.key.get_pressed()
                p1_current_speed = P1.move_speed * 2 if P1.speed_boost_timer > 0 else P1.move_speed
                p2_current_speed = P2.move_speed * 2 if P2.speed_boost_timer > 0 else P2.move_speed

                P1.v.x = 0
                if keys[pygame.K_a]:
                    P1.v.x = -p1_current_speed
                    P1.Turn = "left"
                if keys[pygame.K_d]:
                    P1.v.x = p1_current_speed
                    P1.Turn = "right"

                P2.v.x = 0
                if keys[pygame.K_LEFT]:
                    P2.v.x = -p2_current_speed
                    P2.Turn = "left"
                if keys[pygame.K_RIGHT]:
                    P2.v.x = p2_current_speed
                    P2.Turn = "right"
                
                if keys[pygame.K_w]:
                    if P1lim < 2:
                        P1.v.y = jump_vector.y
                        P1lim += 1
                elif keys[pygame.K_UP]:
                    if P2lim < 2:
                        P2.v.y = jump_vector.y
                        P2lim += 1

                elif event.key == pygame.K_SPACE:
                    P1.fire(bullet_group)

                elif event.key == pygame.K_RCTRL:
                    P2.fire(bullet_group)

            elif event.type == pygame.KEYUP:
                
                if event.key == pygame.K_a:
                    P1.v.x = 0

                elif event.key == pygame.K_d:
                    P1.v.x = 0

                elif event.key == pygame.K_LEFT:
                    P2.v.x = 0 

                elif event.key == pygame.K_RIGHT:
                    P2.v.x = 0

        P1.v.y += gravity_vector.y

        P1.rect.x += P1.v.x

        for block in map2codeupdated.wall:

            if P1.rect.colliderect(block):

                if P1.v.x > 0:
                    P1.rect.right = block.left

                elif P1.v.x < 0:
                    P1.rect.left = block.right

        P1.rect.y += P1.v.y

        for block in map2codeupdated.wall:

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

        for block in map2codeupdated.wall:

            if P2.rect.colliderect(block):

                if P2.v.x > 0:
                    P2.rect.right = block.left

                elif P2.v.x < 0:
                    P2.rect.left = block.right

        P2.rect.y += P2.v.y

        for block in map2codeupdated.wall:

            if P2.rect.colliderect(block):

                if P2.v.y > 0:
                    P2.rect.bottom = block.top
                    P2.v.y = 0
                    P2lim = 0

                elif P2.v.y < 0:
                    P2.rect.top = block.bottom
                    P2.v.y = 0

        if P1.rect.top > 800:
            P1.rect.center = (300, -500)
            P1.v = pygame.math.Vector2(0, 0)
            P1.return_starting_gun()

        if P2.rect.top > 800:
            P2.rect.center = (500, -500)
            P2.v = pygame.math.Vector2(0, 0)
            P2.return_starting_gun()

        for drop in drop_group:

            if P1.rect.colliderect(drop.rect):

                P1.change_gun(drop.gun_inside)

                drop.kill()

            elif P2.rect.colliderect(drop.rect):

                P2.change_gun(drop.gun_inside)

                drop.kill()
        
        for speed in Speed_Group:
            if P1.rect.colliderect(speed.rect):
                P1.speed_boost_timer = 300
                speed.kill()

            elif P2.rect.colliderect(speed.rect):
                P2.speed_boost_timer = 300
                speed.kill()

        map2codeupdated.draw_map(Screen1)

        bullet_group.update()
        
        Character_Group.update()

        drop_group.update()

        Speed_Group.update()

        Character_Group.draw(Screen1)

        for character in Character_Group:
            character.draw_gun(Screen1)

        bullet_group.draw(Screen1)

        Speed_Group.draw(Screen1)

        drop_group.draw(Screen1)

        for bullet in bullet_group:

            if P1.rect.colliderect(bullet.rect):

                P1.rect.move_ip(bullet.direction * bullet.push_back)

                bullet.kill()

            if P2.rect.colliderect(bullet.rect):

                P2.rect.move_ip(bullet.direction * bullet.push_back)

                bullet.kill()

        pygame.display.update()

    pygame.time.Clock().tick(60)