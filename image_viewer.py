# Code With Drex
# Importing Modules

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os, os.path

win = ttk.Window()
win.title('Image Viewer')
ttk.Style('superhero')

# Size of the window
win.geometry('800x600')

main_frame = ttk.Frame(win)
main_frame.pack()

# Variables
file_location = ''
img_no = 0
imgs = []


explorer_frame = ttk.Frame(main_frame)
explorer_frame.grid(row=0, column=0, padx=10, pady=(10, 0))

explorer_entry = ttk.Entry(explorer_frame, width=80)
explorer_entry.grid(row=0, column=0, columnspan=2, padx=(80, 0))

image_frame = ttk.Frame(main_frame)
image_frame.grid(row=1, column=0)

btn_frame = ttk.Frame(main_frame)
btn_frame.grid(row=2, column=0)

no_label = ttk.Label(image_frame, font=('Arial', 20, 'bold'))
no_label.grid(row=0, column=4, pady=(10, 0), sticky=NW)

image_label = ttk.Label(image_frame, width=100, text=' ')
image_label.grid(row=1, column=0, padx=(60, 0), pady=10, rowspan=10, columnspan=8)


#******* Functions  *******#
# Picking the image folder
def explor_file():
    global file_location
    no_label.configure(text='')
    file_location = filedialog.askdirectory(initialdir='/', title='Select a Folder')
    explorer_entry.delete(0, END)
    explorer_entry.insert(0, file_location)
    set_img_list()


# Extracting all the images in the folder
# resizing the images and saving them in a list
def set_img_list():
    global imgs
    global file_location
    global img_no
    global image_label
    valid_images = ['.jpg', '.gif', '.png', '.tga']
    imgs = []
    img_no=0
    for file in os.listdir(file_location):
        ext = os.path.splitext(file)[1]
        if ext.lower() not in valid_images:
            continue
        img = Image.open(os.path.join(file_location, file))

        # Resizing the Images
        w, h = img.size # Getting the current size (width and height) of the image
        n_height = 400  # Setting the constant height (new_height)
        n_width = int((n_height/h) * w) # Calculating the new width that will make the image maintain it ration
        img = img.resize((n_width, n_height))
        imgs.append(ImageTk.PhotoImage(img))

    if len(imgs) >= 1:
        image_label.configure(image=imgs[img_no])
        no_label.configure(text=f"{img_no+1}/{len(imgs)}")
    else:
        messagebox.showerror('No image', 'No image in this directory, choose another directory to view images')
    

# Moving to the next image
def next_img():
    global img_no
    global imgs
    no_of_img = len(imgs)
    if img_no < no_of_img-1:
        img_no+=1
        image_label.configure(image=imgs[img_no])

    no_label.configure(text=f"{img_no+1}/{no_of_img}")


# Moving to the previous image
def prev_img():
    global img_no
    global imgs
    if img_no > 0:
        img_no-=1
        image_label.configure(image=imgs[img_no])
    no_label.configure(text=f"{img_no+1}/{len(imgs)}")


prev_btn = ttk.Button(btn_frame, text='Previous', command=prev_img)
prev_btn.grid(row=0, column=0, padx=10)

next_btn = ttk.Button(btn_frame, text='  Next  ', command=next_img)
next_btn.grid(row=0, column=1, padx=10)

explorer_btn = ttk.Button(explorer_frame, text='Choose Location', command=explor_file)
explorer_btn.grid(row=0, column=5, padx=10)

win.mainloop()
