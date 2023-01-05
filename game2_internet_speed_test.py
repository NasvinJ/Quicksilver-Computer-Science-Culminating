#imports tkinter module for the screen, speedtest module for necessary abilites (to get info on download speed, upload speed, and ping), and other modules
import tk
from tkinter import *
import speedtest
import tkinter.messagebox
option=''
from PIL import Image
import ImageTk


def internet_speed_gui_screen():
  #Grabbing info from user relative to device's speed using the speedtest module
  def showSpeed():
      global option
      #Speedtest module renamed to st
      st = speedtest.Speedtest()
      #Grabs downdload speed, upload speed, and ping info
      if option == 'Download Speed':
          speed=(st.download())
      elif option == 'Upload Speed':
          speed=(st.upload())
      elif option == 'Ping':
          servernames =[]
          st.get_servers(servernames)
          speed=(st.results.ping)
      speedWithUnits=''
      #Values returned gets rounded along with the necessary speed measurement
      if(speed<1000):
          speedWithUnits=str(round(speed, 3))+" bps"
      elif(speed<1000000):
          speedWithUnits=str(round(speed/1000, 3))+" Kbps"
      elif(speed<1000000000):
          speedWithUnits=str(round(speed/1000000, 3))+" Mbps"
      else:
          speedWithUnits=str(round(speed/1000000000, 3))+" Gbps"

      #When the message box appears, it gives the user's value back in string
      tkinter.messagebox.showinfo("Quicksilver Internet Speed Tester",  "Hi! Your " +option+" Speed is:"+speedWithUnits)

  def downloadSpeed():
      global option
      option='Download Speed'
      showSpeed()
  def uploadSpeed():
      global option
      option='Upload Speed'
      showSpeed()
  def ping():
      global option
      option='Ping'
      showSpeed()
  
  #Creating the main window, the captions of windown as "Quicksilver Internet Speed Tester," screen size as 740x460, and a background color
  wn = tkinter.Tk()
  wn.title("Quicksilver Internet Speed Tester")
  wn.geometry('740x460')
  wn.config(bg='azure')

  #Creates the text titles shown to the user using their coordinates and font size
  Label(wn, text='Quicksilver Internet Speed Test',bg='azure',
        fg='black', font=('Courier', 15)).place(x=40, y=30)
  Label(wn, text='Choose Any of the Options Below if Worthy',bg='azure',
        fg='black', font=('Courier', 12)).place(x=20, y=70)
  #Button to convert Audio to PDF form
  Button(wn, text="Check Download Speed", bg='ivory3',font=('Courier', 15), borderwidth = '4',width=20,
         command=downloadSpeed).place(x=230, y=110)
  #Button to Check Upload Speed
  Button(wn, text="Check Upload Speed", bg='ivory3',font=('Courier', 15),borderwidth = '4', width=20,
         command=uploadSpeed).place(x=230, y=205)
  #Button to convert Audio to PDF form
  Button(wn, text="Check Ping", bg='ivory3',font=('Courier', 15), borderwidth = '4', width=20,
         command=ping).place(x=230, y=305)
  
  flash_delay = 600  # msec between colour change
  flash_colours = ('black', 'red') # Two colours to swap between

  #Goes between black and red using the flash_colors variable and delays it by 600 msecs
  def flashColour(object, colour_index):
      object.config(foreground = flash_colours[colour_index])
      wn.after(flash_delay, flashColour, object, 1 - colour_index)

  #Creates the accutal text and using the flashcolor function to vary between the color and time
  my_label = Label(wn, text = 'Quicksilver Incorporation',font=('Courier', 12), foreground = flash_colours[0])
  my_label.pack()
  
  flashColour(my_label, 0)

  #Shows a speedometer image on the bottom middle with normal color in the entire row
  img = ImageTk.PhotoImage(Image.open("internet_speedometer.png"))
  panel = Label(wn, image = img)
  panel.pack(side = "bottom", fill="both")
  #Runs the window till it is closed
  wn.mainloop()