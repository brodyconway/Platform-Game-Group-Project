import os.path

from PIL import Image
import pygame
from pygame import SurfaceType
import GlobalVar

class Player2:

    def __init__(self, x, y, map, screen_width, screen_height):
        self.health = 100
        self.map = map
        self.rect = pygame.Rect(x, y, 180, 220)
        self.jump = False
        self.fall = False
        self.floor = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = Image.open(os.path.abspath("Character/CharacterImage/" + GlobalVar.selectedf2 + ".png"))
        self.attack = False
        self.stop = True
        self.face = "Left"
        self.damaged = False
        self.ability_status = False
        self.attack_cooldown = False  # Cooldown state
        self.cooldown_time = 1.0  # Cooldown duration in seconds
        self.cooldown_timer = 0  # Timer to track cooldown
        self.abilityend = 0
        self.ability_x = 0
        self.ability_y = 0


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
        self.draw_health_bar(map, map.get_size()[0] * 0.6, map.get_size()[1] * 0.08)  # Health bar for player 2
        if(action == "combo_down_attack"):
            attckimage = pygame.image.load(
                os.path.abspath("Character/CharacterImage/" + GlobalVar.selectedf2 + "_combo_down_attack.png"))

            # Scale the image to the desired size (180x220)
            attckimage = pygame.transform.scale(attckimage, (180, 220))

            # Blit the image at the player's current position
            self.map.blit(attckimage, self.rect)

        elif (self.attack) and self.face == "Left":
            attckimage = pygame.image.load(
                os.path.abspath("Character/CharacterImage/" + GlobalVar.selectedf2 + "_attack_left.png"))

            # Scale the image to the desired size (180x220)
            attckimage = pygame.transform.scale(attckimage, (180, 220))

            # Blit the image at the player's current position
            self.map.blit(attckimage, self.rect)

            # Reset the attack status
            self.attack = False
        elif (self.attack) and self.face == "Right":
            attckimage = pygame.image.load(
                os.path.abspath("Character/CharacterImage/" + GlobalVar.selectedf2 + "_attack_right.png"))

            # Scale the image to the desired size (180x220)
            attckimage = pygame.transform.scale(attckimage, (180, 220))

            # Blit the image at the player's current position
            self.map.blit(attckimage, self.rect)

            # Reset the attack status
            self.attack = False
        elif (action == "stand") and self.face == "Right":
            ser = pygame.image.load(
            os.path.abspath("Character/CharacterImage/" + GlobalVar.selectedf2 + "_right.png"))
            ser = pygame.transform.scale(ser, (180, 220))
            self.map.blit(ser, self.rect)

        elif (action == "stand") and self.face == "Left":
            print("is Standing")
            ser = pygame.image.load(
            os.path.abspath("Character/CharacterImage/" + GlobalVar.selectedf2 + "_left.png"))
            ser = pygame.transform.scale(ser, (180, 220))
            map.blit(ser, self.rect)
        elif (action == "damaged") and self.face == "Right":
            ser = pygame.image.load(
                os.path.abspath("Character/CharacterImage/" + GlobalVar.selectedf2 + "_get_attack_right.png"))
            ser = pygame.transform.scale(ser, (180, 220))
            self.map.blit(ser, self.rect)
        elif (action == "damaged") and self.face == "Left":
            ser = pygame.image.load(
                os.path.abspath("Character/CharacterImage/" + GlobalVar.selectedf2 + "_get_attack_Left.png"))
            ser = pygame.transform.scale(ser, (180, 220))
            self.map.blit(ser, self.rect)

    def move(self, map_width, map_height, playeropp):
        speed = 5
        move_x = 0
        move_y = 0
        gravity = 2
        key = pygame.key.get_pressed()

        # Handle cooldown timer
        if self.attack_cooldown:
            current_time = pygame.time.get_ticks()  # Get current time in milliseconds
            if current_time - self.cooldown_timer >= self.cooldown_time * 500:
                self.attack_cooldown = False  # Cooldown has ended

        if not self.damaged:
            self.display(self.map, "stand")
        else:
            self.damaged = False

        if not self.stop and not self.attack_cooldown:  # Prevent movement/actions during cooldown
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
            if not self.jump and not self.fall and key[pygame.K_UP]:
                self.jump = True

            # Move Left
            if key[GlobalVar.keys["player2"]["move_left"]]:
                self.face = "Left"
                move_x -= speed
                ability_sound = pygame.mixer.Sound(
                    os.path.abspath("Character/CharacterSound/Walk.mp3"))
                ability_sound.set_volume(GlobalVar.SoundEffect)
                ability_sound.play()

            # Move Right
            if key[GlobalVar.keys["player2"]["move_right"]]:
                self.face = "Right"
                move_x += speed
                ability_sound = pygame.mixer.Sound(
                    os.path.abspath("Character/CharacterSound/Walk.mp3"))
                ability_sound.set_volume(GlobalVar.SoundEffect)
                ability_sound.play()

            # Boundary check to prevent moving out of bounds
            if self.rect.left + move_x < 0:
                move_x -= self.rect.left
            if self.rect.right + move_x > map_width:
                move_x = map_width - self.rect.right

            # Update location
            self.rect.x += move_x
            self.rect.y += move_y

            # Handle attack and ability
            is_attack = key[GlobalVar.keys["player2"]["attack"]] and not self.attack and not self.attack_cooldown
            is_ability = key[GlobalVar.keys["player2"]["ability"]] and not self.attack_cooldown
            is_defend = key[GlobalVar.keys["player2"]["defend"]] and not self.attack_cooldown

            if is_attack:
                self.attack = True
                ability_sound = pygame.mixer.Sound(os.path.abspath("Character/CharacterSound/Punch.mp3"))
                ability_sound.set_volume(GlobalVar.SoundEffect)
                ability_sound.play()

                # Start cooldown
                self.attack_cooldown = True
                self.cooldown_timer = pygame.time.get_ticks()  # Set the timer when the attack is performed

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

            if is_ability and not self.ability_status:
                self.ability_status = True
                self.ability_x = self.rect.x
                self.ability_y = self.rect.y
                self.ability(self.ability_x, self.ability_y)

            # Handle simultaneous attack and defend
            if is_attack and is_defend:
                # Load and display the combo image
                self.display(self.map, "combo_down_attack")
                range_offset = map_width // 5

                # Check if the opponent is a bit left or a bit right
                if (
                        self.rect.x - range_offset <= playeropp.rect.x <= self.rect.x + range_offset) and playeropp.rect.y == self.rect.y:
                    playeropp.damage(10)

            # Ability movement and effects
            if self.ability_status and self.face == "Right":
                self.ability_x += self.screen_width // 5
                self.ability(self.ability_x, self.ability_y)
                if self.ability_x > self.screen_width:
                    self.ability_status = False
                if playeropp.rect.x - self.screen_width * 0.3 <= self.ability_x <= playeropp.rect.x + self.screen_width * 0.3:
                    playeropp.damage(5)
                    ability_sound = pygame.mixer.Sound(
                        os.path.abspath("Character/CharacterSound/" + GlobalVar.selectedf2 + "_ability.mp3"))
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
                        os.path.abspath("Character/CharacterSound/" + GlobalVar.selectedf2 + "_ability.mp3"))
                    ability_sound.set_volume(GlobalVar.SoundEffect)
                    ability_sound.play()

    #revive damage
    def damage(self,damage):
        print(damage)
        self.health -= damage
        if False and self.health <= 0:
            self.health=100

        self.damaged = True
        self.stop=True
        self.display(self.map,"damaged")
        self.stop=False

        ability_sound = pygame.mixer.Sound(
            os.path.abspath("Character/CharacterSound/Damaged_Sound.mp3"))
        ability_sound.set_volume(GlobalVar.SoundEffect)
        ability_sound.play()

    def ability(self,x,y):
        ab_left=pygame.image.load((os.path.abspath("Character/CharacterImage/"+GlobalVar.selectedf2 + "_ability_left.png")))
        ab_left=pygame.transform.scale(ab_left, (self.screen_width*0.3,self.screen_height*0.3))
        ab_right=pygame.image.load((os.path.abspath("Character/CharacterImage/"+GlobalVar.selectedf2 + "_ability_right.png")))
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

    def getcrruntlocation(self):
        return self.rect.x, self.rect.y

    def winround(self, map: SurfaceType):
        font = pygame.font.SysFont('Arial', 40)
        Winner = font.render("Winner", True, (255, 255, 255))
        rect = Winner.get_rect()
        rect.center = (map.get_size()[0] * 0.6, map.get_size()[1] * 0.04)
        return [Winner, rect]

