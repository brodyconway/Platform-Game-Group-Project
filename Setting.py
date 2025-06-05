import os.path
import sys
from PIL import Image
import pygame
import GlobalVar
import button
import numpy as np
import keychange

# Initialize Pygame
pygame.init()

# Set up screen dimensions(height and width)
screen_width = int(pygame.display.get_desktop_sizes()[0][0]*0.63)
screen_height = int(pygame.display.get_desktop_sizes()[0][1]*0.66)

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Sugar World') #name of the game

# Define colors

# Set up FPS (frames per second)
clock = pygame.time.Clock()
FPS = 60
slider_width = screen_width * 0.125  # Width of the slider bar
slider_height = screen_height * 0.015  # Height of the slider bar
handle_radius = slider_height  # Radius of the draggable handle

def Serve_Setting():
    mutepos = int(screen_width / 2.05)
    LocalSTATUS=GlobalVar.STATUS
    Localvol = GlobalVar.Volume
    Localse = GlobalVar.SoundEffect
    LocalBrightness = GlobalVar.Brightness
    dragging = False  # Whether the handle is being dragged or not

    font = pygame.font.SysFont('Arial', 40)
    back = font.render("Back", True, GlobalVar.YELLOW)
    backrect=back.get_rect()
    backrect.center=(screen_width//1.1, screen_height//10)

    adjustControltext=font.render("Adjust Controls", True, GlobalVar.BLUE)
    controlrect = adjustControltext.get_rect()
    controlrect.center=(screen_width//3.3, screen_height//1.75)

    volumetext=font.render("Volume", True, GlobalVar.BLACK)
    volumetextrect=volumetext.get_rect()
    volumetextrect.center = (screen_width // 2, screen_height / 3.0)

    soundeffecttext = font.render("Sound Effect", True, GlobalVar.BLACK)
    soundeffectrect = soundeffecttext.get_rect()
    soundeffectrect.center = (screen_width // 2, screen_height / 2.0)

    brighnesstext = font.render("Brightness", True, GlobalVar.BLACK)
    brighnessrect = brighnesstext.get_rect()
    brighnessrect.center = (screen_width // 2, screen_height / 1.5)

    mutetext= font.render("Mute", True, GlobalVar.BLACK)
    muterect = mutetext.get_rect()
    muterect.center = (screen_width // 2, screen_height / 1.2)
    if GlobalVar.Setting_count==1:
        postionVolumebar=[int(screen_width//2.3)+slider_width,int(screen_height//2.5)]
        postionsoundeffectbar = [int(screen_width//2.3)+slider_width, int(screen_height // 1.75)]
        postionBrightness = [int(screen_width//2.3)+slider_width, int(screen_height // 1.35)]
        #mutepos=[int(screen_width//2.3)+slider_width]
        GlobalVar.Setting_count+=1
    else:
         postionVolumebar = GlobalVar.postionVolumebarX
         postionsoundeffectbar = GlobalVar.postionsoundeffectbarX
         postionBrightness = GlobalVar.postionBrightnessX
         postionVolumebar = [postionVolumebar, int(screen_height // 2.5)]
         postionsoundeffectbar = [postionsoundeffectbar, int(screen_height // 1.75)]
         postionBrightness = [postionBrightness, int(screen_height // 1.35)]
         #mutepos = [GlobalVar.mutebuttonX + slider_width]
    running = True

    while running and (LocalSTATUS=="Setting" or GlobalVar.Disconnect):
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #check mouse click and back to MainMenu
            if event.type==pygame.MOUSEBUTTONDOWN:

                mouse_pos= pygame.mouse.get_pos()
                if backrect.collidepoint(mouse_pos) and LocalSTATUS!="Main":
                    GlobalVar.STATUS="Main"
                    LocalSTATUS = "Main"
                    GlobalVar.postionVolumebarX=postionVolumebar[0]
                    GlobalVar.postionsoundeffectbarX = postionsoundeffectbar[0]
                    GlobalVar.postionBrightnessX = postionBrightness[0]
                    GlobalVar.mutebuttonX = mutepos
                if controlrect.collidepoint(mouse_pos) and LocalSTATUS=="Setting":
                    GlobalVar.STATUS = "AdjustControl"
                    LocalSTATUS = "AdjustControl"
                    GlobalVar.postionVolumebarX = postionVolumebar[0]
                    GlobalVar.postionsoundeffectbarX = postionsoundeffectbar[0]
                    GlobalVar.postionBrightnessX = postionBrightness[0]
                    GlobalVar.mutebuttonX=mutepos
                    keychange.keychange()
                dragging = True
                volbar = (int(screen_width // 2.3) <= mouse_pos[0] <= int(screen_width // 2.3) + slider_width*1.1 and int(
                    screen_height // 2.5) - slider_height*1.5 <= mouse_pos[1] <= int(screen_height // 2.5) + slider_height)
                sebar = (int(screen_width // 2.3) <= mouse_pos[0] <= int(screen_width // 2.3) + slider_width*1.1 and int(
                    screen_height // 1.75) - slider_height <= mouse_pos[1] <= int(screen_height // 1.75) + slider_height)
                brightbar = (int(screen_width // 2.3) <= mouse_pos[0] <= int(screen_width // 2.3) + slider_width*1.1 and int(
                    screen_height // 1.35) - slider_height*2 <= mouse_pos[1] <= int(screen_height // 1.35) + slider_height*2)
                #mutebutton=(int(screen_width // 2.05) <= mouse_pos[0] <= int(screen_width // 2.05) + slider_width*1.1 and int(
                #    screen_height // 1.15) - slider_height*2 <= mouse_pos[1] <= int(screen_height // 1.15) + slider_height*2)

                #if mutebutton and mutepos<int(screen_width / 2.05)+slider_width//5:
                #    mutepos+=slider_width//5
                #elif mutepos>=int(screen_width / 2.05+slider_width//5):
                #     mutepos -= slider_width // 5
                if volbar and dragging:
                    postionVolumebar[0]=mouse_pos[0]
                    pygame.draw.circle(screen, GlobalVar.BLUE,
                                   (mouse_pos[0], postionVolumebar[1]),
                                   handle_radius)
                    pygame.display.flip()
                elif sebar and dragging:
                    postionsoundeffectbar[0] = mouse_pos[0]
                    pygame.draw.circle(screen, GlobalVar.BLUE,
                                       (mouse_pos[0], postionsoundeffectbar[1]),
                                       handle_radius)
                    pygame.display.flip()
                elif brightbar and dragging:
                    postionBrightness[0] = mouse_pos[0]
                    pygame.draw.circle(screen, GlobalVar.BLUE,
                                       (mouse_pos[0], postionBrightness[1]),
                                       handle_radius)
                    pygame.display.flip()
            # Mouse button up event
            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False


        if dragging and volbar:
            mouse_pos= pygame.mouse.get_pos()
            # Update handle position, but keep it within the slider bar limits
            postionVolumebar[0] = max(int(screen_width//2.3), min(mouse_pos[0], int(screen_width//2.3) + slider_width))
        elif dragging and sebar:
            mouse_pos = pygame.mouse.get_pos()
            postionsoundeffectbar[0]=max(int(screen_width//2.3), min(mouse_pos[0], int(screen_width//2.3) + slider_width))
        elif dragging and brightbar:
            mouse_pos = pygame.mouse.get_pos()
            postionBrightness[0]=max(int(screen_width//2.3), min(mouse_pos[0], int(screen_width//2.3) + slider_width))

        Setting_background = pygame.image.load(os.path.abspath("ImageResource/setting_background.png"))
        # Adjust size of the image and change it to surface
        Setting_background = pygame.transform.scale(Setting_background, (screen_width, screen_height))
        Setting_background_Brightness = GlobalVar.apply_brightness(Setting_background, LocalBrightness*0.5)

        screen.fill(GlobalVar.WHITE)
        screen.blit(Setting_background_Brightness, (0,0))
        screen.blit(back, backrect)
        screen.blit(volumetext, volumetextrect)
        screen.blit(soundeffecttext, soundeffectrect)
        screen.blit(brighnesstext,brighnessrect)
        screen.blit(adjustControltext,controlrect)
        #screen.blit(mutetext,muterect)

        pygame.draw.rect(screen, GlobalVar.WHITE,
                         (int(screen_width / 2.3), postionVolumebar[1], slider_width, slider_height))
        pygame.draw.circle(screen, GlobalVar.BLUE, (postionVolumebar[0], postionVolumebar[1] + slider_height // 2),
                           handle_radius)
        pygame.draw.rect(screen, GlobalVar.WHITE,
                         (int(screen_width / 2.3), postionsoundeffectbar[1], slider_width, slider_height))
        pygame.draw.circle(screen, GlobalVar.BLUE,
                           (postionsoundeffectbar[0], postionsoundeffectbar[1] + slider_height // 2), handle_radius)
        pygame.draw.rect(screen, GlobalVar.WHITE,
                         (int(screen_width / 2.3), int(screen_height / 1.35), slider_width, slider_height))
        pygame.draw.circle(screen, GlobalVar.BLUE, (postionBrightness[0], postionBrightness[1] + slider_height // 2),
                           handle_radius)

        #pygame.draw.rect(screen, GlobalVar.WHITE,(int(screen_width / 2.05), int(screen_height / 1.15), slider_width//5, slider_height))
        #pygame.draw.circle(screen, GlobalVar.BLUE, (mutepos, int(screen_height / 1.15 + slider_height // 2)),handle_radius)
        Localvol = round((postionVolumebar[0] - int(screen_width // 2.3)) / slider_width,2)
        GlobalVar.Volume = Localvol
        pygame.mixer.music.set_volume(GlobalVar.Volume)
        Localse =round((postionsoundeffectbar[0] - int(screen_width // 2.3)) / slider_width, 2)
        GlobalVar.SoundEffect = Localse
        LocalBrightness = round((postionBrightness[0] - int(screen_width // 2.3)) / slider_width, 2) + 1.0
        GlobalVar.Brightness = LocalBrightness
        #print(GlobalVar.Brightness)
        # Update the display
        pygame.display.flip()

        # Set the frame rate
        clock.tick(FPS)


Serve_Setting()