import pygame,sys
from button import Button
from pygame import display, event

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

  def game_screen():
    while True:
      screen = pygame.display.set_mode((infoObject.current_w * 1.4, infoObject.current_h / 1.1))
      display.set_caption("Game Screen")
      options_mouse_pos = pygame.mouse.get_pos()
      screen.fill("dark gray")
      hey_font = pygame.font.Font("assets/font.ttf", 20)
      options_text =hey_font.render("Pick a Speed Test!", True,
                                         "Black")
      options_rect = options_text.get_rect(center=(375, 70))
      screen.blit(options_text, options_rect)

      options_back = Button(image=None,
                      pos=(630, 40),
                      text_input="BACK",
                      font=get_font(45),
                      base_color="Blue",
                      hovering_color="Green")

      options_back.changeColor(options_mouse_pos)
      options_back.update(screen)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if options_back.checkForInput(options_mouse_pos):
                run_test()

        typing_test_button = Button(image=None,
                        pos=(150, 200),
                        text_input="Typing Speed Test",
                        font=get_font(17),
                        base_color="White",
                        hovering_color="Black")

        typing_test_button.changeColor(options_mouse_pos)
        typing_test_button.update(screen)

      pygame.display.update()
  
  def run_test():
    while True:
      screen.blit(bg, (0, 0))
      menu_mouse_pos = pygame.mouse.get_pos()
      menu_text = get_font(100).render("", True, "#b68f40")
      menu_rect = menu_text.get_rect(center=(640, 100))
      
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
  
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if options_button.checkForInput(menu_mouse_pos):
                  game_screen()

      pygame.display.update()

  run_test()