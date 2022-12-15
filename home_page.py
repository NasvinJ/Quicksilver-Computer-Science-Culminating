import pygame,sys,time

def home_screen_gui():
  pygame.init()
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

  BG=pygame.image.load("quicksilver_main_bg.jpg")

  screen.blit(BG, (0, 0))