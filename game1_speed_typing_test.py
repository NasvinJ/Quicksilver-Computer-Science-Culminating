#import necessary modules including pygame for the screen
import pygame
from pygame.locals import *
import sys
import time
import random

def speed_typing_gui_screen():
  class Game:
      def __init__(self):
          #Intializes necessary variables
          self.w=740
          self.h=460
          self.reset=True
          self.speed = True
          self.active = False
          self.input_text=''
          self.word = ''
          self.time_start = 0
          self.total_time = 0
          self.accuracy = '0%'
          self.results = 'Time:0 Accuracy:0 % Wpm:0 '
          self.wpm = 0
          self.end = False
          self.HEAD_C = (255,213,102)
          self.TEXT_C = (240,240,240)
          self.RESULT_C = (255,70,70)
          
          #Each time the speed typing test game loads or rests, the type_speed_open.png flashes in-between
          pygame.init()
          self.open_img = pygame.image.load('type-speed-open.png')
          self.open_img = pygame.transform.scale(self.open_img, (self.w,self.h))
  
          #Creates the screen with adjusted measurements: 850x750
          self.bg = pygame.image.load('background.jpg')
          self.bg = pygame.transform.scale(self.bg, (850,750))
  
          self.screen = pygame.display.set_mode((self.w,self.h))
          #Puts the caption of the window on top
          pygame.display.set_caption('Type Speed test')
         
      #Function used to draw text on the screen including coordinates and color
      def draw_text(self, screen, msg, y ,fsize, color):
          font = pygame.font.Font(None, fsize)
          text = font.render(msg, 1,color)
          text_rect = text.get_rect(center=(self.w/2, y))
          screen.blit(text, text_rect)
          pygame.display.update()   

      #Function to grab text file with the quotes to randomly choose from
      def get_sentence(self):
          f = open('sentences.txt').read()
          sentences = f.split('\n')
          sentence = random.choice(sentences)
          return sentence

      #Function to input the results for the user involving time, accuracy, and wpm
      def show_results(self, screen):
          if(not self.end):
              #Calculate time
              self.total_time = time.time() - self.time_start
                 
              #Calculate accuracy
              count = 0
              for i,c in enumerate(self.word):
                  try:
                      if self.input_text[i] == c:
                          count += 1
                  except:
                      pass
              self.accuracy = count/len(self.word)*100
             
              #Calculate words per minute by counting each word as an average score of 5
              self.wpm = len(self.input_text)*60/(5*self.total_time)
              self.end = True
              print(self.total_time)

              #Inputs the actual string of the results
              self.results = 'Time:'+str(round(self.total_time)) +" secs   Accuracy:"+ str(round(self.accuracy)) + "%" + '   Wpm: ' + str(round(self.wpm))

              #Using if-else statements, if the user gets a score of 30 or less then an image of a turtle is shown on the bottom left corner, but if they get between 31 to 70 then a cheetah is shown, while a score that is 71 or higher is a cartoon image of Quicksilver. The computer icon is inputed in the bottom middle as a button which when clicked on, runs the reset function to retry
              if self.wpm <= 30:
                # draw turtle image
                self.speed_img = pygame.image.load('turtle.png')
                self.speed_img = pygame.transform.scale(self.speed_img, (150,150))
                screen.blit(self.speed_img, (self.w/2-357,self.h-150))
              elif self.wpm >= 31 and self.wpm <=70:
                # draw cheetah image
                self.speed_img = pygame.image.load('cheetah.png')
                self.speed_img = pygame.transform.scale(self.speed_img, (250,140))
                screen.blit(self.speed_img, (self.w/2-355,self.h-135))
              else:
                # draw quicksilver animated image
                self.speed_img = pygame.image.load('quicksilver_animated.png')
                self.speed_img = pygame.transform.scale(self.speed_img, (170,170))
                screen.blit(self.speed_img, (self.w/2-345,self.h-167))
  
              # draw icon image
              self.time_img = pygame.image.load('icon.png')
              self.time_img = pygame.transform.scale(self.time_img, (150,150))
              screen.blit(self.time_img, (self.w/2-75,self.h-120))
              self.draw_text(screen,"Reset", self.h - 50, 26, (100,100,100))
              
              print(self.results)
              pygame.display.update()
  
      def run(self):
          self.reset_game()
      
         
          self.running=True
          while(self.running):
              clock = pygame.time.Clock()
              self.screen.fill((0,0,0), (50,250,650,50))
              pygame.draw.rect(self.screen,self.HEAD_C, (50,250,650,50), 2)
              # update the text of user input
              self.draw_text(self.screen, self.input_text, 274, 26,(250,250,250))
              pygame.display.update()
              for event in pygame.event.get():
                  if event.type == QUIT:
                      self.running = False
                      sys.exit()
                  elif event.type == pygame.MOUSEBUTTONUP:
                      x,y = pygame.mouse.get_pos()
                      # position of input box
                      if(x>=50 and x<=650 and y>=250 and y<=300):
                          self.active = True
                          self.input_text = ''
                          self.time_start = time.time() 
                       # position of reset box
                      if(x>=310 and x<=510 and y>=390 and self.end):
                          self.reset_game()
                          x,y = pygame.mouse.get_pos()
           
                  #When the user presses enter, it shows the results
                  elif event.type == pygame.KEYDOWN:
                      if self.active and not self.end:
                          if event.key == pygame.K_RETURN:
                              print(self.input_text)
                              self.show_results(self.screen)
                              print(self.results)
                              self.draw_text(self.screen, self.results,325, 28, self.RESULT_C)  
                              self.end = True
                              
                          elif event.key == pygame.K_BACKSPACE:
                              self.input_text = self.input_text[:-1]
                          else:
                              try:
                                  self.input_text += event.unicode
                              except:
                                  pass
              
              pygame.display.update()
               
                  
          clock.tick(60)

      #Function to reset all variables back to original values
      def reset_game(self):
          self.screen.blit(self.open_img, (0,0))
  
          pygame.display.update()
          time.sleep(1)
          
          self.reset=False
          self.end = False
          self.active= False
  
          self.input_text=''
          self.word = ''
          self.time_start = 0
          self.total_time = 0
          self.wpm = 0
        
          # Get random sentence 
          self.word = self.get_sentence()
          if (not self.word): self.reset_game()
          #drawing heading
          self.screen.fill((0,0,0))
          self.screen.blit(self.bg,(0,0))
          #Shows the main and secondary title on the screen
          msg = "Typing Speed Test"
          self.draw_text(self.screen, msg,75, 80,self.HEAD_C) 
          msg = "Inspirational Quotes"
          self.draw_text(self.screen, msg,140, 50,self.HEAD_C) 
          # draw the rectangle for input box
          pygame.draw.rect(self.screen,(255,192,25), (50,250,650,50), 2)
  
          # draw the sentence string
          self.draw_text(self.screen, self.word,200, 28,self.TEXT_C)
          
          pygame.display.update()
  
  Game().run()