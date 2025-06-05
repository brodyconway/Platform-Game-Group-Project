import os.path

from Character.Onimaru import  Onimaru
from Character.Selee import Selee
from Character.Catanjeaux import Catanjeaux
from Character.Iris import Iris
import sys
import time

from PIL import Image
import pygame
import GlobalVar

# Initialize Pygame
pygame.init()

# Set up screen dimensions(height and width)
screen_width = int(pygame.display.get_desktop_sizes()[0][0]*0.63)
screen_height = int(pygame.display.get_desktop_sizes()[0][1]*0.66)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sugar World') #name of the game


# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up FPS (frames per second)
clock = pygame.time.Clock()
FPS = 60

#Convert icon to surface
Icon=Image.open(os.path.abspath("ImageResource/Selee menu.png"))
surfaceIco = pygame.image.fromstring(Icon.tobytes(), Icon.size, Icon.mode)
#set_icon function handle surface parameters (transfer image to surface)
pygame.display.set_icon(surfaceIco)
# Background set up
backgrounds_width = screen_width
backgrounds_height = screen_height
winner=0
GlobalVar.player1_point=0
GlobalVar.player2_point=0



def endgame(winner: int,player1,player2):
    timer = time.time()
    if winner == 1:
        while (time.time() - timer <= 3.0):
            screen.blit(player1.winround(screen)[0], player1.winround(screen)[1])
            pygame.display.flip()
            pygame.display.update()
    elif winner == 2:
        while (time.time() - timer <= 3.0):
            screen.blit(player1.winround(screen)[0], player1.winround(screen)[1])
            pygame.display.flip()
            pygame.display.update()
    else:
        while (time.time() - timer <= 3.0):
            pass
    ai()

def move1(player2, player1):
    if (player2.attack == False):
        if player2.facing == "Right":
            player2.map.blit(player2.moveRight, player2.rect)
        if player2.facing == "Left":
            player2.map.blit(player2.moveLeft, player2.rect)
    # Calculate the distance between player2 and player1
    distance_x = player1.rect.centerx - player2.rect.centerx
    dx = 0
    dy = 0
    # Determine the movement direction towards player1
    if abs(distance_x) >= screen_width*0.25:  # If player2 is more than 150 pixels away


        #pygame.draw.rect(player2.map, (0, 0, 0), player2.rect)
        if player2.attack == False and not player2.ability_use:
            if distance_x > 0:

                if abs(player2.rect.right - player1.rect.left) > player2.speed or player2.rect.bottom > player2.bottom:
                    dx = player2.speed
                elif (player2.y == player2.bottom) and player1.rect.left - player2.rect.right < player2.speed:
                    dx = player2.rect.right - player1.rect.left
                player2.facing = "Right"
            if distance_x < 0:
                if abs(player1.rect.right - player2.rect.left) > player2.speed or player2.rect.bottom > player2.bottom:
                    dx -= player2.speed
                #elif (player2.y == player2.bottom) and player1.rect.right - player2.rect.left > player2.speed:
                  #  dx = player1.rect.right - player2.rect.left
                player2.facing = "Left"
                #print(dx)
    else:
        print(99)
        #pygame.draw.rect(player2.map, (0, 0, 0), player2.rect)
        if player2.attack == False and not player2.ability_use:
           # print(999999999999)
            if not player2.upattacking and not player2.downattacking:
                player2.attack = True
                player2.attack_stage = "start"

        if (player2.attack == False and player2.downattacking == False):
            if player2.facing == "Right":
                #pygame.draw.rect(player2.map, (0, 0, 0), player2.rect)
                player2.map.blit(player2.moveRight, player2.rect)
            if player2.facing == "Left":
                player2.map.blit(player2.moveLeft, player2.rect)

        player2.vel_y += player2.gravity
        dy += player2.vel_y

        # bian jie
    if player2.rect.left + dx < 0:
        dx = -player2.rect.left
    if player2.rect.right + dx > GlobalVar.screen_width:
        dx = GlobalVar.screen_width - player2.rect.right

    if player2.rect.bottom + dy >= player2.bottom:
        player2.vel_y = 0
        dy = player2.bottom - player2.rect.bottom
        player2.jump = False
    print(player2.attack)
    player2.rect.x += dx
    player2.rect.y += dy
    print(distance_x)
    if player2.attack == True:
        print("attacking")
        player2.attacking(player1)


    # Ensure player2 doesn't move outside the screen boundaries

def ai():
    times = time.time()

    Characters = {
        "Selee_player1": Selee(GlobalVar.player1_spawn_point[0], GlobalVar.player1_spawn_point[1],screen,"player1"),
        "Selee_player2": Selee(GlobalVar.player2_spawn_point[0], GlobalVar.player2_spawn_point[1],screen,"player2"),
        "Catanjeaux_player1": Catanjeaux(GlobalVar.player1_spawn_point[0], GlobalVar.player1_spawn_point[1],screen,"player1"),
        "Catanjeaux_player2": Catanjeaux(GlobalVar.player2_spawn_point[0], GlobalVar.player2_spawn_point[1],screen,"player2"),
        "Irises_player1":Iris(GlobalVar.player1_spawn_point[0], GlobalVar.player1_spawn_point[1],screen,"player1"),
        "Irises_player2": Iris(GlobalVar.player2_spawn_point[0], GlobalVar.player2_spawn_point[1], screen, "player2"),
        "Onimaru_player1": Onimaru(GlobalVar.player1_spawn_point[0], GlobalVar.player1_spawn_point[1], screen,
                                   "player1"),
        "Onimaru_player2": Onimaru(GlobalVar.player2_spawn_point[0], GlobalVar.player2_spawn_point[1], screen,
                                   "player2")
    }

    Training=False

    if (GlobalVar.player1_point == 2) or GlobalVar.player2_point == 2:
        font = pygame.font.SysFont(None, 40)
        text_obj = font.render("Winner Player1", True, (0, 0, 0))
        screen.blit(text_obj, (screen_width / 2, screen_height / 2))
        pygame.time.delay(3000)
        GlobalVar.STATUS = "Main"
        return True

    while(time.time() - times <= 1.0):
        screen.fill(WHITE)
        pygame.display.flip()
        pygame.display.update()

    Map = GlobalVar.map
    Map_Dispaly = Map
    Map_Rect = Map.get_rect()
    player1 =Characters.get(GlobalVar.selectedf1)
    player2 =Characters.get(GlobalVar.selectedf2)


    screen.blit(Map_Dispaly, Map_Rect)

    # player1.stand()
    player1.move(player2)
    #player2.move(player1)

    move1(player2, player1)
    player1.health_bar()
    player2.health_bar()
    pygame.display.flip()
    pygame.display.update()

    times = time.time()
    while (time.time() - times <= 2.0):
        pass

    #等待一个音效
    player1.stop = False
    player2.stop = False


    while True:

        screen.blit(Map_Dispaly, Map_Rect)

        if player1.health<=0:
            winner=2
            GlobalVar.player2_point +=1
            try:
                break
            finally:
                endgame(winner, player1, player2)
        elif player2.health<=0 :
            winner=1
            GlobalVar.player1_point +=1
            try:
                break
            finally:
                endgame(winner, player1, player2)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        key= pygame.key.get_pressed()


        player1.move(player2)
        #player2.move(player1)
        move1(player2, player1)

        player1.health_bar()
        player2.health_bar()
        # player1

        # player2

        pygame.display.flip()
        pygame.display.update()
        time2 = time.time()
        while(time.time()-time2 <0.02):
            pass

if(GlobalVar.STATUS == "AI"):
    ai()