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
#code from https://yagisanatode.com/2018/02/24/how-to-center-the-main-window-on-the-screen-in-tkinter-with-python-3/

windowWidth = 500
windowHeight = 500
print("Width",windowWidth,"Height",windowHeight)

 
# Gets both half the screen width/height and window width/height
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight,positionRight, positionDown))
my_img = None

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

def upload_picture():
    #find file 
    global my_img
    filename = filedialog.askopenfilename(initialdir=".", title="Select File to Upload", 
    filetypes=(("jpeg", "*.jpeg"),("png", "*.png"),("bmp", "*.bmp"),("gif", "*.gif"),("jpg", "*.jpg")))
    my_file = Label(window, text=filename)
    my_file.pack()
    my_img = Image.open(filename)
    width, height = my_img.size
    print(width, height)
    w,h = resize_img(1080, 1350, width, height)
    print(w,h)
    resize_my_img = my_img.resize((w, h), Image.ANTIALIAS) 
    width, height = resize_my_img.size
    print (width, height)
    window.geometry("{}x{}".format(width, height))
    fin_img = ImageTk.PhotoImage(resize_my_img)
    my_label = Label(window, image=fin_img)
    my_label.photo = fin_img
    my_label.pack(side = "bottom", fill = "both", expand = "yes")

button_upload = Button(window, text="Select image to upload", command=upload_picture)
button_upload.pack()



#exit button
button_quit = Button(window, text="Quit", command=window.quit)
button_quit.pack()

window.mainloop()