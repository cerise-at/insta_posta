import tkinter as tk
from tkinter import filedialog

from tkinter.filedialog import askopenfilename
from tkinter import *
from PIL import ImageTk, Image
import PIL.Image

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

window = Tk()

def place_window(width=500, height=500):
    #put window in centre of screen
    windowWidth = width
    windowHeight = height
    print("Width",windowWidth,"Height",windowHeight)
    
    # Gets both half the screen width/height and window width/height
    positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
    
    # Positions the window in the center of the page.
    window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight,positionRight, positionDown))


def upload_picture():
    #find file 
    global my_img
    filename = filedialog.askopenfilename(initialdir=".", title="Select File to Upload", 
    filetypes=(("jpeg", "*.jpeg"),("png", "*.png"),("bmp", "*.bmp"),("gif", "*.gif"),("jpg", "*.jpg")))
    #open file
    my_img = Image.open(filename)
    width, height = my_img.size
    print(width, height)
    #work out new image sizes for insta
    w,h = resize_img(1080, 1350, width, height)
    print(w,h)
    #resize the image
    resize_my_img = my_img.resize((w, h), Image.ANTIALIAS) 
    width, height = resize_my_img.size
    print (width, height)
    # Change window size to fit new image 
    window.geometry("{}x{}".format(width, height))
    # Pack new image onto window
    fin_img = ImageTk.PhotoImage(resize_my_img)
    tk_image = Label(window, image=fin_img)
    tk_image.photo = fin_img
    place_window(width, height)
    tk_image.pack(side = "bottom", fill = "both", expand = "yes", padx=20, pady=20)

def resize_img(c_w, c_h, i_w, i_h):
        #if size is bigger than instagram rec
    if c_w < i_w or c_h < i_h:
        if i_w > i_h:
            r = c_w / i_w
        else:
            r = c_h / i_h
        h = i_h * r
        w = i_w * r
    else:
        return int(i_w), int(i_h)
    return int(w), int(h) 

place_window()
my_img = None
button_upload = Button(window, text="Select image to upload", command=upload_picture)
button_upload.pack()



#exit button
button_quit = Button(window, text="Quit", command=window.quit)
button_quit.pack()

window.mainloop()