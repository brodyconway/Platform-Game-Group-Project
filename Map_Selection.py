import os.path
import sys
from PIL import Image
import pygame
import GlobalVar

import battle
import AI
pygame.init()


# Adjust screen size based on desktop size
info = pygame.display.Info()
screen_width = pygame.display.get_desktop_sizes()[0][0]*0.63
screen_height = pygame.display.get_desktop_sizes()[0][1]*0.66
screen = pygame.display.set_mode((int(screen_width), int(screen_height)))


pygame.display.set_caption('Sugar World')  # name of the game


# Define colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)


# Set up FPS (frames per second)
clock = pygame.time.Clock()
FPS = 60


# Set icon
Icon = Image.open(os.path.abspath("ImageResource/Selee menu.png"))
surfaceIco = pygame.image.fromstring(Icon.tobytes(), Icon.size, Icon.mode)


# Display icon
pygame.display.set_icon(surfaceIco)

LocalBrightness=GlobalVar.Brightness
# Load map images
dojo_map = pygame.image.load(os.path.abspath("ImageResource/Maps/battle_map_2.png"))
dojo_map = pygame.transform.scale(dojo_map,(screen_width,screen_height))
dojo_map_brightness=GlobalVar.apply_brightness(dojo_map, LocalBrightness*0.5)

cherry_blossom_map = pygame.image.load(os.path.abspath("ImageResource/Maps/battle_map_1.png"))
cherry_blossom_map = pygame.transform.scale(cherry_blossom_map,(screen_width,screen_height))
cherry_blossom_map_brightness = GlobalVar.apply_brightness(cherry_blossom_map, LocalBrightness*0.5)


map_images = [
    dojo_map_brightness,
    cherry_blossom_map_brightness
]


player1_spawn_point = (screen_width // 4, screen_height)  # Player 1 spawn (left)
player2_spawn_point = (3 * screen_width // 4, screen_height)  # Player 2 spawn (right)


player_size = 30  # Size of the players (for boundary calculations)


# x_min_boundary = 0
# x_max_boundary = screen_width
# y_min_boundary = 0
# y_max_boundary = screen_height


def Serve_MapSelection():
   print("地图启动")
   running = True
   LocalSTATUS = GlobalVar.STATUS
   selected_map_index = 0  # Start with the first map selected

   LocalBrightness = GlobalVar.Brightness
   # Load background image
   background_image = pygame.image.load(os.path.abspath("ImageResource/Maps/background_image.png"))
   background_image = pygame.transform.scale(background_image, (
   int(screen_width), int(screen_height)))  # Resize the background to fit the screen size

   background_image_bright = GlobalVar.apply_brightness(background_image, LocalBrightness * 0.5)

   # Adjust button size based on screen size
   button_width = screen_width // 6
   button_height = screen_height // 4
   button_spacing = screen_width // 50
   start_x = (screen_width - (button_width * len(map_images) + button_spacing * (len(map_images) - 1))) // 2
   y = screen_height - (button_height * 2)  # The y-position for all buttons


   # Create back button
   back_button_width = 150
   back_button_height = 50
   back_button_rect = pygame.Rect(50, 50, back_button_width, back_button_height)


   # Set up Choose Map
   font = pygame.font.Font(None, 36)
   text_surface = font.render("Choose Map", True, WHITE)
   text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 10))  # Position it at the top center


   # Set up Back
   back_font = pygame.font.Font(None, 26)
   back_text_surface = back_font.render("Back", True, WHITE)
   back_text_rect = back_text_surface.get_rect(center=back_button_rect.center)



   maps = {
       0: {
           "image": dojo_map,
           "floor": screen_height - 50,
           "platform": (100, 200),
           "player1 spawn": [screen_width*0.2,screen_height*0.7],
           "player2 spawn": [screen_width*0.71,screen_height*0.7]
       },
       1: {
           "image": cherry_blossom_map,
           "floor": screen_height - 60,
           "platform": (150, 300),
           "player1 spawn": [screen_width*0.2,screen_height*0.7],
           "player2 spawn": [screen_width*0.71,screen_height*0.7]
       }
   }


   # Main loop to handle both map selection and map display
   while running and LocalSTATUS == "Map":
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
               pygame.quit()
               sys.exit()


           elif event.type == pygame.KEYDOWN:
                   # Map selection phase
               if event.key == pygame.K_RIGHT:
                   selected_map_index = (selected_map_index + 1) % len(map_images)  # Navigate right
               elif event.key == pygame.K_LEFT:
                   selected_map_index = (selected_map_index - 1) % len(map_images)  # Navigate left
               elif event.key == pygame.K_RETURN:                        #Get which map is seletive
                   print("start battle")
                   Maps = maps[selected_map_index]["image"]
                   Maps_bright = GlobalVar.apply_brightness(Maps, LocalBrightness*0.5)
                   print(LocalBrightness)
                   print("local")

                   GlobalVar.map = Maps_bright

                   GlobalVar.mapfloor = maps[selected_map_index]["floor"]
                   GlobalVar.player1_spawn_point = maps[selected_map_index]["player1 spawn"]
                   GlobalVar.player2_spawn_point = maps[selected_map_index]["player2 spawn"]

                   GlobalVar.player1_point = 0
                   GlobalVar.player2_point = 0
                   if GlobalVar.AI==True:
                       GlobalVar.STATUS = "AI"
                       LocalSTATUS= "AI"
                       AI.ai()
                   else:
                       GlobalVar.STATUS = "Battle"
                       LocalSTATUS = "Battle"
                       battle.battle()
                       break
               # elif event.key == pygame.K_ESCAPE:
               #     LocalSTATUS = "SinglePlayer"
               #     GlobalVar.STATUS = "SinglePlayer"
               #     Single_Player.Serve_Single_Player()
               #     return  # Exit to single player


       # Map selection phase
       screen.blit(background_image_bright, (0, 0))


       # Load Choose Map text
       screen.blit(text_surface, text_rect)


       # Draw Back Button
       pygame.draw.rect(screen, RED, back_button_rect)
       screen.blit(back_text_surface, back_text_rect)


       # Draw map selection buttons as images
       for idx in range(len(map_images)):
           x = start_x + (button_width + button_spacing) * idx
           button_image = pygame.transform.scale(map_images[idx], (button_width, button_height))
           screen.blit(button_image, (x, y))


           # Highlight the selected map
           if idx == selected_map_index:
               pygame.draw.rect(screen, RED, (x, y, button_width, button_height), 3)




       pygame.display.flip()
       clock.tick(FPS)


