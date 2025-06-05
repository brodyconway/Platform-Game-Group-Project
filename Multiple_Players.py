import os.path
import pygame
import sys
from PIL import Image
from pygame import mouse

import GlobalVar
import Map_Selection

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = pygame.display.get_desktop_sizes()[0][0]*0.63
SCREEN_HEIGHT = pygame.display.get_desktop_sizes()[0][1]*0.66
BOX_SIZE = SCREEN_HEIGHT*50/800
PADDING = 10
HIGHLIGHT_SIZE_INCREASE = 10  # Increase the size of the blue background box

# Colors
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#model name
pygame.display.set_caption('Suger World')


# Set up FPS (frames per second)
clock = pygame.time.Clock()
FPS = 60




#Set up width and height of image
Image_width = SCREEN_WIDTH
Image_height = SCREEN_HEIGHT

font_size = 36
font = pygame.font.Font(None, font_size)

#adding label image
# Label_image_surface = pygame.image.load(os.path.abspath("ImageResource/CharacterSelection/Label of Single Player.png"))
# Label_rect = Label_image_surface.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//5))
# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Map Selection")

# Grid setup: 2 rows, 4 columns (adjusted for 4 images)
rows = 1
cols = 4  # We have 4 images

# Selected row and column
selected_row = 0
selected_col = 0

# Track confirmed selections
selected_boxes = []



# Dictionary to store the image filenames and their corresponding numbers and letters
image_info = {
    os.path.abspath("ImageResource/CharacterSelection/Catanjeaux.png"): (1, "A"),
    os.path.abspath("ImageResource/CharacterSelection/Selee.png"): (2, "B"),
    os.path.abspath("ImageResource/CharacterSelection/Irises.png"): (3, "C"),
    os.path.abspath("ImageResource/CharacterSelection/Onimaru.png"): (4, "D")
}

# Load images based on the provided filenames
images = []
for filename in image_info.keys():
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image, (BOX_SIZE, BOX_SIZE))  # Scale the images to fit the boxes
    images.append(image)

# List of image filenames (to maintain order)
image_filenames = list(image_info.keys())

def create_grid():
    selected_row = 0
    selected_col = 0
    selected_boxes = []
    """Create a grid of boxes at the bottom of the screen."""
    global grid
    grid = []
    for row in range(rows):
        row_list = []
        for col in range(cols):
            # Calculate position of each box
            x = col * (BOX_SIZE + PADDING) + (SCREEN_WIDTH - cols * (BOX_SIZE + PADDING)) // 2
            y = SCREEN_HEIGHT - (rows - row) * (BOX_SIZE + PADDING) - BOX_SIZE
            rect = pygame.Rect(x, y, BOX_SIZE, BOX_SIZE)
            row_list.append(rect)
        grid.append(row_list)

def draw_grid(selected_row, selected_col):
    """Draw the grid, highlight the selected box, and place images in the boxes."""
    for row in range(rows):
        for col in range(cols):
            rect = grid[row][col]

            # Determine the index of the image for the current box (0-3)
            image_index = col

            # Check if the box is confirmed as selected (draw it green)
            if [row, col] in selected_boxes:
                pygame.draw.rect(screen, GREEN, rect)

            # Draw the blue highlight box (bigger than the gray box) for the current selection
            if row == selected_row and col == selected_col:
                highlight_rect = rect.inflate(HIGHLIGHT_SIZE_INCREASE, HIGHLIGHT_SIZE_INCREASE)
                pygame.draw.rect(screen, BLUE, highlight_rect)

            # Draw the gray box on top of the blue highlight
            pygame.draw.rect(screen, GRAY, rect)
            pygame.draw.rect(screen, WHITE, rect, 3)  # Draw the white box border

            # Place the image in the box
            image_rect = images[image_index].get_rect(center=rect.center)
            screen.blit(images[image_index], image_rect)

def move_selection(direction,selected_row,selected_col):
    """Move the selected box within the grid."""
    if direction == 'up' and selected_row > 0:
        selected_row -= 1
    elif direction == 'down' and selected_row < rows - 1:
        selected_row += 1
    elif direction == 'left' and selected_col > 0:
        selected_col -= 1
    elif direction == 'right' and selected_col < cols - 1:
        selected_col += 1

