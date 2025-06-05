import os.path
import pygame
import sys
from PIL import Image
import pygame
import button
import GlobalVar
import Multiple_Players
import Setting
import Mode_Selection
import control


# Initialize Pygame
pygame.init()

# Set up screen dimensions(height and width)
screen_width = pygame.display.get_desktop_sizes()[0][0]*0.63
screen_height = pygame.display.get_desktop_sizes()[0][1]*0.66
screen = pygame.display.set_mode((screen_width, screen_height))
GlobalVar.screen_width = screen_width
GlobalVar.screen_height = screen_height
def ret_screen_size():
    return [screen_width, screen_height]

pygame.display.set_caption('Sugar World') #name of the game

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)

#Setting up text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#a Set up FPS (frames per second)
clock = pygame.time.Clock()
FPS = 60

# Player settings for proof for concepts(for now)
player_width = 50
player_height = 50

#Convert image to surface
Icon=Image.open(os.path.abspath("ImageResource/Selee menu.png"))
surfaceIco = pygame.image.fromstring(Icon.tobytes(), Icon.size, Icon.mode)

#set_icon function handle surface parameters (transfer image to surface)
pygame.display.set_icon(surfaceIco)


pygame.mixer.music.load(os.path.abspath("Music/Guitar Man.mp3"))


pygame.mixer.music.play(loops=-1)



# Main game loop
def lanuch():
    running = True
    GlobalVar.Training=False
    GlobalVar.AI =  False
    #Setting up status
    GlobalVar.STATUS="Main"
    while running and GlobalVar.STATUS=="Main":
        GlobalVar.Training = False

        GlobalVar.AI = False

        pygame.mixer.music.set_volume(GlobalVar.Volume)
        # Handle events

        LocalBrightness=GlobalVar.Brightness
        SettingIcon=pygame.image.load(os.path.abspath("ImageResource/SettingIcon.png"))
        SettingIcon=pygame.transform.scale(SettingIcon,(screen_width*0.08,screen_height*0.09))
        SettingIcon_Brigntness=GlobalVar.apply_brightness(SettingIcon,GlobalVar.Brightness*0.5)
        SettingIcon_Brigntness_rect=SettingIcon_Brigntness.get_rect()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if start_game_button.checkForInput(pos):
                    GlobalVar.STATUS = "Mode Selection"
                    Mode_Selection.Serve_ModeSelection()
                    # GlobalVar.STATUS = "Multiple Selection"
                    # Multiple_Players.serve_multiple_games()

                if controls_button.checkForInput(pos):
                    GlobalVar.STATUS = "Control"
                    control.control()
                if exit_button.checkForInput(pos):
                    pygame.quit()
                    sys.exit()
                if SettingIcon_Brigntness_rect.collidepoint(pos):
                    GlobalVar.STATUS = "Setting"
                    GlobalVar.Setting_count+=1
                    Setting.Serve_Setting()

            # Get keys pressed
            keys = pygame.key.get_pressed()
            # Set screen to the main menu background, set background color to white before that.
            LocalBrightness=GlobalVar.Brightness
            Main_Menu_background = pygame.image.load(os.path.abspath("ImageResource/MainMenu.png"))
            Main_Menu_background = pygame.transform.scale(Main_Menu_background, (screen_width, screen_height))
            Main_Menu_background_Brightness = GlobalVar.apply_brightness(Main_Menu_background, LocalBrightness * 0.5)

            # There is some white space exist because the image doesn't fit the ratio of the screen size!
            screen.fill(WHITE)
            screen.blit(Main_Menu_background_Brightness ,(0,0))
            draw_text("Sugar World", pygame.font.SysFont("arial", 60, False, True), PINK, screen_width*0.4, screen_height*0.15)
            start_game_button = button.Button(image=None, pos=(screen_width*0.5,screen_height*0.65), text_input="Start Game", font=pygame.font.SysFont("arialblack", 40), base_color="Yellow", hovering_color="Black")
            button.Button.update(start_game_button, screen)
            controls_button = button.Button(image=None, pos=(screen_width*0.5, screen_height*0.73), text_input="Controls", font=pygame.font.SysFont("arialblack", 40), base_color="Yellow", hovering_color="Black")
            button.Button.update(controls_button, screen)
            exit_button = button.Button(image=None, pos=(screen_width*0.5, screen_height*0.81), text_input="Exit", font=pygame.font.SysFont("arialblack", 40), base_color="Yellow", hovering_color="Black")
            button.Button.update(exit_button, screen)
            screen.blit(SettingIcon_Brigntness,(0,0))
            # settings_button = button.Button(image=None, pos=(screen_width*0.5, screen_height*0.81), text_input="Settings", font=pygame.font.SysFont("arialblack", 40), base_color="Yellow", hovering_color="Black")
            # button.Button.update(settings_button, screen)
            
        # Update the display
        pygame.display.flip()

        # Set the frame rate
        clock.tick(FPS)

if __name__ == '__main__':
    lanuch()
