import os.path
from platform import system
import time
from PIL import Image
import pygame
from pygame import SurfaceType
import GlobalVar


class Player1:


    def __init__(self,x,y,map,screen_width,screen_height):
        self.health = 100
        self.map = map
        self.rect = pygame.Rect(x,y,180,220)
        self.jump = False
        self.fall = False
        self.floor = y
        self.screen_width = screen_width
        self.screen_height=screen_height
        self.image = Image.open(os.path.abspath("Character/CharacterImage/"+GlobalVar.selectedf1 + ".png"))
        self.attack = False
        self.stop = True
        self.face = "Right"
        self.damaged = False
        self.ability_status = False
        self.abilityend = 0
        self.ability_x = 0
        self.ability_y = 0
        self.pause = False

        self.image.transpose(Image.FLIP_LEFT_RIGHT)
        image = pygame.image.fromstring(self.image.tobytes(), self.image.size, self.image.mode)
        self.image = pygame.transform.scale(image, (180, 220))



    def draw_health_bar(self,screen, x, y):
        # Define colors
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        # Calculate the width of the health bar based on the current health
        bar_width = screen.get_size()[0] * 0.35  # Fixed width of the health bar
        bar_height = screen.get_size()[1] * 0.03  # Height of the health bar

        # Draw the white frame (border)
        frame_rect = pygame.Rect(x, y, bar_width, bar_height)
        pygame.draw.rect(screen, WHITE, frame_rect, 2)  # Draw white border with thickness 2

        # Draw the red health bar
        health = bar_width * (self.health/100)
        health_rect = pygame.Rect(x, y, health, bar_height)
        pygame.draw.rect(screen, RED, health_rect)
        #select

        # Debug print to confirm the health bar is being drawn

    def display(self,map,action):
        self.draw_health_bar(map, map.get_size()[0]*0.05, map.get_size()[1]*0.08)  # Health bar for player 1
        if(action == "combo_down_ability"):
            ser = pygame.image.load(
                os.path.abspath("Character/CharacterImage/" + GlobalVar.selectedf1 + "_combo_down_ability.png"))

            # Get the size of the map (screen)
            screen_width, screen_height = map.get_size()

            # Scale the image to have the height of the entire screen
            ser_width = ser.get_width()
            ser_height = ser.get_height()

            # Calculate the new width proportionally to maintain aspect ratio
            new_height = screen_height + screen_height/3
            new_width = int(ser_width * (new_height / ser_height))

            # Scale the image
            ser = pygame.transform.scale(ser, (new_width, new_height))

            # Center the image horizontally and blit it to the screen
            ser_rect = ser.get_rect(center=(self.rect.centerx, screen_height // 2 - screen_height // 9))
            map.blit(ser, ser_rect)

        elif(self.attack) and self.face == "Left":
            attckimage = pygame.image.load(
                os.path.abspath("Character/CharacterImage/" + GlobalVar.selectedf1 + "_attack_left.png"))

            # Scale the image to the desired size (180x220)
            attckimage = pygame.transform.scale(attckimage, (180, 220))

            # Blit the image at the player's current position
            self.map.blit(attckimage, self.rect)
            self.attack = False

            # Reset the attack status
        elif(self.attack) and self.face == "Right":
            attckimage = pygame.image.load(os.path.abspath("Character/CharacterImage/" + GlobalVar.selectedf1 + "_attack_right.png"))
            # Scale the image to the desired size (180x220)
            attckimage = pygame.transform.scale(attckimage, (180, 220))
            # Blit the image at the player's current position
            self.map.blit(attckimage, self.rect)

            # Reset the attack status
            self.attack = False
        elif(action == "stand") and self.face == "Right":
            ser = pygame.image.load(os.path.abspath("Character/CharacterImage/"+GlobalVar.selectedf1 + "_right.png"))
            ser = pygame.transform.scale(ser, (180, 220))
            map.blit(ser, self.rect)

        elif(action == "stand") and self.face == "Left":
            print("is standing")
            ser = pygame.image.load(os.path.abspath("Character/CharacterImage/" + GlobalVar.selectedf1 + "_left.png"))
            ser = pygame.transform.scale(ser, (180, 220))
            map.blit(ser, self.rect)

        elif(action == "damaged") and self.face == "Right":
            ser = pygame.image.load(os.path.abspath("Character/CharacterImage/" + GlobalVar.selectedf1 + "_get_attack_right.png"))
            ser = pygame.transform.scale(ser, (180, 220))
            self.map.blit(ser, self.rect)
        elif(action == "damaged") and self.face == "Left":
            ser = pygame.image.load(os.path.abspath("Character/CharacterImage/" + GlobalVar.selectedf1 + "_get_attack_Left.png"))
            ser = pygame.transform.scale(ser, (180, 220))
            self.map.blit(ser, self.rect)






    def move(self,map_width,map_height,playeropp):
        speed = 5
        move_x = 0
        move_y = 0
        gravity = 2
        key = pygame.key.get_pressed()
        if(not self.stop):
            if self.jump:
                # Going up
                move_y -= 2
                if self.rect.y <= self.floor - 200:
                    self.jump = False
                    self.fall = True

            elif self.fall:
                # Going down (falling)
                move_y += gravity
                gravity += gravity
                if self.rect.y >= self.floor:
                    move_y = self.floor - self.rect.y
                    self.fall = False

                # Check if the player initiates a jump
            elif not self.jump and not self.fall and key[GlobalVar.keys["player1"]["jump"]]:
                self.jump = True


            #move right
            if(key[GlobalVar.keys["player1"]["move_left"]]):
                # Play the ability sound effect without stopping the music
                self.face = "Left"
                move_x -= speed
                #move left
                ability_sound = pygame.mixer.Sound(
                    os.path.abspath("Character/CharacterSound/Walk.mp3"))
                ability_sound.set_volume(GlobalVar.SoundEffect)
                ability_sound.play()

            if(key[GlobalVar.keys["player1"]["move_right"]]):
                self.face = "Right"
                move_x += speed
                #stop when leftest
                ability_sound = pygame.mixer.Sound(
                    os.path.abspath("Character/CharacterSound/Walk.mp3"))
                ability_sound.set_volume(GlobalVar.SoundEffect)
                ability_sound.play()

            if(self.rect.left + move_x < 0):
                move_x -= self.rect.left
            #stop when rightest
            if(self.rect.right + move_x > map_width):
                move_x = map_width  - self.rect.right

                #update location
            self.rect.x += move_x
            self.rect.y += move_y

                #attack
            # Handle attack and ability
            is_attack = key[GlobalVar.keys["player1"]["attack"]]
            is_ability = key[GlobalVar.keys["player1"]["ability"]]
            is_defend = key[GlobalVar.keys["player1"]["defend"]]

            if is_attack and not self.pause :
                self.attack = True
                self.pause = True
                ability_sound = pygame.mixer.Sound(os.path.abspath("Character/CharacterSound/Punch.mp3"))
                ability_sound.set_volume(GlobalVar.SoundEffect)
                ability_sound.play()
                # Check opponent position
                if self.face == "Right":
                    if playeropp.rect.x > self.rect.x:
                        distance_to_opponent_x = abs(playeropp.rect.x - self.rect.x)
                        distance_to_opponent_y = abs(self.rect.y - playeropp.rect.y)
                        if distance_to_opponent_x <= 100 and distance_to_opponent_y <= 80:
                            playeropp.damage(1)
                elif self.face == "Left":
                    if playeropp.rect.x < self.rect.x:
                        distance_to_opponent_x = abs(self.rect.x - playeropp.rect.x)
                        distance_to_opponent_y = abs(self.rect.y - playeropp.rect.y)
                        if distance_to_opponent_x <= 100 and distance_to_opponent_y <= 80:
                            playeropp.damage(1)

            elif is_ability and not self.ability_status:
                self.ability_status = True
                self.ability_x = self.rect.x
                self.ability_y = self.rect.y

            # Handle simultaneous attack and ability key press
            elif is_ability and is_defend:
                # Load and display the combo image
                self.display(self.map,"combo_down_ability")
                range_offset = map_width // 10

                # Check if the opponent is a bit left or a bit right
                if (
                        self.rect.x - range_offset <= playeropp.rect.x <= self.rect.x + range_offset):
                    playeropp.damage(10)


            # Ability movement and effects
            elif self.ability_status and self.face == "Right":
                self.ability_x += self.screen_width // 5
                self.ability(self.ability_x, self.ability_y)
                if self.ability_x > self.screen_width:
                    self.ability_status = False
                if playeropp.rect.x - self.screen_width * 0.3 <= self.ability_x <= playeropp.rect.x + self.screen_width * 0.3:
                    playeropp.damage(5)
                    ability_sound = pygame.mixer.Sound(
                        os.path.abspath("Character/CharacterSound/" + GlobalVar.selectedf1 + "_ability.mp3"))
                    ability_sound.set_volume(GlobalVar.SoundEffect)
                    ability_sound.play()

            elif self.ability_status and self.face == "Left":
                self.ability_x -= self.screen_width // 5
                self.ability(self.ability_x, self.ability_y)
                if self.ability_x < 0:
                    self.ability_status = False
                if playeropp.rect.x - self.screen_width * 0.3 <= self.ability_x <= playeropp.rect.x + self.screen_width * 0.3:
                    playeropp.damage(5)
                    ability_sound = pygame.mixer.Sound(
                        os.path.abspath("Character/CharacterSound/" + GlobalVar.selectedf1 + "_ability.mp3"))
                    ability_sound.set_volume(GlobalVar.SoundEffect)
                    ability_sound.play()

        if not self.damaged:
            self.display(self.map, "stand")
            self.pause = False
        else:
            self.damaged = False


    def ability(self,x,y):
        ab_left=pygame.image.load((os.path.abspath("Character/CharacterImage/"+GlobalVar.selectedf1 + "_ability_left.png")))
        ab_left=pygame.transform.scale(ab_left, (self.screen_width*0.3,self.screen_height*0.3))
        ab_right=pygame.image.load((os.path.abspath("Character/CharacterImage/"+GlobalVar.selectedf1 + "_ability_right.png")))
        ab_right=pygame.transform.scale(ab_right, (self.screen_width*0.3,self.screen_height*0.3))
        ab_left_rect=ab_left.get_rect()
        ab_right_rect=ab_right.get_rect()
        ab_left_rect.x=x
        ab_left_rect.y=y
        ab_right_rect.x=x
        ab_right_rect.y=y
        if self.face == "Left":
            self.map.blit(ab_left, ab_left_rect)
        elif self.face=="Right":
            self.map.blit(ab_right,ab_right_rect)


    #revive damage
    def damage(self,damage):
        self.health -= damage

        self.damaged = True
        self.display(self.map, "damaged")

        ability_sound = pygame.mixer.Sound(
            os.path.abspath("Character/CharacterSound/Damaged_Sound.mp3"))
        ability_sound.set_volume(GlobalVar.SoundEffect)
        ability_sound.play()

    def getcrruntlocation(self):
        return self.rect.x, self.rect.y

    def winround(self,map:SurfaceType):
        font = pygame.font.SysFont('Arial', 40)
        Winner = font.render("Winner", True, (255,255,255))
        rect = Winner.get_rect()
        rect.center = (map.get_size()[0] *0.35 , map.get_size()[1]*0.04)
        return [Winner,rect]
