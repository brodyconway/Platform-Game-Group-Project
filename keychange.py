import os.path
import sys
from PIL import Image
import pygame
import GlobalVar
import Setting

# Initialize Pygame
pygame.init()

# Set up screen dimensions (height and width)
screen_width = int(pygame.display.get_desktop_sizes()[0][0]*0.63)
screen_height = int(pygame.display.get_desktop_sizes()[0][1]*0.66)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sugar World')  # name of the game

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
BOX_COLOR = (50, 50, 50)

# Set up FPS (frames per second)
clock = pygame.time.Clock()
FPS = 60

# Convert icon to surface
Icon = Image.open(os.path.abspath("ImageResource/Selee menu.png"))
surfaceIco = pygame.image.fromstring(Icon.tobytes(), Icon.size, Icon.mode)
pygame.display.set_icon(surfaceIco)

# Define fonts
font = pygame.font.SysFont(None, 40)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, (x, y))

def draw_text_with_box(text, font, text_color, box_color, surface, x, y, box_padding=10):
    text_obj = font.render(text, True, text_color)
    text_rect = text_obj.get_rect()

    # Draw the box with padding around the text
    box_rect = pygame.Rect(text_rect.x - box_padding // 2, text_rect.y - box_padding // 2,
                           text_rect.width + box_padding, text_rect.height + box_padding)
    box_rect.topleft = (x, y)
    pygame.draw.rect(surface, box_color, box_rect)  # Draw the background box

    # Blit the text onto the surface
    surface.blit(text_obj, (x, y))
    return box_rect

