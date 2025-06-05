import os.path
import time
import pygame
from pygame import SurfaceType
import GlobalVar


class Iris:

    def __init__(self,x,y,map,player):
        #
        self.point = 0
        self.player = player
        self.map = map
        self.speed = GlobalVar.screen_width*0.01
        self.jumpPower = GlobalVar.screen_height * 0.08
        self.jumpPowerEach = GlobalVar.screen_height * 0.018939392
        self.health=100
        self.damage=1
        self.x=x
        self.y=y
        self.gravity  = GlobalVar.screen_height * 0.001262628
        #图片们
        self.attackLeft= pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Iris_slash_left.png")),(GlobalVar.screen_width*0.13,GlobalVar.screen_height*0.2))
        self.attackRight= pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Iris_slash_right.png")),(GlobalVar.screen_width*0.13,GlobalVar.screen_height*0.2))
        self.slashLeft = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Iris_attack_left.png")),(GlobalVar.screen_width*0.13,GlobalVar.screen_height*0.2))
        self.slashRight = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Iris_attack_right.png")),(GlobalVar.screen_width*0.13,GlobalVar.screen_height*0.2))

        self.getAttackLeft=pygame.transform.scale(pygame.image.load(os.path.abspath(
            "Character//CharacterImage//Iris_get_attack_left.png")), (GlobalVar.screen_width * 0.13, GlobalVar.screen_height * 0.2))
        self.getAttackRight = pygame.transform.scale(pygame.image.load(os.path.abspath(
           "Character//CharacterImage//Iris_get_attack_right.png")), (GlobalVar.screen_width * 0.13, GlobalVar.screen_height * 0.2))
        self.moveLeft =  pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Iris_left.png")),(GlobalVar.screen_width*0.13,GlobalVar.screen_height*0.2))
        self.moveRight = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Iris_right.png")),(GlobalVar.screen_width*0.13,GlobalVar.screen_height*0.2))
        self.abilityLeft = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Iris_ability_left.png")),(GlobalVar.screen_width * 0.2, GlobalVar.screen_height * 0.35))
        self.abilityRight = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Iris_ability_right.png")),(GlobalVar.screen_width * 0.2, GlobalVar.screen_height * 0.35))
        self.downAttack_left = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Iris_combo_down_attack_left.png")),(GlobalVar.screen_width*0.4,GlobalVar.screen_height*0.4))
        self.downAttack_right = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Iris_combo_down_attack_right.png")),(GlobalVar.screen_width*0.4,GlobalVar.screen_height*0.4))

        self.upAttack = pygame.transform.scale(pygame.image.load(os.path.abspath("Character//CharacterImage//Iris_combo_up_attack.png")),(GlobalVar.screen_width*0.3,GlobalVar.screen_height*0.4))
        self.height=666 #bushi
        self.width=666 #bushi
        self.rect = self.rect = self.moveRight.get_rect(topleft=(x, y))
        self.avaRect=pygame.Rect(self.height,self.width,GlobalVar.screen_width*0.05, GlobalVar.screen_height*0.05)  #真实肉眼位置
        #dependent variable
        self.bottom = self.rect.bottom
        if self.player == "player2":
            self.facing = "Left"
        if self.player == "player1":
            self.facing = "Right"
        self.vel_y = 0
        self.jump = False
        self.attack = False
        self.ability_use = False
        self.ability_now = 0
        self.ability_face = self.facing
        self.attack_stage = "end"

        #above are apply for all characters


        self.downattack_stage = "end"
        #up attack
        self.upattacking = False
        self.timeup = None
        #down attack
        self.downattacking = False
        self.field_rect_left = None
        self.field_rect_right = None
        self.time = None
        self.training = False
        self.get_damages = False

    def move(self, opponent):
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        #pygame.draw.rect(self.map,(0,0,0),self.rect)
        if self.attack == False and not self.ability_use and not self.downattacking and self.training == False:
            if keys[GlobalVar.keys[self.player]["move_right"]]:
                ability_sound = pygame.mixer.Sound(
                    os.path.abspath("Character/CharacterSound/Walk.mp3"))
                ability_sound.set_volume(GlobalVar.SoundEffect)
                ability_sound.play()
                if abs(self.rect.right - opponent.rect.left)  > self.speed or self.rect.bottom > self.bottom:
                    dx = self.speed
                elif (self.y == self.bottom) and opponent.rect.left - self.rect.right < self.speed:
                    dx = self.rect.right - opponent.rect.left
                self.facing = "Right"
            if keys[GlobalVar.keys[self.player]["move_left"]]:
                ability_sound = pygame.mixer.Sound(
                    os.path.abspath("Character/CharacterSound/Walk.mp3"))
                ability_sound.set_volume(GlobalVar.SoundEffect)
                ability_sound.play()
                if abs(opponent.rect.right - self.rect.left) > self.speed or self.rect.bottom > self.bottom:
                    dx -= self.speed
                elif (self.y == self.bottom) and opponent.rect.right - self.rect.left > self.speed:
                    dx = opponent.rect.right - self.rect.left
                self.facing = "Left"
                print(dx)
            if keys[GlobalVar.keys[self.player]["jump"]] and keys[GlobalVar.keys[self.player]["attack"]] and not self.upattacking and not self.downattacking:
                self.timeup = time.time()
                self.upattacking = True
                self.slash_rect_right = pygame.Rect(self.rect.right,self.y, self.upAttack.get_rect().width,self.upAttack.get_rect().height)
                self.slash_rect_left = pygame.Rect(self.rect.x-self.rect.left,self.y, self.upAttack.get_rect().width,self.upAttack.get_rect().height)
            if keys[GlobalVar.keys[self.player]["defend"]] and keys[GlobalVar.keys[self.player]["attack"]] and not self.downattacking and not self.upattacking:
                self.time  = time.time()
                self.downattacking = True
                self.field_rect_left = pygame.Rect(self.rect.x-self.rect.width*1.5,self.rect.top-self.rect.height*0.5, self.downAttack_left.get_rect().width,self.downAttack_left.get_rect().height)
                self.field_rect_right = pygame.Rect(self.rect.x-self.rect.width*0.55,self.rect.top-self.rect.height*0.5, self.downAttack_right.get_rect().width,self.downAttack_right.get_rect().height)

            if keys[GlobalVar.keys[self.player]["jump"]] and not self.jump and not self.upattacking:
                self.jump = True
                self.vel_y = -self.jumpPowerEach

            if keys[GlobalVar.keys[self.player]["attack"]] and not self.upattacking and not self.downattacking:
                self.attack = True
                self.attack_stage = "start"
            if keys[GlobalVar.keys[self.player]["ability"]]:
                ability_sound = pygame.mixer.Sound(
                    os.path.abspath("Character/CharacterSound/flower.mp3"))
                ability_sound.set_volume(GlobalVar.SoundEffect)
                ability_sound.play()
                self.ability_use = True
                self.ability_face = self.facing
                if self.ability_face == "Right":
                    self.ability_now = pygame.Rect(self.rect.right, self.rect.y, self.abilityRight.get_rect().width,
                                                   self.attackRight.get_rect().height)
                elif self.ability_face == "Left":
                    self.ability_now = pygame.Rect(self.rect.left, self.rect.y, self.abilityRight.get_rect().width,
                                                   self.attackRight.get_rect().height)

        if (self.attack == False and self.upattacking == False) and self.get_damages == False:
            if self.facing == "Right":
                #pygame.draw.rect(self.map,(0,0,0),self.rect)
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

        # bian jie
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
        if self.downattacking==True:
            self.down_attack(opponent)
        if self.upattacking == True:
            self.up_attack(opponent)

    def get_damage(self, damage):
        self.health -= damage
        ability_sound = pygame.mixer.Sound(
            os.path.abspath("Character/CharacterSound/Damaged_Sound.mp3"))
        ability_sound.set_volume(GlobalVar.SoundEffect)
        ability_sound.play()
        self.health -= damage
        self.get_damages = True

    def attacking(self, opponent):

        if (self.attack_stage == "start"):
            attack_rect_right = pygame.Rect(self.rect.x, self.rect.y, 1.3 * self.rect.width, self.rect.height)
            attack_rect_left = pygame.Rect(self.rect.x - 1.3 * self.rect.width, self.rect.y, (1.3 * self.rect.width),
                                           self.rect.height)
            ability_sound = pygame.mixer.Sound(
                os.path.abspath("Character/CharacterSound/Punch.mp3"))
            ability_sound.set_volume(GlobalVar.SoundEffect)
            ability_sound.play()

            # 判定应该是个框而不是一个点  还没加判定只有动作
            if self.facing == "Left":
                #pygame.draw.rect(self.map, (0, 0, 0), attack_rect_left)

                self.map.blit(self.attackLeft, self.rect)
                if attack_rect_left.colliderect(opponent.rect):
                    opponent.get_damage(self.damage)

            if self.facing == "Right":
                #pygame.draw.rect(self.map, (0, 0, 0), attack_rect_right)

                self.map.blit(self.attackRight, self.rect)
                if attack_rect_right.colliderect(opponent.rect):
                    opponent.get_damage(self.damage)
            self.attack_stage = "end"

        elif (self.attack_stage == "end"):
            if self.facing == "Left":
                self.map.blit(self.moveLeft, self.rect)
            if self.facing == "Right":
                self.map.blit(self.moveRight, self.rect)
            self.attack = False

    def ability(self, opponent):
        ability_speed = GlobalVar.screen_width * 0.01

        if self.ability_face == "Right":
            if (self.ability_now.colliderect(opponent.rect)):
                opponent.get_damage(self.damage)
            if (self.ability_now.right + ability_speed >= GlobalVar.screen_width):
                ability_speed = GlobalVar.screen_width - self.ability_now.right
                self.ability_use = False
            self.map.blit(self.abilityRight, self.ability_now)
            # self.map.blit(self.moveRight,self.rect)
            self.ability_now.x += ability_speed
        if self.ability_face == "Left":
            self.map.blit(self.abilityLeft, self.ability_now)
            if (self.ability_now.colliderect(opponent.rect)):
                opponent.get_damage(self.damage)
            if (self.ability_now.left - ability_speed <= 0):
                ability_speed = GlobalVar.screen_width - self.ability_now.left
                self.ability_use = False
            self.map.blit(self.abilityLeft, self.ability_now)
            # self.map.blit(self.moveLeft,self.rect)
            self.ability_now.x -= ability_speed

    def up_attack(self, opponent):
        #pygame.draw.rect(self.map, (0, 0, 0), self.slash_rect)
        if time.time()-self.timeup<=1:
            if self.facing == "Left":
                self.map.blit(self.slashLeft, self.rect)
                self.map.blit(self.upAttack, self.slash_rect_left)
                if self.slash_rect_left.colliderect(opponent.rect):
                    opponent.get_damage(0.5)
            if self.facing == "Right":
                self.map.blit(self.slashRight, self.rect)
                self.map.blit(self.upAttack, self.slash_rect_right)
                if self.slash_rect_right.colliderect(opponent.rect):
                    opponent.get_damage(0.5)
        else:
            self.upattacking = False






    def down_attack(self, opponent):
        if time.time()-self.time <=2:
            if self.facing == "Left":
                #pygame.draw.rect(self.map, (0, 0, 0), self.field_rect_left)

                self.map.blit(self.downAttack_left, self.field_rect_left)
                if self.field_rect_left.colliderect(opponent.rect):
                    opponent.get_damage(0.5)
            elif self.facing == "Right":
                #pygame.draw.rect(self.map, (0, 0, 0), self.field_rect_right)

                self.map.blit(self.downAttack_right, self.field_rect_right)
                if self.field_rect_right.colliderect(opponent.rect):
                    opponent.get_damage(0.5)
        else:
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