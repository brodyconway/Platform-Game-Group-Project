import os.path


import random
from Character.Onimaru import Onimaru
from Character.Selee import Selee
from Character.Catanjeaux import Catanjeaux
from Character.Iris import Iris
import sys
import time
import control
from PIL import Image
import pygame
import Player2
import Player1
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

# Load the falling object (cherry blossom petal) image
petal_image = pygame.image.load(os.path.abspath("ImageResource/Maps/cherry_blossom_petal.png"))
petal_image = pygame.transform.scale(petal_image, (30, 30))  # Adjust size as needed

# Falling object variables
falling_petals = []
petal_spawn_interval = random.randint(2 * FPS, 5 * FPS)  # Petals appear every 2-5 seconds
petal_timer = 0  # Timer to keep track of when to spawn the next petal

def endgame(winner: int,player1,player2):
    timer = time.time()
    if winner == 1:
        while (time.time() - timer <= 3.0):
            screen.blit(player1.winround(screen)[0], player1.winround(screen)[1])
            pygame.display.flip()
            pygame.display.update()
    elif winner == 2:
        while (time.time() - timer <= 3.0):
            screen.blit(player2.winround(screen)[0], player2.winround(screen)[1])
            pygame.display.flip()
            pygame.display.update()
    else:
        while (time.time() - timer <= 3.0):
            pass

    battle()


def update_falling_objects(player1, player2):
    global petal_timer, petal_spawn_interval
    petal_timer += 1
    if petal_timer >= petal_spawn_interval:
        petal_timer = 0
        petal_spawn_interval = random.randint(2 * FPS, 5 * FPS)
        petal_x = random.randint(0, screen_width - 30)
        falling_petals.append(pygame.Rect(petal_x, 0, 30, 30))  # Add new petal rect

    # Move each petal down and remove if it goes off screen
    for petal in falling_petals[:]:
        petal.y += 5  # Adjust falling speed here
        if petal.y > screen_height:
            falling_petals.remove(petal)

    # Draw and check for collisions with players
    for petal in falling_petals:
        screen.blit(petal_image, petal.topleft)
        if player1.rect.colliderect(petal):
            player1.health -= 1
            falling_petals.remove(petal)
        elif player2.rect.colliderect(petal):
            player2.health -= 1
            falling_petals.remove(petal)
def battle():
    font = pygame.font.SysFont('Arial', 40)
    optext = font.render("Control", True, GlobalVar.BLUE)
    oprect = optext.get_rect()
    oprect.center = (screen_width // 2, screen_height // 20)
    times = time.time()


    Characters = {
        "Selee_player1": Selee(GlobalVar.player1_spawn_point[0], GlobalVar.player1_spawn_point[1],screen,"player1"),
        "Selee_player2": Selee(GlobalVar.player2_spawn_point[0], GlobalVar.player2_spawn_point[1],screen,"player2"),
        "Catanjeaux_player1": Catanjeaux(GlobalVar.player1_spawn_point[0], GlobalVar.player1_spawn_point[1],screen,"player1"),
        "Catanjeaux_player2": Catanjeaux(GlobalVar.player2_spawn_point[0], GlobalVar.player2_spawn_point[1],screen,"player2"),
        "Irises_player1": Iris(GlobalVar.player1_spawn_point[0], GlobalVar.player1_spawn_point[1],screen,"player1"),
        "Irises_player2": Iris(GlobalVar.player2_spawn_point[0], GlobalVar.player2_spawn_point[1],screen,"player2"),
        "Onimaru_player1":Onimaru(GlobalVar.player1_spawn_point[0], GlobalVar.player1_spawn_point[1],screen,"player1"),
        "Onimaru_player2": Onimaru(GlobalVar.player2_spawn_point[0], GlobalVar.player2_spawn_point[1], screen, "player2")
    }


    print(f"玩家2的胜点{GlobalVar.player1_point}")
    if (GlobalVar.player1_point == 2) or GlobalVar.player2_point == 2:
        print("结束程序被启动了")
        font = pygame.font.SysFont(None, 40)
        text_obj = font.render("Winner Player", True, (0, 0, 0))
        screen.blit(text_obj, (screen_width / 2, screen_height / 2))
        pygame.time.delay(3000)
        GlobalVar.STATUS = "Main"
        GlobalVar.Training=False
        return True

    while(time.time() - times <= 2.0):
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
    player2.move(player1)
    player1.health_bar()
    player2.health_bar()
    pygame.display.flip()
    pygame.display.update()

    times = time.time()
    while (time.time() - times <= 1.0):
        pass

    #等待一个音效
    player1.stop = False
    player2.stop = False
    if GlobalVar.Training == True:
        player2.training = True

    while GlobalVar.STATUS == "Battle":


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



        screen.blit(Map_Dispaly, Map_Rect)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and GlobalVar.Training==True:
                mouse_pos=pygame.mouse.get_pos()
                if oprect.collidepoint(mouse_pos):
                    GlobalVar.STATUS = "Control"
                    control.control()

        key= pygame.key.get_pressed()
        # if key[GlobalVar.keys["player1"]["jump"]] and not player1.rise and not player1.fall and not player1.air:
        #     player1.rise=True
        #     print("键位获取成功")
        # elif key[GlobalVar.keys["player1"]["move_left"]]:
        #     player1.move_left(player2)
        # elif key[GlobalVar.keys["player1"]["move_right"]]:
        #     player1.move_right(player2)
        # elif key[GlobalVar.keys["player1"]["attack"]]:
        #     player1.attack(player2)
        # elif key[GlobalVar.keys["player1"]["ability"]]:
        #     player1.ability(player2)
        # else:
        #     player1.stand()

        player1.move(player2)


        player2.move(player1)



        player1.health_bar()
        player2.health_bar()
        # Update falling objects (cherry blossom petals)
        update_falling_objects(player1, player2)

        if GlobalVar.Training == True:
            screen.blit(optext, oprect)
        # player1

        # player2

        pygame.display.flip()
        pygame.display.update()
        time2 = time.time()
        while(time.time()-time2 <0.02):
            pass

# if(GlobalVar.STATUS == "Battle"):
#     battle()