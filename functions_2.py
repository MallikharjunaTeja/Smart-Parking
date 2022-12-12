from re import L
import random
from functions_1 import *
from database import *
import tkinter as tk
from tkinter import messagebox
# from socketlistener import carwidth
#client-server
# car width calculation
# carwidth
# count=1
with open('readme.txt') as f:
    lines=f.readlines()
carwidth=int(lines[0])

def checkin_clicked(window,fare,pic_path):
    new_pic_path = pic_path.replace('/', '\\')
    fare = float(fare)
    number_plate_str = getNumberPlateSting(new_pic_path)
    res = addVehicleCheckin(vehicle_num=number_plate_str, fare=fare)
    if(res == True):
        messagebox.showinfo('SUCCESS!!!','Vehicle is allocated slots:{}'.format(find_slot(carwidth)))

def checkout_clicked(window, pic_path):
    new_pic_path = pic_path.replace('/', '\\')
    number_plate_str = getNumberPlateSting(pic_path)
    res = addVehicleCheckout(vehicle_num=number_plate_str)
    ans = getCheckoutdetails(vehicle_num=number_plate_str)
    text_str = 'Number= '+str(ans[0])+'\n'+'Check-In Time= ' + str(ans[1])+'\n'+'Check-Out Time= '+str(ans[2])+'\n'+'Base Fare= '+str(ans[3])+'\n'+'Collectible Fare= ' + \
        str(ans[4])+'\n'+'Durationin hrs = '+str(ans[5])+'\n'
    if(res == True):
        messagebox.showinfo('Charges Calculated!!',text_str)

# def checkin_clicked(window,fare,pic_path):
#     new_pic_path = pic_path.replace('/', '\\')
#     fare = float(fare)
#     number_plate_str = getNumberPlateSting(new_pic_path)
#     res = addVehicleCheckin(vehicle_num=number_plate_str, fare=fare)
#     if(res == True):
#         messagebox.showinfo('SUCCESS!!!','Vehicle is allocated slots:{}'.format(random.randint(0,9)))