import string
from random import randint, choice
from tkinter import *
from tkinter import Button

#fucntion that generates the password
def generatePassword():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password ="".join(choice(all_chars) for X in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# the height and width of the screen
HEIGHT = 400
WIDTH = 400
# create the tkinter screen
window = Tk()
window.title("Password Generator")
window.geometry(f"{HEIGHT}x{WIDTH}")
window.iconbitmap()
window.config(background='royalblue')

# create the principale fram
frame = Frame(window, bg='red')

# create the ipnut to show the generated password
password_entry = Entry(frame, font=("Helvetica", 20), bg='royalblue', fg='white')
password_entry.pack()

# create the button thats gonna generate the password , onClick we call the function generatePassword
generate_password_button = Button(frame, text="Generate", font=("Helvetica", 15), bg='black', fg='white', command=generatePassword)
generate_password_button.pack(fill=X)

# the menu on the top left
menu = Menu(window)
menu.add_command(label="EXIT", command=window.quit)

# screen config
frame.pack(expand=YES)
window.config(menu=menu)
window.mainloop()
