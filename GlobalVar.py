import pygame
import numpy as np


#STATUS
STATUS="Main"

Disconnect=False
Training = False
AI=False
screen_width=0
screen_height=0
#Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW=(255,241,16)
BLACK=(0,0,0)


Volume=1.0
SoundEffect=100
Brightness=2.0


postionVolumebarX=0
postionsoundeffectbarX=0
postionBrightnessX=0
Setting_count=0
mutebuttonX=0

selectedf1=0
selectedf2=0
player1_spawn_point = [0,0]
player2_spawn_point = [0,0]
map=""
def apply_brightness(image, brightness):
    """Adjust brightness by manipulating pixel values directly."""
    img_array = pygame.surfarray.pixels3d(image).copy()  # Get pixel array and make a copy

    # Apply brightness scaling (multiplying pixel values by brightness)
    img_array = np.clip(img_array * brightness, 0, 255).astype(np.uint8)  # Clip values between 0 and 255

    # Create a new surface from the adjusted pixel array
    brightened_image = pygame.surfarray.make_surface(img_array)

    return brightened_image

keys={
        "player1": {
            "jump": pygame.K_w,
            "move_left": pygame.K_a,
            "move_right": pygame.K_d,
            "attack": pygame.K_j,
            "ability": pygame.K_u,
            "defend": pygame.K_s
        },
        "player2": {
            "jump": pygame.K_UP,
            "move_left": pygame.K_LEFT,
            "move_right": pygame.K_RIGHT,
            "attack": pygame.K_KP0,  # Keypad 0 for player2 attack
            "ability": pygame.K_KP_4,
            "defend": pygame.K_DOWN
        }
}

player1_point=0
player2_point=0