def serve_multiple_games():
    # Track how many selections have been made
    selection_count = 0
    # Variables to store selected picture information (filename, number, letter)
    selected_info_1 = ("", 0, "")  # (filename, number, letter)
    selected_info_2 = ("", 0, "")  # (filename, number, letter)
    selected_boxes = []
    selected_row = 0
    selected_col = 0

    LocalBrightness = GlobalVar.Brightness
    Single_Player_background = pygame.image.load(os.path.abspath(
        "ImageResource/MultipleSelection.png"))
    Single_Player_background_bright = GlobalVar.apply_brightness(Single_Player_background, LocalBrightness * 0.5)
    # Initialize the grid
    create_grid()
    selection_count = 0
    # Main game loop
    running = True
    character = 'Catanjeaux'
    while running and GlobalVar.STATUS=="Multiple Selection":
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEBUTTONDOWN and GlobalVar.STATUS == "Multiple Selection":
            #     GlobalVar.STATUS = "Main"
            #     break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and selected_row > 0:
                    selected_row-=1

                elif event.key == pygame.K_a and selected_col > 0:
                    filename = image_filenames[selected_col]

                    character = filename.split('.png', 1)[0].split('CharacterSelection/')[1]
                    if selected_col > 0:
                        selected_col -= 1
                elif event.key == pygame.K_s:
                    filename = image_filenames[selected_col]
                    character = filename.split('.png', 1)[0].split('CharacterSelection/')[1]
                    if selected_row < rows - 1:
                        selected_row += 1

                elif event.key == pygame.K_d:
                    filename = image_filenames[selected_col]
                    character = filename.split('.png', 1)[0].split('CharacterSelection/')[1]
                    if selected_col < cols - 1:
                        selected_col += 1

                elif event.key == pygame.K_RETURN:  # Press Enter to confirm the selection
                    # Calculate the image index of the selected box (0 to 3)
                    image_index = selected_col  # Col determines which image is in the box
                    filename = image_filenames[image_index]
                    number, letter = image_info[filename]
                    print("Unique" + filename)

                    if [selected_row, selected_col] not in selected_boxes:
                        print("被清了嘛？")
                        selected_boxes.append([selected_row, selected_col])  # Add current selection to confirmed list
                        selection_count += 1  # Increment the selection count

                        # Assign to selected_info_1 for the first selection and selected_info_2 for the second selection
                        if selection_count == 1:
                            selected_info_1 = (filename, number, letter)
                            print(
                                f"First Selection: {selected_info_1[0]}, Number: {selected_info_1[1]}, Letter: {selected_info_1[2]}")
                            GlobalVar.selectedf1=selected_info_1[0].split('.png',1)[0].split("CharacterSelection/")[1]+"_player1"
                        elif selection_count == 2:
                            selected_info_2 = (filename, number, letter)
                            print(
                                f"Second Selection: {selected_info_2[0]}, Number: {selected_info_2[1]}, Letter: {selected_info_2[2]}")
                            GlobalVar.selectedf2 = selected_info_2[0].split('.png', 1)[0].split("CharacterSelection/")[1] + "_player2"
                            GlobalVar.STATUS="Map"  # End the program after two selections
                            Map_Selection.Serve_MapSelection()
                            break
        # Draw the grid with the current selection
        print([selected_row,selected_col])
        draw_grid(selected_row,selected_col)
        regulate_image = pygame.transform.scale(Single_Player_background_bright, (Image_width, Image_height * 0.7))

        # Update the display
        screen.blit(regulate_image, (0, 0))
        x = 0
        if character == 'Catanjeaux':
            text_info = "Catanjeaux:\nTentacle Attack\nFire Laser\nGround Slam\nConcussive Attack\nFighting Style: Strong\nBackstory: The evil god from the distant past is spreading His ravings to His followers"
            lines_info = text_info.split('\n')
        elif character == 'Selee':
            text_info = "Selee:\nPunch Forward\nFireball\nTornado\nLightning\nFighting Style: Basic\nBackstory: Selee is a wizard from the continent of Valerian."
            lines_info = text_info.split('\n')
        elif character == 'Irises':
            text_info = "Irises:\nreleases a ball of wind\nFighting Style: Swings a sword\nBackstory: Iris is a swordsman from the House of the Irises."
            lines_info = text_info.split('\n')
        else:
            text_info = "Onimaru:\nAbilities: *insert abilities*\nFighting Style: Sword\nBackstory: Onimaru is the last survivor of a clan of wind-wielding swordsmen, now wandering the world seeking justice for his fallen family."
            lines_info = text_info.split('\n')
        for info in lines_info:
            character_info = font.render(info, True, WHITE)
            info_rect = character_info.get_rect(center=(SCREEN_WIDTH // 6, SCREEN_HEIGHT // 4 + x))
            stroke_rect = info_rect.inflate(5, 5)
            pygame.draw.rect(screen, (0, 0, 0), stroke_rect)
            x += 40
            screen.blit(character_info, info_rect)
        # Update the Label of single player
        # screen.blit(Label_image_surface, Label_rect)
        # Update the display
        pygame.display.flip()