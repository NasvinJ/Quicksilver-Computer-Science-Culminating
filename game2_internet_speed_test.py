import tk
from tkinter import *
import speedtest
import tkinter.messagebox
option=''
from PIL import Image
import ImageTk

def showSpeed():
    global option
    st = speedtest.Speedtest()
    if option == 'Download Speed':
        speed=(st.download())
    elif option == 'Upload Speed':
        speed=(st.upload())
    elif option == 'Ping':
        servernames =[]
        st.get_servers(servernames)
        speed=(st.results.ping)
    speedWithUnits=''
    if(speed<1000):
        speedWithUnits=str(round(speed, 3))+" bps"
    elif(speed<1000000):
        speedWithUnits=str(round(speed/1000, 3))+" Kbps"
    elif(speed<1000000000):
        speedWithUnits=str(round(speed/1000000, 3))+" Mbps"
    else:
        speedWithUnits=str(round(speed/1000000000, 3))+" Gbps"
   
    #print( "Hi! Your" +option+" Speed is:"+speedWithUnits)
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

#Creating the main window
wn = tkinter.Tk()
wn.title("Quicksilver Internet Speed Tester")
wn.geometry('740x460')
wn.config(bg='azure')

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

def flashColour(object, colour_index):
    object.config(foreground = flash_colours[colour_index])
    wn.after(flash_delay, flashColour, object, 1 - colour_index)

my_label = Label(wn, text = 'Quicksilver Incorporation',font=('Courier', 12), foreground = flash_colours[0])
my_label.pack()

flashColour(my_label, 0)

img = ImageTk.PhotoImage(Image.open("internet_speedometer.png"))
panel = Label(wn, image = img)
panel.pack(side = "bottom", fill="both")
#Runs the window till it is closed
wn.mainloop()