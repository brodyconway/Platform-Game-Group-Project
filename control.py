import os.path
import pygame
import sys
from pygame.locals import *
import battle
import GlobalVar

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define screen dimensions
screen_width = int(pygame.display.get_desktop_sizes()[0][0]*0.63)
screen_height = int(pygame.display.get_desktop_sizes()[0][1]*0.66)
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up FPS (frames per second)
clock = pygame.time.Clock()
FPS = 60

# Set up fonts
font = pygame.font.Font(None, 36)



# Control positions
control_width = screen_width // 3
control_height = screen_height // 3

# Set target position for control boxes (final positions on screen)
target_position_x = screen_width // 2 + screen_width // 8 # Player 1's final position
target_position_x2 = screen_width // 2 + screen_width // 8 # Player 2's final position

# Speed for the control animation
speed_of_display = 10
# Key layout for player 1 (WASD + J layout)

# Initial X position for Player 1 and Player 2 controls (off-screen to the right)
control_rect_x1 = screen_width
control_rect_x2 = screen_width

# Size of each key box
key_box_size = screen_width//14
box_padding = screen_width//45  # Padding between boxes
extra_horizontal_spacing = screen_height//40  # Extra space between "D" and "J" and "Right" and "Num0"


# Define a vertical offset so Player 1's controls appear above Player 2's controls
vertical_offset = screen_height/5  # Adjust this to create more space between Player 1 and Player 2


def draw_controls():
    pass


def control():
    global controls
    controls = True
    control_rect_x1 = screen_width
    control_rect_x2 = screen_width
    player1_layout = {
        pygame.key.name(GlobalVar.keys["player1"]["jump"]): (1, 0),  # Top (center)
        pygame.key.name(GlobalVar.keys["player1"]["move_left"]): (0, 1),  # Left
        pygame.key.name(GlobalVar.keys["player1"]["move_right"]): (2, 1),  # Right
        pygame.key.name(GlobalVar.keys["player1"]["attack"]): (3, 1),  # To the right of "D", extra space (col 4 instead of 3)
        pygame.key.name(GlobalVar.keys["player1"]["ability"]): (4, 1),
        pygame.key.name(GlobalVar.keys["player1"]["defend"]): (1, 1)

    }

    # Key layout for player 2 (arrow keys + Num0)
    player2_layout = {
        pygame.key.name(GlobalVar.keys["player2"]["jump"]): (1, 0),  # Up arrow
        pygame.key.name(GlobalVar.keys["player2"]["move_left"]): (0, 1),  # Left arrow
        pygame.key.name(GlobalVar.keys["player2"]["move_right"]): (2, 1),  # Right arrow
        pygame.key.name(GlobalVar.keys["player2"]["attack"]): (3, 1),  # To the right of "Right Arrow", with extra space (col 4 instead of 3)
        pygame.key.name(GlobalVar.keys["player2"]["ability"]): (4, 1),
        pygame.key.name(GlobalVar.keys["player2"]["defend"]): (1, 1)
    }

    print(player1_layout)
    while controls and GlobalVar.STATUS=="Control":
        LocalBrightness = GlobalVar.Brightness
        Main_Menu_background = pygame.image.load(os.path.abspath("ImageResource/MainMenu.png"))
        Main_Menu_background = pygame.transform.scale(Main_Menu_background, (screen_width, screen_height))
        Main_Menu_background_Brightness = GlobalVar.apply_brightness(Main_Menu_background, LocalBrightness * 0.5)

        #global control_rect_x1,control_rect_x2

        # Animate the controls moving into the screen
        if control_rect_x1 > target_position_x:
            control_rect_x1 -= speed_of_display  # Move Player 1's controls left
        if control_rect_x2 > target_position_x2:
            control_rect_x2 -= speed_of_display  # Move Player 2's controls left

        # Draw the background image
        screen.blit(Main_Menu_background_Brightness, (0, 0))

        # Define vertical center positions for Player 1 and Player 2
        player1_center_y = (screen_height // 2) - vertical_offset  # Player 1 higher up
        player2_center_y = (screen_height // 2) + vertical_offset  # Player 2 lower down

        # Draw Player 1 WASD + J keys (represented like a keyboard layout)
        for key, (col, row) in player1_layout.items():
            # Apply extra space between "D" and "J"
            if key == GlobalVar.keys["player1"]["attack"]:
                box_x = control_rect_x1 + (col - 1) * (key_box_size + box_padding + extra_horizontal_spacing)
            else:
                box_x = control_rect_x1 + (col - 1) * (key_box_size + box_padding)

            box_y = player1_center_y + (row - 1) * (key_box_size + box_padding)  # Adjust for position
            pygame.draw.rect(screen, RED, (box_x, box_y, key_box_size, key_box_size))
            text_surface = font.render(key, True, WHITE)
            text_rect = text_surface.get_rect(center=(box_x + key_box_size // 2, box_y + key_box_size // 2))
            screen.blit(text_surface, text_rect)

        # Draw Player 2 arrow keys + Num0 (represented like a keyboard layout)
        for key, (col, row) in player2_layout.items():
            # Apply extra space between "Right Arrow" and "Num0"
            if key == GlobalVar.keys["player2"]["attack"]:
                box_x = control_rect_x2 + (col - 1) * (key_box_size + box_padding + extra_horizontal_spacing)
            else:
                box_x = control_rect_x2 + (col - 1) * (key_box_size + box_padding)

            box_y = player2_center_y + (row - 1) * (key_box_size + box_padding)  # Adjust for position
            pygame.draw.rect(screen, RED, (box_x, box_y, key_box_size, key_box_size))
            text_surface = font.render(key, True, WHITE)
            text_rect = text_surface.get_rect(center=(box_x + key_box_size // 2, box_y + key_box_size // 2))
            screen.blit(text_surface, text_rect)

            # Update the display
        pygame.display.flip()
        for event in pygame.event.get():
            # Handle quit event (clicking close or pressing ESC)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            # Handle mouse click event (exit when clicked anywhere on screen)
            if event.type == pygame.MOUSEBUTTONDOWN and GlobalVar.Training == True:
                GlobalVar.STATUS = "Battle"
                print("Control回来时被切换了")
                try:
                    return 1
                finally:
                    battle.battle()
                    GlobalVar.Training= True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                GlobalVar.STATUS = "Main"
                break


        # Set the frame rate
        clock.tick(FPS)