def draw_popup(text,text2):
    # Popup box dimensions
    popup_width = screen_width//2
    popup_height = screen_width//5
    popup_x = (screen.get_width() - popup_width) // 2
    popup_y = (screen.get_height() - popup_height) // 2
    # Draw the box background
    pygame.draw.rect(screen, GRAY, (popup_x, popup_y, popup_width, popup_height))
    # Draw the border
    pygame.draw.rect(screen, WHITE, (popup_x, popup_y, popup_width, popup_height), 3)
    # Draw the text
    draw_text(text, font, WHITE, screen, popup_x + popup_x//2, popup_y + popup_y//3)
    draw_text(text2, font, WHITE, screen, popup_x + popup_x//9, popup_y + popup_y//2)


# Main loop
def keychange():
    LocalSTATUS=GlobalVar.STATUS
    # Initial key bindings
    key_bindings = GlobalVar.keys
    # Track if we are changing a key
    changing_key = None
    show_popup = False
    running=True
    # Back button dimensions
    back_button_text = "Back"
    back_button_width = 150
    back_button_height = 50
    back_button_x = screen_width - back_button_width - 10  # 10px padding from the right
    back_button_y = screen_height - back_button_height - 10  # 10px padding from the bottom

    while running and LocalSTATUS=="AdjustControl":
        screen.fill(BLACK)
        # Draw key bindings for Player 1 and Player 2
        draw_text("Player 1 Key Bindings", font, WHITE, screen, screen_width*0.1, screen_height*0.1)
        draw_text("Player 2 Key Bindings", font, WHITE, screen, screen_width*0.6, screen_height*0.1)

        # Player 1 key bindings
        draw_text("Jump:", font, WHITE, screen, screen_width*0.1, screen_height*0.25)
        p1_jump_key_box = draw_text_with_box(pygame.key.name(key_bindings["player1"]["jump"]), font, WHITE, BOX_COLOR,
                                             screen, screen_width*0.35, screen_height*0.25)

        draw_text("Move Left:", font, WHITE, screen, screen_width*0.1, screen_height*0.35)
        p1_move_left_key_box = draw_text_with_box(pygame.key.name(key_bindings["player1"]["move_left"]), font, WHITE,
                                                  BOX_COLOR, screen, screen_width*0.35, screen_height*0.35)

        draw_text("Move Right:", font, WHITE, screen, screen_width*0.1, screen_height*0.45)
        p1_move_right_key_box = draw_text_with_box(pygame.key.name(key_bindings["player1"]["move_right"]), font, WHITE,
                                                   BOX_COLOR, screen, screen_width*0.35, screen_height*0.45)

        draw_text("Attack:", font, WHITE, screen, screen_width*0.1, screen_height*0.55)
        p1_attack_key_box = draw_text_with_box(pygame.key.name(key_bindings["player1"]["attack"]), font, WHITE,
                                               BOX_COLOR, screen, screen_width*0.35, screen_height*0.55)

        draw_text("Ability:", font, WHITE, screen, screen_width*0.1, screen_height*0.65)
        p1_ability_key_box = draw_text_with_box(pygame.key.name(key_bindings["player1"]["ability"]), font, WHITE,
                                               BOX_COLOR, screen, screen_width*0.35, screen_height*0.65)
        draw_text("Defend:", font, WHITE, screen, screen_width * 0.1, screen_height * 0.75)
        p1_defend_key_box = draw_text_with_box(pygame.key.name(key_bindings["player1"]["defend"]), font, WHITE,
                                                BOX_COLOR, screen, screen_width * 0.35, screen_height * 0.75)

        # Player 2 key bindings
        draw_text("Jump:", font, WHITE, screen, screen_width*0.6, screen_height*0.25)
        p2_move_jump_key_box = draw_text_with_box(pygame.key.name(key_bindings["player2"]["jump"]), font, WHITE,
                                                  BOX_COLOR, screen, screen_width*0.85, screen_height*0.25)

        draw_text("Move Left:", font, WHITE, screen, screen_width*0.6, screen_height*0.35)
        p2_move_left_key_box = draw_text_with_box(pygame.key.name(key_bindings["player2"]["move_left"]), font, WHITE,
                                                  BOX_COLOR, screen, screen_width*0.85, screen_height*0.35)

        draw_text("Move Right:", font, WHITE, screen, screen_width*0.6, screen_height*0.45)
        p2_move_right_key_box = draw_text_with_box(pygame.key.name(key_bindings["player2"]["move_right"]), font, WHITE,
                                                   BOX_COLOR, screen, screen_width*0.85, screen_height*0.45)

        draw_text("Attack:", font, WHITE, screen, screen_width*0.6, screen_height*0.55)
        p2_attack_key_box = draw_text_with_box(pygame.key.name(key_bindings["player2"]["attack"]), font, WHITE,
                                               BOX_COLOR, screen, screen_width*0.85, screen_height*0.55)

        draw_text("Ability:", font, WHITE, screen, screen_width*0.6, screen_height*0.65)
        p2_ability_key_box = draw_text_with_box(pygame.key.name(key_bindings["player2"]["ability"]), font, WHITE,
                                               BOX_COLOR, screen, screen_width*0.85, screen_height*0.65)

        draw_text("Defend:", font, WHITE, screen, screen_width * 0.6, screen_height * 0.75)
        p2_defend_key_box = draw_text_with_box(pygame.key.name(key_bindings["player2"]["defend"]), font, WHITE,
                                                BOX_COLOR, screen, screen_width * 0.85, screen_height * 0.75)

        # Draw the Back button
        pygame.draw.rect(screen, GRAY, (back_button_x, back_button_y, back_button_width, back_button_height))
        pygame.draw.rect(screen, WHITE, (back_button_x, back_button_y, back_button_width, back_button_height), 2)
        draw_text(back_button_text, font, WHITE, screen, back_button_x + 30, back_button_y + 10)

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for mouse click on key boxes
            if event.type == pygame.MOUSEBUTTONDOWN and not show_popup:
                mouse_pos = pygame.mouse.get_pos()
                #check if back button is clicked
                if back_button_x <= mouse_pos[0] <= back_button_x + back_button_width and back_button_y <= mouse_pos[
                    1] <= back_button_y + back_button_height:
                    LocalSTATUS = "Setting"
                    GlobalVar.STATUS="Setting"
                    GlobalVar.Setting_count+=1
                    try:
                        break
                    finally:
                        Setting.Serve_Setting()
                # Check if any key binding box is clicked
                if p1_jump_key_box.collidepoint(mouse_pos):
                    changing_key = ("player1", "jump")
                    show_popup = True
                elif p1_move_left_key_box.collidepoint(mouse_pos):
                    changing_key = ("player1", "move_left")
                    show_popup = True
                elif p1_move_right_key_box.collidepoint(mouse_pos):
                    changing_key = ("player1", "move_right")
                    show_popup = True
                elif p1_attack_key_box.collidepoint(mouse_pos):
                    changing_key = ("player1", "attack")
                    show_popup = True
                elif p1_ability_key_box.collidepoint(mouse_pos):
                    changing_key = ("player1", "ability")
                    show_popup = True
                elif p1_ability_key_box.collidepoint(mouse_pos):
                    changing_key = ("player1", "ability")
                    show_popup = True
                elif p1_defend_key_box.collidepoint(mouse_pos):
                    changing_key = ("player1", "defend")
                    show_popup = True
                elif p2_move_jump_key_box.collidepoint(mouse_pos):
                    changing_key = ("player2", "jump")
                    show_popup = True
                elif p2_move_left_key_box.collidepoint(mouse_pos):
                    changing_key = ("player2", "move_left")
                    show_popup = True
                elif p2_move_right_key_box.collidepoint(mouse_pos):
                    changing_key = ("player2", "move_right")
                    show_popup = True
                elif p2_attack_key_box.collidepoint(mouse_pos):
                    changing_key = ("player2", "attack")
                    show_popup = True
                elif p2_ability_key_box.collidepoint(mouse_pos):
                    changing_key = ("player2", "ability")
                    show_popup = True
                elif p2_defend_key_box.collidepoint(mouse_pos):
                    changing_key = ("player2", "defend")
                    show_popup = True


            # If waiting for a key press after clicking a box
            if event.type == pygame.KEYDOWN and changing_key:
                dupkey=False
                if event.key not in GlobalVar.keys.get("player1").values() and event.key not in GlobalVar.keys.get("player2").values():
                    dupkey=False
                else:
                    dupkey=True
                if dupkey==False:
                    player, action = changing_key
                    print(player)
                    print(action)
                    print(GlobalVar.keys[player][action])
                    GlobalVar.keys[player][action] = event.key
                    print("wait")
                    print(GlobalVar.keys[player][action])
                    changing_key = None  # Reset after key is pressed
                    show_popup = False  # Hide popup after key is pressed

        # Show the popup box if we're waiting for the user to press a new key
        if show_popup:
            draw_popup("Press a new key","Please don't enter the same key")

        # Update the display
        pygame.display.flip()
        pygame.display.update()
