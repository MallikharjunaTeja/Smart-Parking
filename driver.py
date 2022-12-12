import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from functions_1 import *
from functions_2 import *
import os

def browsefunc(ent):
    filename = askopenfilename(filetypes=([
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    ]))
    ent.insert(tk.END, filename)  # add this

def nav_to_checkin(window):
    checkin_frame(window)

def nav_to_checkout(window):
    checkout_frame(window)

def checkin_frame(destroy_this_win=None):
    if destroy_this_win is not None:
        destroy_this_win.destroy()
    root = tk.Tk()
    root.title("SMART PARKING")
    root.geometry("500x700") 
    root.call('wm','attributes','.','-topmost',True)
    uname_label = tk.Label(root,text="SMART PARKING",font=10)
    uname_label.place(x=90,y=50)
    facepic_message=tk.Label(root,text="Fare per hour: Rs.100/-",font=10)
    facepic_message.place(x=10,y=120)
    # fare_entry=tk.Entry(root,font=10)
    # fare_entry.place(x=150,y=120)
    # fare_entry.insert(tk.END,'10.00')
    facepic_entry=tk.Entry(root,font=10)
    facepic_entry.place(x=150,y=240)
    np_message=tk.Label(root,text="Number-Plate",font=10)
    np_message.place(x=10,y=250)
    facepic_browse_button=tk.Button(root,text="Capture",font=10,command=lambda:captureFace(facepic_entry))
    facepic_browse_button.place(x=400,y=210)
    profilepic_browse_button=tk.Button(root,text="Browse",font=10,command=lambda:browsefunc(facepic_entry))
    profilepic_browse_button.place(x=400,y=260)
    login_button=tk.Button(root,text="Submit",font=10,command=lambda:checkin_clicked(window=root,fare=100,pic_path=facepic_entry.get(),))
    login_button.place(x=200,y=320)
    register_nav_button=tk.Button(root,text="Checkout Page",font=10,command=lambda:nav_to_checkout(window=root,))
    register_nav_button.place(x=250,y=450)
    root.mainloop()

def checkout_frame(destroy_this_win=None):
    if destroy_this_win is not None:
        destroy_this_win.destroy()
    root = tk.Tk()
    root.title("SMART PARKING")
    root.geometry("500x700")
    root.call('wm','attributes','.','-topmost',True)
    uname_label = tk.Label(root,text="SMART PARKING",font=10)
    uname_label.place(x=90,y=100)
    profilepic_message=tk.Label(root,text="Number-Plate",font=10)
    profilepic_message.place(x=10,y=230)
    profilepic_entry=tk.Entry(root,font=10)
    profilepic_entry.place(x=150,y=230)
    profilepic_browse_button=tk.Button(root,text="Browse",font=10,command=lambda:browsefunc(profilepic_entry))
    profilepic_browse_button.place(x=400,y=190)
    facepic_browse_button=tk.Button(root,text="Capture",font=10,command=lambda:captureFace(profilepic_entry))
    facepic_browse_button.place(x=400,y=240)
    register_button=tk.Button(root,text="Submit",font=10,command=lambda:checkout_clicked(window=root,pic_path=profilepic_entry.get()))
    register_button.place(x=200,y=320)
    login_nav_button=tk.Button(root,text="Checkin Page",font=10,command=lambda:nav_to_checkin(window=root,))
    login_nav_button.place(x=300,y=450)
    root.mainloop()

checkin_frame()
