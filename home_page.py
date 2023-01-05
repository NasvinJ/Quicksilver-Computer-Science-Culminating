#imports pygame, the 2 tests, buttons file, and more
import pygame,sys
from tkinter import *
from button import Button
from pygame import display, event
import game1_speed_typing_test
import game2_internet_speed_test
import time

#Grabs color for the text in console
color_off="\033[0m"
red = "\033[0;31m"
blue = "\033[0;34m"
black="\033[0;30m"
yellow="\033[0;33m"

def get_font(size):  # Returns Press-Start-2P in the desired size
  return pygame.font.Font("assets/font.ttf", size)
pygame.init()

def home_screen_gui():
  infoObject = pygame.display.Info()

  #create the display surface to grab the size of the pygame screen
  screen = pygame.display.set_mode((infoObject.current_w * 1.5, infoObject.current_h * 2))
  display.set_caption("Quicksilver Home Page")

  def pushImage(Quicksilver_Main_BG,Background):
    #create the window with the title given
    pygame.display.set_caption(Quicksilver_Main_BG) 
  
    #convert the file to a png for pygame to use
    image = pygame.image.load(quicksilver_main_bg.jpg)#.convert()
  
    #scale the image to the pygame window size
    image =pygame.transform.scale("quicksilver_main_bg.jpg", (infoObject.current_w, infoObject.current_h))
  
    #push the image out to the pygame screen
    screen.blit("quicksilver_main_bg.jpg", (infoObject.current_w, infoObject.current_h))

  bg=pygame.image.load("quicksilver_main_bg.jpg")

  screen.blit(bg, (0, 0))
  
  display.flip()

  #Creates the secondary page in a function
  def game_screen():
    while True:
      screen = pygame.display.set_mode((infoObject.current_w * 1.4, infoObject.current_h / 1.1))
      #The window's caption is Game Screen
      display.set_caption("Game Screen")
      options_mouse_pos = pygame.mouse.get_pos()
      #Background color set to dark gray
      screen.fill("dark gray")
      #Intializes font
      hey_font = pygame.font.Font("assets/font.ttf", 30)
      #Uses the font variable to create the title in black and centered positioned
      options_text =hey_font.render("Pick a Speed Test!", True,
                                         "Black")
      options_rect = options_text.get_rect(center=(355, 70))
      screen.blit(options_text, options_rect)

      #Creates the button on the top right corner which appears as "Back." Main color is blue while when you hover it changes to green
      options_back = Button(image=None,
                      pos=(600, 40),
                      text_input="BACK",
                      font=get_font(45),
                      base_color="Blue",
                      hovering_color="Green")

      options_back.changeColor(options_mouse_pos)
      options_back.update(screen)

      #When you click on the back button, it runs the run_test function to go back to the main home page
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if options_back.checkForInput(options_mouse_pos):
                run_test()

        #Creates the Typing Speed Test button as the first game, which is in white and when hovered on turns black
        typing_test_button = Button(image=None,
                        pos=(155, 200),
                        text_input="Typing Speed Test",
                        font=get_font(24),
                        base_color="White",
                        hovering_color="Black")

        typing_test_button.changeColor(options_mouse_pos)
        typing_test_button.update(screen)

        #When you click on the first game button, it runs the function to play the game
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if typing_test_button.checkForInput(options_mouse_pos):
                  game1_speed_typing_test.speed_typing_gui_screen()

        #Creates the Internet Speed Test button
        internet_test_button = Button(image=None,
                pos=(500, 200),
                text_input="Internet Speed Test",
                font=get_font(24),
                base_color="White",
                hovering_color="Black")

        internet_test_button.changeColor(options_mouse_pos)
        internet_test_button.update(screen)

        #Runs the second game when you click on the button
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if internet_test_button.checkForInput(options_mouse_pos):
                  game2_internet_speed_test.internet_speed_gui_screen()
      
      pygame.display.update()

  #Creates the home screen
  def run_test():
    while True:
      screen.blit(bg, (0, 0))
      menu_mouse_pos = pygame.mouse.get_pos()
      #Creates the font and rectangles to use as variables
      menu_text = get_font(100).render("", True, "#b68f40")
      menu_rect = menu_text.get_rect(center=(640, 100))

      #Creates the main button which uses the rectangle image
      options_button = Button(
      image=pygame.image.load("assets/Options_Rect.png"),
      pos=(380, 230),
      text_input="Run Test",
      font=get_font(60),
      base_color="#d7fcd4",
      hovering_color="White")
      
      screen.blit(menu_text, menu_rect)
  
      for button in [options_button]:
        button.changeColor(menu_mouse_pos)
        button.update(screen)

      #Click on the main button takes you to the secondary page for the games to choose from
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if options_button.checkForInput(menu_mouse_pos):
                  game_screen()

      #There is an information icon image on the right bottom
      info_button = Button(
      image=pygame.image.load("info_icon.png"),
      pos=(665, 410),
      text_input="",
      font=get_font(60),
      base_color="#d7fcd4",
      hovering_color="White")
      
      for button in [info_button]:
        button.changeColor(menu_mouse_pos)
        button.update(screen)

      #When you click on the information icon, it prints out the instructions through the console
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if info_button.checkForInput(menu_mouse_pos):
                #Prints out instructions on console and use the color variables to change from different colors. It waits 30 seconds before the console clears
                print(yellow + "Instructions")
                print()
                print(red + "Game 1: Speed Typing Test")
                print("To start the timer, click on the input field on the screen each time. Then type out the text shown above the input field and click enter to finish. There will be statistics shown on time, accuracy, and wpm. There will be a corresponding image on the left corner for your speed. You may reset and try again as much as you want by click on the reset button on the bottom middle!")
                print()
                print(blue + "Game 2: Internet Speed Test")
                print("Brought to you by Quicksilver Incorporation (with copyright laws), there will be 3 buttons which can test your device's speed. By click on the corresponding button, you may test your download speed, upload speed, and ping. May your device be worthy!😈😈😈")
                time.sleep(30)
                print("\033[H\033[J")

      pygame.display.update()

  run_test()