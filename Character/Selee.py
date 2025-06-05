# import os.path
# import time
# from PIL import Image
# import pygame
# from pygame import SurfaceType
# import GlobalVar
#
#
# class Selee:
#
#     def __init__(self,x,y,map,player):
#         #
#         self.player = player
#         self.map = map
#         self.speed = GlobalVar.screen_width*0.001
#         self.jumpPower = GlobalVar.screen_height * 0.1
#         self.jumpPowerEach = GlobalVar.screen_height * 0.02
#         self.health=100
#         self.damage=1
#         self.x=float(x)
#         self.y=float(y)
#         self.gravity  = GlobalVar.screen_height * 0.01
#         #图片们
#         self.attackLeft= pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_attack_left.png")),(GlobalVar.screen_width*0.2,GlobalVar.screen_height*0.35))
#         self.attackRight= pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_attack_right.png")),(GlobalVar.screen_width*0.2,GlobalVar.screen_height*0.35))
#         self.getAttackLeft=pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_get_attack_left.png")),(GlobalVar.screen_width*0.2,GlobalVar.screen_height*0.35))
#         self.getAttackRight = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_get_attack_right.png")),(GlobalVar.screen_width*0.2,GlobalVar.screen_height*0.35))
#         self.moveLeft =  pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_left.png")),(GlobalVar.screen_width*0.2,GlobalVar.screen_height*0.35))
#         self.moveRight = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_right.png")),(GlobalVar.screen_width*0.2,GlobalVar.screen_height*0.35))
#         print(GlobalVar.screen_width)
#         print(GlobalVar.screen_height)
#
#         self.abilityLeft = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_ability_left.png")),(GlobalVar.screen_width*0.2,GlobalVar.screen_height*0.35))
#         self.abilityRight = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_ability_right.png")),(GlobalVar.screen_width*0.2,GlobalVar.screen_height*0.35))
#         self.downAttack = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_combo_down_ability.png")),(GlobalVar.screen_width*0.05,GlobalVar.screen_height*0.05)) #bushi
#         #.upAttack = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_combo_down_ability.png")),(GlobalVar.screen_width*0.05,GlobalVar.screen_height*0.05)) #bushi
#         self.height=666 #bushi
#         self.width=666 #bushi
#         print("hong yun dang tou 666")
#         self.rect = pygame.Rect(x, y, 180,220)  #方框位置
#         self.avaRect=pygame.Rect(self.height,self.width,GlobalVar.screen_width*0.05, GlobalVar.screen_height*0.05)  #真实肉眼位置
#         #dependent variable
#         if self.player == "player2":
#             self.facing = "Left"
#         if self.player == "player1":
#             self.facing = "Right"
#         self.fall = False
#         self.rise = False
#         self.air = False
#
#
#
#     def move_right(self,opponent):
#         self.rect.x += self.speed
#         #if at the edge of map
#         if self.rect.colliderect(opponent.rect):
#             self.rect.x -= self.speed
#         if self.rect.x > int(GlobalVar.screen_width) - self.rect.width * 0.5:
#             print("is this happen")
#             self.rect.x = int(GlobalVar.screen_width) - self.rect.width * 0.5
#         print(self.rect.x)
#         print(int(GlobalVar.screen_width))
#         print(GlobalVar.screen_width)
#         self.map.blit(self.moveRight, self.rect)
#         self.facing="Right"
#
#     def move_left(self,opponent):
#         self.rect.x -= self.speed
#         #if at the edge of map
#         if self.rect.colliderect(opponent.rect):
#             self.rect.x += self.speed
#         if self.rect.x < 0 + self.rect.width * 0.5:
#             self.rect.x = 0 + self.rect.width * 0.5
#         self.map.blit(self.moveLeft, self.rect)
#         self.facing="Left"
#
#     def jump(self):
#         if not self.rise and not self.fall and not self.air:
#             self.rise = True
#
#     def falling(self):
#
#         self.rect.y += int(self.gravity)
#         if self.rect.y > self.y:
#             self.rect.y = int(self.y)
#             print("这里是不是没生效")
#         if self.facing == "Right":
#             self.map.blit(self.moveRight,self.rect)
#         elif self.facing == "Left":
#             self.map.blit(self.moveLeft,self.rect)
#         print([self.y, self.rect.y])
#         if self.rect.y == int(self.y):
#             self.fall = False
#
#     def rising(self):
#         self.rect.y -= self.jumpPowerEach
#         print(self.rect.y)
#         print(int(self.y - self.jumpPower))
#         print(self.jumpPowerEach)
#
#         if self.rect.y < int(self.y - self.jumpPower):
#             self.rect.y = int(self.y - self.jumpPower)
#         if self.facing == "Right":
#             self.map.blit(self.moveRight,self.rect)
#         if self.facing == "Left":
#             self.map.blit(self.moveLeft,self.rect)
#         if self.rect.y == int(self.y - self.jumpPower):
#             self.rise = False
#             self.air = True
#
#     def stay_air(self):
#         if self.facing == "Right":
#             self.map.blit(self.moveRight,self.rect)
#         if self.facing == "Left":
#             self.map.blit(self.moveLeft,self.rect)
#         self.air = False
#         self.fall = True
#
#     def defend(self):
#         pass
#
#     def stand(self):
#         if self.facing == "Left":
#             self.map.blit(self.moveLeft,self.rect)
#         if self.facing == "Right":
#             self.map.blit(self.moveRight,self.rect)
#
#
#     def get_damage(self,damage):
#         self.health -= damage
#
#     def attack(self,opobj):
#         #判定应该是个框而不是一个点  还没加判定只有动作
#         if self.facing == "Left":
#             self.map.blit(self.attackLeft,self.rect)
#         if self.facing == "Right":
#             self.map.blit(self.attackRight,self.rect)
#
#     def ability(self,playeropp):
#         if self.facing=="Left":
#             self.map.blit(self.abilityLeft,self.rect)
#             while(self.x + GlobalVar.screen_width*0.05 >self.abilityLeft.get_rect().x > 0):
#                 self.map.blit(self.abilityLeft,self.abilityLeft.get_rect())
#                 if(playeropp.rect.x - self.screen_width * 0.3 <= self.ability_x <= playeropp.rect.x + self.screen_width * 0.3):
#                     playeropp.get_damge(5)
#                 ability_sound = pygame.mixer.Sound(
#                     os.path.abspath("Character/CharacterSound/" + GlobalVar.selectedf1 + "_ability.mp3"))
#                 ability_sound.set_volume(GlobalVar.SoundEffect)
#                 ability_sound.play()
#         else:
#             self.map.blit(self.abilityRight,self.rect)
#             while(self.x - GlobalVar.screen_width*0.05 < self.abilityRight.get_rect().x < GlobalVar.screen_width):
#                 self.map.blit(self.abilityRight,self.abilityRight.get_rect())
#
#     def up_attack(self):
#         pass
#
#     def down_attack(self):
#         pass
#
#     def ult(self):
#         pass
#
#     def health_bar(self):
#         y = GlobalVar.screen_height * 0.08
#         if self.player == "player1":
#             x = GlobalVar.screen_width * 0.05
#         else:
#             x = GlobalVar.screen_width * 0.6
#
#         bar_width = GlobalVar.screen_width * 0.35  # Fixed width of the health bar
#         bar_height = GlobalVar.screen_height * 0.03  # Height of the health bar
#
#         # Draw the white frame (border)
#         frame_rect = pygame.Rect(x, y, bar_width, bar_height)
#         pygame.draw.rect(self.map, GlobalVar.WHITE, frame_rect, 2)  # Draw white border with thickness 2
#
#         # Draw the red health bar
#         health = bar_width * (self.health / 100)
#         health_rect = pygame.Rect(x, y, health, bar_height)
#         pygame.draw.rect(self.map, GlobalVar.RED, health_rect)

















