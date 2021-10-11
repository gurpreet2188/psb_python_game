from gui import *
import csv_read_write as csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

# p = player, hp = player health power, w = weapons

mp = []
sp = []
hp = []
ws = []
spmp = ''
count = 0
root = Tk()


def main():
    global root
    csv.CSVRW.clean(csv)
    mainframe = ttk.Frame(root, padding="3 3 12 12")

    tnkbt = ttk
    dronebtn = ttk
    warriorbtn = ttk
    startbtn = ttk

    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    tnkbt.Button(mainframe, text='Set name for:\nTank, Max = 1', command=set_tnk_name).grid(column=1, row=1)
    dronebtn.Button(mainframe, text='Set name for:\nDrones, Max = 2', command=set_drone_name).grid(column=2, row=1)
    warriorbtn.Button(mainframe, text='Set name for:\nWarrior', command=set_warrior_name).grid(column=3, row=1)
    startbtn.Button(mainframe, text='Start Game', command=start_gui).grid(column=2, row=6)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    mainframe.mainloop()


def start_gui():
    global root
    check = csv.CSVRW.reader(csv)
    if check[0]['type'] != '.' and check[1]['type'] != '.' and check[2]['type'] != '.':
        root.destroy()
        gui = GUI
        gui.turtle_setup(gui)
    else:
        msg = messagebox
        tnk = msg.showerror(title='Used', message='Please fill all 3 slots')


def set_tnk_name():
    tank = 0
    drone = 0
    warrior = 0
    read = csv.CSVRW.reader(csv)
    for i, ch in enumerate(read):
        if read[i]['type'] == 'warrior':
            warrior += 1
        elif read[i]['type'] == 'drone':
            drone += 1
        elif read[i]['type'] == 'tanker':
            tank += 1
    if warrior == 0 and drone == 0:
        if tank == 0:
            dialog = simpledialog
            name = dialog.askstring('Name', 'Enter name for tank user')
            if name:
                tank_name(name)
        else:
            msg = messagebox
            tnk = msg.showerror(title='Used', message='Zero slots available for tank')
    elif warrior == 0 and drone == 1:
        if tank == 0:
            dialog = simpledialog
            name = dialog.askstring('Name', 'Enter name for tank user')
            if name:
                tank_name(name)
        else:
            msg = messagebox
            tnk = msg.showerror(title='Used', message='Zero slots available for tank')
    elif warrior == 2 and drone == 0:
        if tank == 0:
            dialog = simpledialog
            name = dialog.askstring('Name', 'Enter name for tank user')
            if name:
                tank_name(name)
        else:
            msg = messagebox
            tnk = msg.showerror(title='Used', message='Zero slots available for tank')

    elif warrior == 2 and drone == 1:
        msg = messagebox
        tnk = msg.showerror(title='Used', message='Zero slots available for tank')
    elif warrior == 3:
        msg = messagebox
        tnk = msg.showerror(title='Used', message='Zero slots available for tank')
    else:
        msg = messagebox
        tnk = msg.showerror(title='Used', message='Zero slots available for tank')


def set_drone_name():
    tank = 0
    drone = 0
    warrior = 0
    dialog = simpledialog
    read = csv.CSVRW.reader(csv)
    for i, ch in enumerate(read):
        if read[i]['type'] == 'warrior':
            warrior += 1
        elif read[i]['type'] == 'drone':
            drone += 1
        elif read[i]['type'] == 'tanker':
            tank += 1
        else:
            break
    if tank == 0 and warrior == 0:
        if drone == 0:
            dialog = simpledialog
            name = dialog.askstring('Name', 'Enter name for drone user')
            if name:
                drone_names(name)

        elif drone == 1:
            name = dialog.askstring('Name', 'Enter name for another drone user?')
            if name:
                drone_names(name)

        elif drone == 2:
            msg = messagebox
            tnk = msg.showerror(title='Used', message='Zero slots available for drone')
        else:
            msg = messagebox
            tnk = msg.showerror(title='Used', message='Zero slots available for drone')
    elif tank == 1 and warrior == 0:
        if drone == 0:
            dialog = simpledialog
            name = dialog.askstring('Name', 'Enter name for drone user')
            if name:
                drone_names(name)
        if drone == 1:
            msg = messagebox
            tnk = msg.showerror(title='Used', message='Zero slots available for drone')
    elif tank == 1 and warrior == 1:
        if drone == 0:
            name = dialog.askstring('Name', 'Enter name for another drone user?')
            if name:
                drone_names(name)
        else:
            msg = messagebox
            tnk = msg.showerror(title='Used', message='Zero slots available for drone')
    elif tank == 0 and warrior == 1:
        if drone == 0:
            name = dialog.askstring('Name', 'Enter name for another drone user?')
            if name:
                drone_names(name)
        elif drone == 1:
            name = dialog.askstring('Name', 'Enter name for another drone user?')
            if name:
                drone_names(name)

        else:
            msg = messagebox
            tnk = msg.showerror(title='Used', message='Zero slots available for drone')
    elif tank == 1 and warrior == 2:
        msg = messagebox
        tnk = msg.showerror(title='Used', message='Zero slots available for drone')
    else:
        msg = messagebox
        tnk = msg.showerror(title='Used', message='Zero slots available for drone')


