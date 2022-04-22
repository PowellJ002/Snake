# Packages imported from Python libraries
# tkinter provides GUI elements to use in the program
from tkinter import *

# os import  provides functions for creating and removing a directory (folder)
# Fetching its contents, changing and identifying the current directory
import os

# Login module, defines action if login is successful or unsuccessful
def login():

    # Variables set for retrieving a username and password from a file
    UNverify = username.get()
    PWverify = password.get()

    # This codeset deletes the username and password types in if log in is successful or unsuccessful
    un_entry.delete(0, END)
    pw_entry.delete(0, END)

    # Variable set for the file that contains all the list
    # UNverify and PWverify will get the username and password from this file, uses OSimport for list directory
    list_of_users = os.listdir()

    # provides action if login is successful or unsuccessful
    # If username retrieved from list_of_users file matches, then the program will check the password
    # Else the system will display message Incorrect username or password
    # If the password retrieved matches the connected password found on the list_of_users file
    # Then the system will open upa new window with the file main.py which is the main application snake game
    # Else the system will display message Incorrect username or password
    if UNverify in list_of_users:
        file1 = open(UNverify, "r")
        pw = file1.read().splitlines()
        if PWverify in pw:
            os.startfile("main.py")
        else:
            print("Incorrect username or password")
    else:
        print("Incorrect username or password")

# Module that defines action when clicking submit after registering a new account
def submit():

    # Variable set for registering a new username and password
    # Variable made global so they can be used outside of the module
    global username_info
    global password_info
    username_info = reg_username.get()
    password_info = reg_password.get()

    # This code set first opens a new file for a new username and password and then writes the username in
    # The the codeset writes the password in and attaches to username
    # The codeset then closes the file and uploads to the list directory above
    file1 = open(username_info, "w")
    file1.write(password_info)
    file1.close()

    # This codeset deletes the username and password if registration is successful or unsuccessful
    unreg_entry.delete(0, END)
    pwreg_entry.delete(0, END)

# This module defines what happens if user selects create a new account
def register():

    # Opens up a new window when create a new account is selected and sets a variable
    register_screen = Toplevel(root)

    # Creates two labels with titles enter username or enter password next to them
    # Will be displayed next to an input text box
    # Sets a variable to both labels
    label3 = Label(register_screen, text= "Enter chosen username ")
    label4 = Label(register_screen, text="Enter chosen password ")

    # Sets a string variable to registered username and registered password for reuse
    # Makes these variables global
    global reg_username
    global reg_password
    reg_username = StringVar()
    reg_password = StringVar()

    # Sets a variable to a username entry box and password entry box
    # When types in and entered, the text becomes the variable reg_username and reg_password
    # Text box variables are set to global use
    global unreg_entry
    global pwreg_entry
    unreg_entry = Entry(register_screen, textvariable = reg_username)
    # Password entry box variable shows * instead of inputted text for security purposes
    pwreg_entry = Entry(register_screen, textvariable = reg_password, show= "*")

    # Creates a button called create account below the text boxes and labels
    # When selected, username and password will be saves to directory and run the submit module
    button3 = Button(register_screen, text= "Create account", command = submit)

    # Commands where the text boxes should sit on the window
    unreg_entry.grid(row=0, column=1)
    pwreg_entry.grid(row=1, column=1)

    # Commands where the labels should sit on the window
    label3.grid(row=0, column=0)
    label4.grid(row=1, column=0)

    # Commands where the button should sit on the window
    button3.grid(row=2, column=0)

# Module for the main log in screen, this is the screen the application should begin with
def mainscreen():
    # Opens up a new window using the tkinter library and makes it the root/main window
    # Makes the window global so other windows can use its properties such as title
    global root
    root = Tk()

    # Sets a title to the new window
    root.title('Snake game')

    # Creates two labels with titles enter username or enter password next to them
    # Will be displayed next to an input text box
    # Sets a variable to both labels
    label1 = Label(root, text= "Enter username ")
    label2 = Label(root, text="Enter password ")

    # Sets a string variable to username and password for reuse
    # Makes these variables global
    global username
    global password
    username = StringVar()
    password = StringVar()

    # Sets a variable to a username entry box and password entry box
    # When types in and entered, the text becomes the variable un_entry and pw_entry
    # Text box variables are set to global use
    global un_entry
    global pw_entry
    un_entry = Entry(root, textvariable = username)

    # Password entry box variable shows * instead of inputted text for security purposes
    pw_entry = Entry(root, textvariable = password, show= "*")

    # Creates a button called Login below the text boxes and labels
    # When selected the program will run the login module
    button1 = Button(root, text= "Login", command = login)

    # Creates a button called Register below the text boxes and labels
    # When selected the program will run the register module
    button2 = Button(root, text="Register", command= register)

    # Commands where the labels should sit on the window
    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)

    # Commands where the text boxes should sit on the window
    un_entry.grid(row=0, column=1)
    pw_entry.grid(row=1, column=1)

    # Commands where the buttons should sit on the window
    button1.grid(row=2, column=0)
    button2.grid(row=2, column=2)

    # Tells Python to run the Tkinter event loop.
    # Listens for events, such as button clicks or key presses
    # Blocks any code that comes after it from running until the window of the called method is closed
    mainloop()

# This initiates the program, from there the program is event-driven
mainscreen()