import os.path
import time
from PIL import Image
import pygame
from pygame import SurfaceType
import GlobalVar


class Selee:

    def __init__(self,x,y,map,player):
        #
        self.player = player
        self.map = map
        self.speed = GlobalVar.screen_width*0.01
        self.jumpPower = GlobalVar.screen_height * 0.1
        self.jumpPowerEach = GlobalVar.screen_height * 0.018939392
        self.health=100
        self.damage=5
        self.gravity  = GlobalVar.screen_height * 0.001262628
        #图片们
        self.attackLeft= pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_attack_left.png")),(GlobalVar.screen_width*0.13,GlobalVar.screen_height*0.2))
        self.attackRight= pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_attack_right.png")),(GlobalVar.screen_width*0.13,GlobalVar.screen_height*0.2))
        self.getAttackLeft=pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_get_attack_left.png")),(GlobalVar.screen_width*0.13,GlobalVar.screen_height*0.2))
        self.getAttackRight = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_get_attack_right.png")),(GlobalVar.screen_width*0.13,GlobalVar.screen_height*0.2))
        self.moveLeft =  pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_left.png")),(GlobalVar.screen_width*0.13,GlobalVar.screen_height*0.2))
        self.moveRight = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_right.png")),(GlobalVar.screen_width*0.13,GlobalVar.screen_height*0.2))
        self.abilityLeft = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_ability_left.png")),(GlobalVar.screen_width*0.18,GlobalVar.screen_height*0.09))
        self.abilityRight = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_ability_right.png")),(GlobalVar.screen_width*0.18,GlobalVar.screen_height*0.09))
        self.downAttack = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_combo_down_ability.png")),(GlobalVar.screen_width*0.15,GlobalVar.screen_height)) #bushi
        self.upAttack = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Selee_combo_up_attack.png")),(GlobalVar.screen_width*0.08,GlobalVar.screen_height*0.3)) #bushi
        #music
        #print(y)        #dependent variable
        self.rect = self.rect = self.moveRight.get_rect(topleft=(x, y))
        self.bottom =self.rect.bottom

        if self.player == "player2":
            self.facing = "Left"
        if self.player == "player1":
            self.facing = "Right"
        #jump
        self.vel_y = 0
        self.jump = False
        #attack
        self.attack = False
        self.attack_stage = "end"
        #ability
        self.ability_use = False
        self.ability_now = self.rect
        self.ability_face = self.facing
        #down attack
        self.downattacking = False
        self.thunder_rect = None
        #up attack
        self.upattacking = False
        self.upAttack_stage = "end"
        self.training = False
        self.get_damages = False
    def move(self,opponent):
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        if self.attack == False and not self.ability_use and not self.downattacking and self.training == False:
            if keys[GlobalVar.keys[self.player]["move_right"]]:
                #ability_sound = pygame.mixer.Sound(
                   # os.path.abspath("Character/CharacterSound/Walk.mp3"))
             #   ability_sound.set_volume(GlobalVar.SoundEffect)
               # ability_sound.play()
                if abs(self.rect.right - opponent.rect.left)> self.speed or self.rect.bottom > self.bottom:
                    dx = self.speed
                elif opponent.rect.left-self.rect.right < self.speed:
                    dx = self.rect.right-opponent.rect.left
                self.facing = "Right"

            if keys[GlobalVar.keys[self.player]["move_left"]]:
               # ability_sound = pygame.mixer.Sound(
                #    os.path.abspath("Character/CharacterSound/Walk.mp3"))
               # ability_sound.set_volume(GlobalVar.SoundEffect)
               # ability_sound.play()
                if abs(opponent.rect.right-self.rect.left) > self.speed or self.rect.bottom > self.bottom:
                    dx -= self.speed
                elif opponent.rect.right-self.rect.left > self.speed:
                    dx = opponent.rect.right-self.rect.left
                self.facing = "Left"

            if keys[GlobalVar.keys[self.player]["jump"]] and keys[GlobalVar.keys[self.player]["attack"]]:
                self.upattacking = True
                self.upAttack_stage = "start"
            if keys[GlobalVar.keys[self.player]["defend"]] and keys[GlobalVar.keys[self.player]["attack"]]:
                self.downattacking = True
                thunder_width = self.downAttack.get_rect().width
                thunder_height = self.downAttack.get_rect().height
                self.thunder_rect = pygame.Rect(self.rect.centerx - thunder_width // 2, 0-thunder_height, thunder_width,
                                                thunder_height)

            if keys[GlobalVar.keys[self.player]["jump"]] and not self.jump and not self.upattacking and not self.downattacking:

                self.jump = True
                self.vel_y = -self.jumpPowerEach

            if keys[GlobalVar.keys[self.player]["attack"]] and not self.upattacking and not self.downattacking:

                self.attack = True
                self.attack_stage = "start"

            if keys[GlobalVar.keys[self.player]["ability"]]:

                self.ability_use = True
                self.ability_face = self.facing
                if self.ability_face == "Right":
                    self.ability_now = pygame.Rect(self.rect.right,self.rect.centery - self.rect.width * 0.25,self.abilityRight.get_rect().width,self.abilityRight.get_rect().height)
                elif self.ability_face == "Left":
                    self.ability_now = pygame.Rect(self.rect.left,self.rect.centery - self.rect.width * 0.25,self.abilityRight.get_rect().width,self.abilityLeft.get_rect().height)

        if (self.attack == False) and self.get_damages == False:
            if self.facing == "Right":
                self.map.blit(self.moveRight, self.rect)
            if self.facing == "Left":
                self.map.blit(self.moveLeft, self.rect)
        if self.get_damages == True:
            if (self.facing == "Right"):
                self.map.blit(self.getAttackRight, self.rect)
            if (self.facing == "Left"):
                self.map.blit(self.getAttackLeft, self.rect)
            self.get_damages = False

        self.vel_y += self.gravity
        dy += self.vel_y

        #bian jie
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > GlobalVar.screen_width:
            dx = GlobalVar.screen_width - self.rect.right

        if self.rect.bottom + dy >= self.bottom:
            self.vel_y = 0
            dy = self.bottom - self.rect.bottom
            self.jump = False

        self.rect.x += dx
        self.rect.y += dy

        if self.ability_use == True:
            self.ability(opponent)
        if self.attack == True:
            self.attacking(opponent)
        if self.downattacking == True:
            self.down_attack(opponent)
        if self.upattacking == True:
            self.up_attack(opponent)

    def get_damage(self,damage):
       # ability_sound = pygame.mixer.Sound(
         #   os.path.abspath("Character/CharacterSound/Damaged_Sound.mp3"))
       # ability_sound.set_volume(GlobalVar.SoundEffect)
      #  ability_sound.play()
        self.health -= damage
        self.get_damages = True


    def attacking(self,opponent):


        if(self.attack_stage == "start"):
           # ability_sound = pygame.mixer.Sound(
            #    os.path.abspath("Character/CharacterSound/Punch.mp3"))
          #  ability_sound.set_volume(GlobalVar.SoundEffect)
          #  ability_sound.play()
            attack_rect_right = pygame.Rect(self.rect.x,self.rect.y,1.3 * self.rect.width,self.rect.height)
            attack_rect_left = pygame.Rect(self.rect.x - 1.3 * self.rect.width,self.rect.y,(1.3 * self.rect.width),self.rect.height)

            #判定应该是个框而不是一个点  还没加判定只有动作
            if self.facing == "Left":
                self.map.blit(self.attackLeft,self.rect)
                if attack_rect_left.colliderect(opponent.rect):
                    opponent.get_damage(self.damage)

            if self.facing == "Right":
                self.map.blit(self.attackRight,self.rect)
                if attack_rect_right.colliderect(opponent.rect):
                    opponent.get_damage(self.damage)
            self.attack_stage = "end"

        elif(self.attack_stage == "end"):
            if self.facing == "Left":
                self.map.blit(self.moveLeft, self.rect)
            if self.facing == "Right":
                self.map.blit(self.moveRight, self.rect)
            self.attack = False

    def ability(self,opponent):

        ability_speed = GlobalVar.screen_width * 0.01
       # ability_sound = pygame.mixer.Sound(
           # os.path.abspath("Character/CharacterSound/Selee_ability.mp3"))
     #   ability_sound.set_volume(GlobalVar.SoundEffect)
      #  ability_sound.play()
        if self.ability_face == "Right":
            if(self.ability_now.colliderect(opponent.rect)):
                opponent.get_damage(self.damage)
            if(self.ability_now.left + ability_speed >= GlobalVar.screen_width):
                ability_speed = GlobalVar.screen_width - self.ability_now.right
                self.ability_use = False
            self.map.blit(self.abilityRight,self.ability_now)
            # self.map.blit(self.moveRight,self.rect)
            self.ability_now.x += ability_speed
        if self.ability_face == "Left":
            self.map.blit(self.abilityLeft,self.ability_now)
            if(self.ability_now.colliderect(opponent.rect)):
                opponent.get_damage(self.damage)
            if(self.ability_now.right - ability_speed <= 0):
                ability_speed = GlobalVar.screen_width - self.ability_now.left
                self.ability_use = False
            self.map.blit(self.abilityLeft,self.ability_now)
            # self.map.blit(self.moveLeft,self.rect)
            self.ability_now.x -= ability_speed


    def up_attack(self,opponent):

        if(self.upAttack_stage == "start"):
            cyclon_rect = pygame.Rect(self.rect.centerx - self.rect.width * 0.25,self.rect.top - self.upAttack.get_height(),self.upAttack.get_rect().width,self.upAttack.get_rect().height)
            pygame.draw.rect(self.map,(50,50,50),cyclon_rect)
            pygame.draw.rect(self.map,(50,50,50),self.rect)

            self.map.blit(self.upAttack,cyclon_rect)
            if(cyclon_rect.colliderect(opponent.rect)):
                opponent.get_damage(self.damage)
            self.upAttack_stage = "end"
        elif(self.upAttack_stage == "end"):
            if self.facing == "Left":
                self.map.blit(self.moveLeft, self.rect)
            if self.facing == "Right":
                self.map.blit(self.moveRight, self.rect)
            self.upattacking = False
    def down_attack(self,opponent):
        thunder_speed = GlobalVar.screen_height * 0.02
        self.thunder_rect.y += thunder_speed
        # Blit the downAttack image as thunder
        self.map.blit(self.downAttack, self.thunder_rect)

        # Check for collision with the opponent
        if self.thunder_rect.colliderect(opponent.rect):
            opponent.get_damage(10)  # Deal 10 damage
            self.downattacking = False  # End thunder

        # End thunder when it reaches the player's top
        if self.thunder_rect.bottom >= self.rect.top:
            self.downattacking = False

    def ult(self):
        pass

    def health_bar(self):
        y = GlobalVar.screen_height * 0.08
        if self.player == "player1":
            x = GlobalVar.screen_width * 0.05
        else:
            x = GlobalVar.screen_width * 0.6

        bar_width = GlobalVar.screen_width * 0.35  # Fixed width of the health bar
        bar_height = GlobalVar.screen_height * 0.03  # Height of the health bar

        # Draw the white frame (border)
        frame_rect = pygame.Rect(x, y, bar_width, bar_height)
        pygame.draw.rect(self.map, GlobalVar.WHITE, frame_rect, 2)  # Draw white border with thickness 2

        # Draw the red health bar
        health = bar_width * (self.health / 100)
        health_rect = pygame.Rect(x, y, health, bar_height)
        pygame.draw.rect(self.map, GlobalVar.RED, health_rect)

    def winround(self, map: SurfaceType):
        font = pygame.font.SysFont('Arial', 40)
        Winner = font.render("Winner", True, (255, 255, 255))
        rect = Winner.get_rect()
        rect.center = (map.get_size()[0] * 0.6, map.get_size()[1] * 0.04)
        return [Winner, rect]

