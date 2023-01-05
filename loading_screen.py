#imports pygame and other modules
import pygame,sys,time
from pygame import display, event, draw
import random
import os

def loading_screen_gui():
  pygame.init()
  infoObject = pygame.display.Info()

  #create the display surface to grab the size of the pygame screen
  screen = pygame.display.set_mode((infoObject.current_w * 1.5, infoObject.current_h * 2))
  display.set_caption("Loading Screen")

  def pushImage(Quicksilver_Loading_BG,Background):
    #create the window with the title given
    pygame.display.set_caption(Quicksilver_Loading_BG) 
  
    #convert the file to a png for pygame to use
    image = pygame.image.load(quicksilver_static.jpg)#.convert()
  
    #scale the image to the pygame window size
    image =pygame.transform.scale("quicksilver_static.jpg", (infoObject.current_w, infoObject.current_h))
  
    #push the image out to the pygame screen
    screen.blit("quicksilver_static.jpg", (infoObject.current_w, infoObject.current_h))

  BG=pygame.image.load("quicksilver_static.jpg")

  #Colors variables uses RGB to create 3 colors (red, yellow, and blue) with x and y coordinates for the rectangles
  colors = [[255, 0, 0], [0, 192, 192], [255, 255, 0]]
  screen.blit(BG, (0, 0))
  rectX = 0
  rectY = 275

  #Total of 8 rectangles (size of 30x30) that wait 0.5 seconds to appears in a cascade, the colors randomize with each rectangle, and a spacing of 80px between each rectangles
  for i in range(1,9):
   rectX = rectX + 80
   rectangle = (rectX, rectY, 30, 30)
   draw.rect(screen, random.choice(colors), rectangle)
   display.flip()
   time.sleep(0.5)
  
  while True:
    allevents = event.get()
    for myevent in allevents:
      if myevent.type == pygame.QUIT:
        sys.exit()