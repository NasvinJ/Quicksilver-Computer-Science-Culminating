#import modules
from tkinter import *
import os

#Reposition buttons

# Designing window for registration
def login_screen_gui(): 
  def register():
      global register_screen
      register_screen = Toplevel(main_screen)
      register_screen.title("Register")
      register_screen.geometry("400x350")
   
      global username
      global password
      global username_entry
      global password_entry
      username = StringVar()
      password = StringVar()

      #Creates register screen details which has an inputable username and password field.
      Label(register_screen, text="Please enter details below", bg="#87ceeb", relief="solid", height=2, font=("Calibri", 13)).pack()
      Label(register_screen, text="").pack()
      Label(register_screen, height=1).pack()
      username_lable = Label(register_screen, text="Username * ", font=(10))
      username_lable.pack()
      username_entry = Entry(register_screen, textvariable=username)
      username_entry.pack()
      Label(register_screen, height=2).pack()
      password_lable = Label(register_screen, text="Password * ", font=(10))
      password_lable.pack()
      password_entry = Entry(register_screen, textvariable=password, show='*')
      password_entry.pack()
      Label(register_screen, text="").pack()
      Button(register_screen, text="Register", width=10, height=1, bg="#87ceeb", command = register_user).pack()
    
      def delete_register_screen():
        register_screen.destroy()
      Button(register_screen, text="Back", width=8, height=1, bg="#FF0000", command = delete_register_screen).pack()
      Label(register_screen, height=2).pack()
      Label(register_screen, width="300", height="3", bg="dimgrey").pack()
   
   
  # Designing window for login 
   
  def login():
      global login_screen
      login_screen = Toplevel(main_screen)
      login_screen.title("Login")
      login_screen.geometry("400x350")
      Label(login_screen, text="Please enter details below", bg="#87ceeb", relief="solid", height=2, font=("Calibri", 13)).pack()
      Label(login_screen, text="").pack()
   
      global username_verify
      global password_verify
   
      username_verify = StringVar()
      password_verify = StringVar()
   
      global username_login_entry
      global password_login_entry
    
      Label(login_screen, height=1).pack()
      Label(login_screen, text="Username * ", font=(10)).pack()
      username_login_entry = Entry(login_screen, textvariable=username_verify)
      username_login_entry.pack()
      Label(login_screen, text="").pack()
      Label(login_screen, height=1).pack()
      Label(login_screen, text="Password * ", font=(10)).pack()
      password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
      password_login_entry.pack()
      Label(login_screen, text="").pack()
      Button(login_screen, text="Login", width=10, height=1, bg="#87ceeb", command = login_verify).pack()
      Button(login_screen, text="Back", width=8, height=1, bg="#FF0000", command = delete_login_screen).pack()
      Label(login_screen, height=2).pack()
      Label(login_screen, width="300", height="3", bg="dimgrey").pack()
   
  # Implementing event on register button which saves the username and password information to a seperate file each time that gets recognized.
  def register_user():
      username_info = username.get()
      password_info = password.get()
   
      file = open(username_info, "w")
      file.write(username_info + "\n")
      file.write(password_info)
      file.close()
   
      username_entry.delete(0, END)
      password_entry.delete(0, END)
   
      Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
   
  # Implementing event on login button which matches the file from the username and password registeration, running the function long_sucess
  def login_verify():
      username1 = username_verify.get()
      password1 = password_verify.get()
      username_login_entry.delete(0, END)
      password_login_entry.delete(0, END)
   
      list_of_files = os.listdir()
      if username1 in list_of_files:
          file1 = open(username1, "r")
          verify = file1.read().splitlines()
          if password1 in verify:
              login_sucess()
   
          else:
              password_not_recognised()
   
      else:
          user_not_found()
   
  # Designing popup for login success that can have the user click on the button "OK," automatically destroying all the pop-ups
  def login_sucess():
      global login_success_screen
      global exitlogin
      login_success_screen = Toplevel(login_screen)
      login_success_screen.title("Success")
      login_success_screen.geometry("250x200")
      Label(login_success_screen, height=2).pack()
      Label(login_success_screen, text="Login Success").pack()
      Label(login_success_screen, height=1).pack()
      Button(login_success_screen, text="OK", bg="#1a9200", command=delete_login_success and delete_login_screen and delete_main_screen).pack()
   
  # Designing popup for login invalid password showing "Invalid Password" and click on "OK" to retry
  def password_not_recognised():
      global password_not_recog_screen
      password_not_recog_screen = Toplevel(login_screen)
      password_not_recog_screen.title("Success")
      password_not_recog_screen.geometry("250x200")
      Label(password_not_recog_screen, height=2).pack()
      Label(password_not_recog_screen, text="Invalid Password ").pack()
      Label(password_not_recog_screen, height=1).pack()
      Button(password_not_recog_screen, text="OK", bg="#1a9200", command=delete_password_not_recognised).pack()
   
  # Designing popup for user not found
  def user_not_found():
      global user_not_found_screen
      user_not_found_screen = Toplevel(login_screen)
      user_not_found_screen.title("Success")
      user_not_found_screen.geometry("250x200")
      Label(user_not_found_screen, height=2).pack()
      Label(user_not_found_screen, text="User Not Found").pack()
      Label(user_not_found_screen, height=1).pack()
      Button(user_not_found_screen, text="OK", bg="#1a9200", command=delete_user_not_found_screen).pack()
   
  # Functions to delete pop-ups
  def delete_login_screen():
      login_screen.destroy()

  def delete_main_screen():
      main_screen.destroy()
  
  def delete_login_success():
      login_success_screen.destroy()
   
  def delete_password_not_recognised():
      password_not_recog_screen.destroy()
   
  def delete_user_not_found_screen():
      user_not_found_screen.destroy()
   
   
  # Designing Main (first) window
  def main_account_screen():
      global main_account_screen
      global main_screen
      main_screen = Tk()
      #Set pop-up screen size to 400x350 for main window
      main_screen.geometry("400x350")
      main_screen.title("Account Login")
      #Title on top centered with blue background and black border
      Label(text="Select Your Choice", bg="#87ceeb", width="300", relief="solid", height="2", font=("Calibri", 13)).pack()
      Label(height="3").pack()
      Label(text="").pack
      #Creates the login and register buttons which takes them to their corresponding new pop-up
      Button(text="Login", height="3", width="30", command = login).pack()
      Label(text="").pack()
      Button(text="Register", height="3", width="30", command=register).pack()
      Label(height="5").pack()
      Label(width="300", height="3", bg="dimgrey").pack() #Grey background for main window
    
      main_screen.mainloop()
   
   
  main_account_screen()