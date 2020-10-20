# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 09:11:25 2020

@author: 66IN
"""
from tkinter import *
from PIL import Image,ImageTk
root = Tk()

root.title("Image Viewer")

# root.iconbitmap('')  -> used to put icon with title

my_img1 = ImageTk.PhotoImage(Image.open('images/1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('images/2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('images/3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('images/4.jpg'))

my_list = [my_img1,my_img2,my_img3,my_img4]
    
    
my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def back(number):
    global button_backback
    global button_forward
    global my_label
    
    my_label.grid_forget()
    my_label = Label(image=my_list[number-1])
    button_forward = Button(root, text =">>",command=lambda:forward(number+1))
    button_back = Button(root,text="<<",command=lambda:back(number-1))
    
    
    if number == 1:
        button_back = Button(root,text="<<",state=DISABLED)
    
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    
    
button_back = Button(root,text="<<",command=back)
button_exit = Button(root,text="Exit",command=root.quit)
button_forward = Button(root,text=">>",command=lambda:forward(2))


button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)    
    
    
def forward(number):
    global button_back
    global button_forward
    global my_label
    
    
    my_label.grid_forget()
    my_label = Label(image=my_list[number-1])
    button_forward = Button(root, text =">>",command=lambda:forward(number+1))
    button_back = Button(root,text="<<",command=lambda:back(number-1))
    
    if number ==4:
        button_forward =Button(root, text=">>",state = DISABLED)
        
    
    
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

button_back = Button(root,text="<<",command=back , state=DISABLED)
button_exit = Button(root,text="Exit",command=root.quit)
button_forward = Button(root,text=">>",command=lambda:forward(2))


button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)



root.mainloop()