def set_warrior_name():
    tank = 0
    drone = 0
    warrior = 0
    dialog = simpledialog
    read = csv.CSVRW.reader(csv)
    for i, ch in enumerate(read):
        if read[i]['type'] == 'warrior':
            warrior += 1
        elif read[i]['type'] == 'drone':
            drone += 1
        elif read[i]['type'] == 'tanker':
            tank += 1
    if tank == 0 and drone == 0:
        if warrior == 0:
            dialog = simpledialog
            name = dialog.askstring('Name', 'Enter name for warrior')
            if name:
                warrior_names(name)

        elif warrior == 1:
            dialog = simpledialog
            name = dialog.askstring('Name', 'Enter name for another warrior')
            if name:
                warrior_names(name)

        elif warrior == 2:
            name = dialog.askstring('Name', 'Enter name for another warrior')
            if name:
                warrior_names(name)
        else:
            msg = messagebox
            tnk = msg.showerror(title='Used', message='Zero slots available.')
    elif tank == 1 and drone == 1:
        if warrior == 0:
            dialog = simpledialog
            name = dialog.askstring('Name', 'Enter name for warrior')
            if name:
                warrior_names(name)
        else:
            msg = messagebox
            tnk = msg.showerror(title='Used', message='Zero slots available.')
    elif tank == 1 and drone == 0:
        if warrior == 0:
            dialog = simpledialog
            name = dialog.askstring('Name', 'Enter name for warrior')
            if name:
                warrior_names(name)
        elif warrior == 1:
            dialog = simpledialog
            name = dialog.askstring('Name', 'Enter name for another warrior')
            if name:
                warrior_names(name)
        else:
            msg = messagebox
            tnk = msg.showerror(title='Used', message='Zero slots available.')
    elif tank == 0 and drone == 1:
        if warrior == 0:
            dialog = simpledialog
            name = dialog.askstring('Name', 'Enter name for warrior')
            if name:
                warrior_names(name)

        elif warrior == 1:
            dialog = simpledialog
            name = dialog.askstring('Name', 'Enter name for another warrior')
            if name:
                warrior_names(name)
        else:
            msg = messagebox
            tnk = msg.showerror(title='Used', message='Zero slots available.')
    elif tank == 0 and drone == 2:
        if warrior == 0:
            dialog = simpledialog
            name = dialog.askstring('Name', 'Enter name for warrior')
            if name:
                warrior_names(name)
        else:
            msg = messagebox
            tnk = msg.showerror(title='Used', message='Zero slots available.')
    else:
        msg = messagebox
        tnk = msg.showerror(title='Used', message='Zero slots available.')


def tank_name(name):
    read = csv.CSVRW.reader(csv)

    if read[0]['type'] == '.':

        csv.CSVRW.enter_type(csv, 1, 'tanker', name)

    elif read[1]['type'] == '.':

        csv.CSVRW.enter_type(csv, 2, 'tanker', name)

    elif read[2]['type'] == '.':

        csv.CSVRW.enter_type(csv, 3, 'tanker', name)
    else:
        msg = messagebox
        tnk = msg.showerror(title='Used', message='Zero slots available.')


def drone_names(n):
    read = csv.CSVRW.reader(csv)

    if read[0]['type'] == '.':

        csv.CSVRW.enter_type(csv, 1, 'drone', n)

    elif read[1]['type'] == '.':

        csv.CSVRW.enter_type(csv, 2, 'drone', n)
    elif read[2]['type'] == '.':

        csv.CSVRW.enter_type(csv, 3, 'drone', n)
    else:
        msg = messagebox
        tnk = msg.showerror(title='Used', message='Zero slots available.')


def warrior_names(wnn):
    read = csv.CSVRW.reader(csv)

    if read[0]['type'] == '.':

        csv.CSVRW.enter_type(csv, 1, 'warrior', wnn)

    elif read[1]['type'] == '.':

        csv.CSVRW.enter_type(csv, 2, 'warrior', wnn)

    elif read[2]['type'] == '.':

        csv.CSVRW.enter_type(csv, 3, 'warrior', wnn)
    else:
        msg = messagebox
        tnk = msg.showerror(title='Used', message='Zero slots available.')


main()
