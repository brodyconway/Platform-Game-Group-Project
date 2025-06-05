import os.path
import pygame
import sys
from PIL import Image
import pygame

import AI_and_Training_Mode
import button
import GlobalVar

import control
import Multiple_Players
import Setting
import Map_Selection
from Map_Selection import LocalBrightness

# Initialize Pygame
pygame.init()

# Set up screen dimensions(height and width)
screen_width = pygame.display.get_desktop_sizes()[0][0] * 0.63
screen_height = pygame.display.get_desktop_sizes()[0][1] * 0.66
screen = pygame.display.set_mode((screen_width, screen_height))


def ret_screen_size():
    return [screen_width, screen_height]


pygame.display.set_caption('Sugar World')  # name of the game

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)


# Setting up text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# Set up FPS (frames per second)
clock = pygame.time.Clock()
FPS = 60

# Player settings for proof for concepts(for now)
player_width = 50
player_height = 50

# Convert image to surface
Icon = Image.open(os.path.abspath("ImageResource/Selee menu.png"))
surfaceIco = pygame.image.fromstring(Icon.tobytes(), Icon.size, Icon.mode)

# set_icon function handle surface parameters (transfer image to surface)
pygame.display.set_icon(surfaceIco)

pygame.mixer.music.load(os.path.abspath("Music/Guitar Man.mp3"))

pygame.mixer.music.play(loops=-1)


# Main game loop
def Serve_ModeSelection():
    running = True
    # Setting up status
    #GlobalVar.STATUS = "Mode Selection"
    while running and GlobalVar.STATUS == "Mode Selection":

        pygame.mixer.music.set_volume(GlobalVar.Volume)
        # Handle events

        LocalBrightness = GlobalVar.Brightness
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if Multiple_Players_button.checkForInput(pos):
                    GlobalVar.STATUS = "Multiple Selection"
                    Multiple_Players.serve_multiple_games()

                if Single_Player_button.checkForInput(pos):
                    GlobalVar.STATUS = "AI and Training Mode"
                    AI_and_Training_Mode.Serve_AIandTraining()

            # Get keys pressed
            keys = pygame.key.get_pressed()
            # Set screen to the main menu background, set background color to white before that.
            LocalBrightness = GlobalVar.Brightness
            Main_Menu_background = pygame.image.load(os.path.abspath("ImageResource/MainMenu.png"))
            Main_Menu_background = pygame.transform.scale(Main_Menu_background, (screen_width, screen_height))
            Main_Menu_background_Brightness = GlobalVar.apply_brightness(Main_Menu_background, LocalBrightness * 0.5)

            # There is some white space exist because the image doesn't fit the ratio of the screen size!
            screen.fill(WHITE)
            screen.blit(Main_Menu_background_Brightness, (0, 0))
            draw_text("Sugar World", pygame.font.SysFont("arial", 60, False, True), PINK, screen_width * 0.4,
                      screen_height * 0.15)
            Multiple_Players_button = button.Button(image=None, pos=(screen_width * 0.5, screen_height * 0.55),
                                              text_input="Multiple Players", font=pygame.font.SysFont("arialblack", 60),
                                              base_color="Yellow", hovering_color="Black")
            button.Button.update(Multiple_Players_button, screen)
            Single_Player_button = button.Button(image=None, pos=(screen_width * 0.5, screen_height * 0.73),
                                            text_input="Single Player", font=pygame.font.SysFont("arialblack", 60),
                                            base_color="Yellow", hovering_color="Black")
            button.Button.update(Single_Player_button, screen)


        # Update the display
        pygame.display.flip()

        # Set the frame rate
        clock.tick(FPS)



Serve_ModeSelection()

