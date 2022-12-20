#Name: Kenneth Ly and Nasvin.J
#Date:November 28, 2022
#Program Name: Main Database
#Purpose: Database for collect people going to the movie theatre
import pygame, sys
from button import Button
from pygame.locals import *
#Initialize all pygame functionality
pygame.init() 

#grab elements from the pygame interface
infoObject = pygame.display.Info()

#create the display surface to grab the size of the pygame screen
SCREEN = pygame.display.set_mode((infoObject.current_w * 2, infoObject.current_h * 2))

def pushImage(Among_Us,Background):
  #create the window with the title given
  pygame.display.set_caption(Among_Us) 

  #convert the file to a png for pygame to use
  image = pygame.image.load(quicksilver_main_bg.jpg)#.convert()

  #scale the image to the pygame window size
  image =pygame.transform.scale("quicksilver_main_bg.jpg", (infoObject.current_w, infoObject.current_h))

  #push the image out to the pygame screen
  SCREEN.blit("quicksilver_main_bg.jpg", (infoObject.current_w, infoObject.current_h))

BG=pygame.image.load("quicksilver_main_bg.jpg")

#Font Size
def get_font(size):  
  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)
#Adds a customer button that is on the output. When clicked it brings to the console. 
def main_menu():
      while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #Creates rectangular box behind rectangle that is positioned
        MENU_TEXT = get_font(100).render("", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        #Creates the white clickable button titled "customer"
        CUSTOMER_BUTTON = Button(
            image=pygame.image.load("assets/Options Rect.png"),
            pos=(640, 500),
            text_input="Customer",
            font=get_font(60),
            base_color="#d7fcd4",
            hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [CUSTOMER_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        #When user clicks on customer button, it redirects them to the console and runs sql_tickets as the sql part
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CUSTOMER_BUTTON.checkForInput(MENU_MOUSE_POS):
                  sql_tickets.main_program()

        pygame.display.update()

main_menu()