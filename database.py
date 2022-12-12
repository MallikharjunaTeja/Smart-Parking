import sqlite3
from datetime import datetime
from sqlite3.dbapi2 import Cursor, Timestamp
from functions_1 import *

slots=[3000,3000,3000,3000,5000,5000,8000,8000]
occupancy=[0,0,0,0,0,0,0,0]

def find_slot(car_width):
    diff=1000
    allocated_slots=[]
    for i in range(len(slots)):
        if(car_width<=slots[i] and diff>(abs(car_width-slots[i])) and occupancy[i]==0):
            diff=abs(car_width-i)
            allocated_slots.append(i+1)
            break
    if(len(allocated_slots)==0):
        for i in range(3):
            if(car_width<=(slots[i]+slots[i+1]) and occupancy[i]==0 and occupancy[i+1]==0):
                allocated_slots.append(i+1)
                allocated_slots.append(i+2)
                break
    if(len(allocated_slots)==0):
        for i in range(2):
            if(car_width<=(slots[i]+slots[i+1]+slots[i+2]) and occupancy[i]==0 and occupancy[i+1]==0 and occupancy[i+2]==0):
                allocated_slots.append(i+1)
                allocated_slots.append(i+2)
                allocated_slots.append(i+3)
                break
    for i in allocated_slots:
        occupancy[i-1]=1
    return allocated_slots

def addVehicleCheckin(vehicle_num,fare):
    conn = sqlite3.connect('vehicles.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS vehicle(
        vehicle_num text PRIMARY KEY,
        intime timestamp,
        outtime timestamp,
        base_fare real,
        total_fare real,
        total_time text
        );''')
    conn.commit()
    conn.execute("INSERT INTO vehicle (vehicle_num,intime,base_fare) \
        VALUES (?,?,?)", (vehicle_num,datetime.now(),fare))
    conn.commit()
    conn.close()
    return True

def getIntime(vehicle_num):
    conn = sqlite3.connect('vehicles.db')
    cur = conn.cursor()
    cur.execute("SELECT intime,base_fare FROM vehicle WHERE vehicle_num=?",(vehicle_num,))
    rows = cur.fetchall()
    conn.close()
    return rows[0]

def view_db():
    conn = sqlite3.connect('vehicles.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM vehicle ")
    rows = cur.fetchall()
    print(rows)
    conn.close()

def addVehicleCheckout(vehicle_num):
    conn = sqlite3.connect('vehicles.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS vehicle(
        vehicle_num text PRIMARY KEY,
        intime timestamp,
        outtime timestamp,
        base_fare real,
        total_fare real,
        total_time text
        );''')
    conn.commit()
    end_time = datetime.now()
    st, base_fare = getIntime(vehicle_num)
    start_time = datetime.fromisoformat(st)
    total_time, total_fare = calculate_charges(start_time=start_time, end_time=end_time, base_charge=base_fare)
    conn.execute("UPDATE vehicle SET total_fare = ?,outtime = ? , total_time = ? WHERE vehicle_num = ?",
                 (total_fare, end_time, total_time, vehicle_num,))
    conn.commit()
    conn.close()
    return True

def getCheckoutdetails(vehicle_num):
    conn = sqlite3.connect('vehicles.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM vehicle WHERE vehicle_num=?", (vehicle_num,))
    rows = cur.fetchall()
    conn.close()
    return rows[0]

# addVehicleCheckin('Mh12345', 12.5165)
# addVehicleCheckout('Mh12345')
# view_db()
# addVehicleCheckin('AIBACC', 163.6516)
# addVehicleCheckout('AIBACC')
# view_db()

# addVehicleCheckin('JNOSCUOWV', 452.65)
# addVehicleCheckout('JNOSCUOWV')
# view_db()

# addVehicleCheckin('OJCNIIEC', 10.5165)
# addVehicleCheckout('OJCNIIEC')
# view_db()
# print(getCheckoutdetails('OJCNIIEC'))
