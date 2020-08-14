import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import PIL.Image
from tkinter.filedialog import askopenfilename
from tkinter import *
'''
Things to do
Do a small tutorial on tkinter
* Text boxes
* Event handlers
* Dragging and dropping files.

Instagram API:
Take a look at this, maybe look for other instagram python API wrappers
https://github.com/ping/instagram_private_api

DO NOT PUSH USERNAMES AND PASSWORDS TO GITHUB. ALWAYS PUT THEM IN A FILE LISTED IN .gitignore
'''

#def UploadAction(event=None):
    #sel_img = window.filename = filedialog.askopenfilename(initialdir="/", title="Choose an image", filetypes=(("png file","*.png"),("jpeg files","*.jpg"),("jpeg files","*.jpeg"),("movies", "*.mov")))
    #print('Selected:', filename)
    #return sel_img

#if __name__ == "__main__":
    #window = tk.Tk()
    #text_box = tk.Text(window)
    #button = tk.Button(window, text='Open Image to Upload', command=UploadAction)
    #text_box.pack()
    #button.pack()
    #my_img = ImageTk.PhotoImage(Image.open(window.filename))
    
    #window.mainloop() 


window = Tk()



#find file
window.filename = filedialog.askopenfilename(initialdir="/", title="Select File to Upload", 
filetypes=(("jpeg", "*.jpeg"),("png", "*.png"),("bmp", "*.bmp"),("gif", "*.gif"),("jpg", "*.jpg")))
my_file = Label(window, text=window.filename)

#open file
my_img = ImageTk.PhotoImage(PIL.Image.open(window.filename))
my_label = Label(image=my_img)
my_label.pack()

#exit button
button_quit = Button(window, text="Quit", command=window.quit)
button_quit.pack()

window.mainloop()