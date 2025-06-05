import os.path
import pygame
import sys
from PIL import Image, ImageDraw, ImageFont
import pygame

import Single_Player
import button
import GlobalVar
import Multiple_Players
import Setting

import control
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
def Serve_AIandTraining():
    running = True


    while running and GlobalVar.STATUS == "AI and Training Mode" :

        pygame.mixer.music.set_volume(GlobalVar.Volume)
        # Handle events

        LocalBrightness = GlobalVar.Brightness
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if AI_Mode_button.checkForInput(pos):
                    GlobalVar.STATUS = "AI Mode"
                    GlobalVar.AI=True
                    Single_Player.serve_single_games()

                if Training_button.checkForInput(pos):
                    GlobalVar.STATUS = "Single Selection"
                    GlobalVar.Training=True
                    Single_Player.serve_single_games()

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
            AI_Mode_button = button.Button(image=None, pos=(screen_width * 0.5, screen_height * 0.55),
                                              text_input="AI Mode", font=pygame.font.SysFont("arialblack", 60),
                                              base_color="Yellow", hovering_color="Black")
            button.Button.update(AI_Mode_button, screen)
            Training_button = button.Button(image=None, pos=(screen_width * 0.5, screen_height * 0.73),
                                            text_input="Training", font=pygame.font.SysFont("arialblack", 60),
                                            base_color="Yellow", hovering_color="Black")
            button.Button.update(Training_button, screen)


        # Update the display
        pygame.display.flip()

        # Set the frame rate
        clock.tick(FPS)



Serve_AIandTraining()