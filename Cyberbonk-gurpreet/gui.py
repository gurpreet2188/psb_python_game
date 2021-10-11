# ref for assets 
# https://ansimuz.itch.io/warped-city
import os
import tkinter as tk
from turtle import Turtle, Screen
import csv_read_write as csv

import time

pos_1 = 0
pos_2 = 0
pos_3 = 0
#  player.........................

turn = 1
num = 0
num1 = 0
num2 = 0
enemy_num = 0
path = os.path.join('assets')

p_warrior = 0
p_drone = 0
p_tanker = 0

# p.................
drone_num1 = 0
drone_num2 = 0
drone_num3 = 0

p_drone_pos = 0
screen = Screen()

canvas = screen.getcanvas()

screen.addshape(os.path.join(path, 'h_base.gif'))
screen.addshape(os.path.join(path, 'h_full.gif'))
screen.addshape(os.path.join(path, 'h_75.gif'))
screen.addshape(os.path.join(path, 'h_50.gif'))
screen.addshape(os.path.join(path, 'h_25.gif'))
screen.addshape(os.path.join(path, 'h_5.gif'))

screen.addshape(os.path.join(path, 'environment.gif'))
screen.addshape('environment.gif')

screen.addshape(os.path.join(path, 'warrior-0.gif'))
screen.addshape(os.path.join(path, 'warrior-1.gif'))
screen.addshape(os.path.join(path, 'warrior-2.gif'))
screen.addshape(os.path.join(path, 'warrior-3.gif'))
screen.addshape(os.path.join(path, 'flipped-warrior0.gif'))
screen.addshape(os.path.join(path, 'flipped-warrior1.gif'))
screen.addshape(os.path.join(path, 'flipped-warrior2.gif'))
screen.addshape(os.path.join(path, 'flipped-warrior3.gif'))
screen.addshape(os.path.join(path, 'tank-resize.gif'))
screen.addshape(os.path.join(path, 'flipped-tank-resize.gif'))

screen.register_shape(os.path.join(path, 'drone-0.gif'))
screen.register_shape(os.path.join(path, 'drone-1.gif'))
screen.register_shape(os.path.join(path, 'drone-2.gif'))
screen.register_shape(os.path.join(path, 'drone-3.gif'))
screen.register_shape(os.path.join(path, 'drone-4.gif'))
screen.register_shape(os.path.join(path, 'drone-5.gif'))

p_warrior_list = ['warrior-0.gif', 'warrior-1.gif', 'warrior-2.gif', 'warrior-3.gif']
warrior_list = ['flipped-warrior0.gif', 'flipped-warrior1.gif', 'flipped-warrior2.gif', 'flipped-warrior3.gif']
drone_list = ['drone-0.gif', 'drone-1.gif', 'drone-2.gif', 'drone-3.gif', 'drone-4.gif', 'drone-5.gif']


class GUI:

    def __init__(self):
        pass

    def turtle_setup(self):
        global screen, p_drone, p_tanker, p_warrior, canvas
        import gui_btns as btns

        screen.setup(1000, 520)
        screen.setworldcoordinates(-20, -20, 20, 12)
        screen.title('Cyberbonk')
        screen.bgcolor('#101010')
        screen.bgpic('environment.gif')
        canvas.itemconfig(screen.bgpic, anchor="s")
        read = csv.CSVRW.reader(csv)
        for i, ch in enumerate(read):
            if read[i]['type'] == 'warrior':
                p_warrior += 1
            elif read[i]['type'] == 'drone':
                p_drone += 1
            elif read[i]['type'] == 'tanker':
                p_tanker += 1

        GUI.setup_players(GUI)
        btns.btn_setup(tk, canvas)

        screen.mainloop()

    def set_players(self, s, shape, x, y):
        global screen
        screen.tracer(False)
        s.penup()
        s.shape(shape)
        s.goto(x, y)
        screen.tracer(True)

    def setup_players(self):
        global p_warrior, p_tanker, p_drone, pos_1, pos_2, pos_3
        if p_warrior == 3:
            GUI.ai_warrior(self)
            player_warrior()
        elif p_drone == 2 and p_warrior == 1:
            pos_1 = True
            pos_2 = True
            animate_drone()
            pos_3 = True
            player_warrior()
            pos_3 = True
            GUI.ai_warrior(self)
        elif p_warrior == 2 and p_tanker == 1:
            pos_1 = True
            pos_2 = True
            GUI.ai_warrior(self)

            pos_1 = True
            pos_2 = True
            player_warrior()

            pos_3 = True
            ai_tank()
        elif p_warrior == 2 and p_drone == 1:
            pos_1 = True
            animate_drone()
            pos_2 = True
            pos_3 = True
            player_warrior()
            pos_2 = True
            pos_3 = True
            GUI.ai_warrior(self)
        elif p_warrior == p_drone == p_tanker:
            pos_1 = True
            animate_drone()
            pos_2 = True
            GUI.ai_warrior(self)
            pos_2 = True
            player_warrior()
            pos_3 = True
            ai_tank()
        elif p_drone == 3:
            animate_drone()

    def stat_show(self, ai_data, p_data, p_ai):
        global canvas
        if p_ai == 'ai':
            status = tk.Label(canvas.master, text=p_data['name'] + ' has damaged ' + ai_data['name'])
            status.place(x=500, y=460)
        elif p_ai == 'p':
            status = tk.Label(canvas.master, text=ai_data['name'] + ' has damaged ' + p_data['name'])
            status.place(x=500, y=480)

    def ai_warrior(self):
        global screen, num, warrior_list, path, pos_1, pos_2, pos_3

        ai = Turtle()
        ai1 = Turtle()
        ai2 = Turtle()
        if p_warrior == 1:
            if pos_1:
                shape_pos(ai, 9, 5.8)
                ai.shape(os.path.join(path, warrior_list[0]))

                pos_1 = False
            elif pos_2:
                shape_pos(ai1, 6, 0.7)
                ai1.shape(os.path.join(path, warrior_list[0]))

                pos_2 = False
            elif pos_3:
                shape_pos(ai2, 8, -4.5)
                ai2.shape(os.path.join(path, warrior_list[0]))

                pos_3 = False
        elif p_warrior == 2:
            if pos_1 and pos_2:
                shape_pos(ai, 9, 5.8)
                ai.shape(os.path.join(path, warrior_list[0]))

                shape_pos(ai1, 6, 0.7)
                ai1.shape(os.path.join(path, warrior_list[0]))

                pos_1 = False
                pos_2 = False
            elif pos_2 and pos_3:
                shape_pos(ai1, 6, 0.7)
                ai1.shape(os.path.join(path, warrior_list[0]))
                shape_pos(ai2, 8, -4.5)
                ai2.shape(os.path.join(path, warrior_list[0]))
                pos_2 = False
                pos_3 = False
        elif p_warrior == 3:
            shape_pos(ai, 9, 5.8)
            ai.shape(os.path.join(path, warrior_list[0]))
            shape_pos(ai1, 6, 0.7)
            ai1.shape(os.path.join(path, warrior_list[0]))
            shape_pos(ai2, 8, -4.5)
            ai2.shape(os.path.join(path, warrior_list[0]))


def player_warrior():
    global screen, p_warrior_list, path, pos_1, pos_2, pos_3, p_warrior

    p = Turtle()
    p1 = Turtle()
    p2 = Turtle()
    if p_warrior == 1:
        # if pos_1:
        #     shape_pos(p, -180, 73)
        #     p.shape(os.path.join(path, p_warrior_list[0]))
        #     # p.frame = num
        #     # warrior_animtion(p, p_warrior_list)
        #     pos_1 = False
        #     pos_2 = False
        #     pos_2 = False
        if pos_2:
            shape_pos(p1, -9, -.3)
            p1.shape(os.path.join(path, p_warrior_list[0]))

        elif pos_3:
            shape_pos(p2, -7, -4.5)
            p2.shape(os.path.join(path, p_warrior_list[0]))

            pos_1 = False
            pos_2 = False
            pos_2 = False
    elif p_warrior == 2:
        if pos_1 and pos_2:
            shape_pos(p, -8.5, 4.7)
            p.shape(os.path.join(path, p_warrior_list[0]))

            shape_pos(p1, -9, -.3)
            p1.shape(os.path.join(path, p_warrior_list[0]))

            pos_1 = False
            pos_2 = False
        elif pos_2 and pos_3:
            shape_pos(p1, -9, -.3)
            p1.shape(os.path.join(path, p_warrior_list[0]))

            shape_pos(p2, -7, -4.5)
            p2.shape(os.path.join(path, p_warrior_list[0]))

            pos_2 = False
            pos_3 = False
    elif p_warrior == 3:
        shape_pos(p, -8.5, 4.7)
        p.shape(os.path.join(path, p_warrior_list[0]))

        shape_pos(p1, -9, -.3)
        p1.shape(os.path.join(path, p_warrior_list[0]))

        shape_pos(p2, -7, -4.5)
        p2.shape(os.path.join(path, p_warrior_list[0]))

    screen.ontimer(player_warrior, 150)


def shape_pos(shape, x, y):
    screen.tracer(False)
    shape.penup()
    shape.goto(x, y)

    screen.tracer(True)


def animate_drone():
    global drone_num1, drone_num2, drone_num3, drone_list, screen, p_drone_pos, p_drone, p_tanker, p_warrior, pos_1, pos_2, pos_3
    p_drone1 = Turtle()
    p_drone2 = Turtle()
    p_drone3 = Turtle()
    ai_drone1 = Turtle()
    ai_drone2 = Turtle()
    ai_drone3 = Turtle()
    if p_drone == 1:
        if pos_1:
            shape_pos(ai_drone1, 9, 4.9)
            ai_drone1.shape(os.path.join(path, drone_list[0]))

            shape_pos(p_drone1, -9, 4.2)
            p_drone1.shape(os.path.join(path, drone_list[4]))

            pos_1 = False
        elif pos_2:
            shape_pos(ai_drone2, 6, 0.4)
            ai_drone2.shape(os.path.join(path, drone_list[0]))

            shape_pos(p_drone2, -8.4, -0.6)
            p_drone2.shape(os.path.join(path, drone_list[4]))

            pos_2 = False
        elif pos_3:
            shape_pos(ai_drone3, 8, -4.7)
            ai_drone3.shape(os.path.join(path, drone_list[0]))

            shape_pos(p_drone3, -7, -4.9)
            p_drone3.shape(os.path.join(path, drone_list[4]))

            pos_3 = False
    elif p_drone == 2:
        if pos_1 and pos_2:
            shape_pos(ai_drone1, 9, 4.9)
            ai_drone1.shape(os.path.join(path, drone_list[0]))

            shape_pos(p_drone1, -9, 4.2)
            p_drone1.shape(os.path.join(path, drone_list[4]))

            shape_pos(ai_drone2, 6, 0.4)
            ai_drone2.shape(os.path.join(path, drone_list[0]))

            shape_pos(p_drone2, -8.4, -0.6)
            p_drone2.shape(os.path.join(path, drone_list[4]))

            pos_1 = False
            pos_2 = False
    elif p_drone == 3:
        shape_pos(ai_drone1, 9, 4.9)
        ai_drone1.shape(os.path.join(path, drone_list[0]))

        shape_pos(p_drone1, -9, 4.2)
        p_drone1.shape(os.path.join(path, drone_list[4]))

        shape_pos(ai_drone2, 6, 0.4)
        ai_drone2.shape(os.path.join(path, drone_list[0]))

        shape_pos(p_drone2, -8.4, -0.6)
        p_drone2.shape(os.path.join(path, drone_list[4]))

        shape_pos(ai_drone3, 8, -4.7)
        ai_drone3.shape(os.path.join(path, drone_list[0]))

        shape_pos(p_drone3, -7, -4.9)
        p_drone3.shape(os.path.join(path, drone_list[4]))


def ai_tank():
    global pos_1, pos_2, pos_3, p_tanker, path
    ai_tankk = Turtle()
    p_tankk = Turtle()
    if p_tanker == 1:
        if pos_3:
            shape_pos(ai_tankk, 8, -5)
            ai_tankk.shape(os.path.join(path, 'tank-resize.gif'))
            shape_pos(p_tankk, -8, -5)
            p_tankk.shape(os.path.join(path, 'flipped-tank-resize.gif'))


def ai():
    global canvas, screen, p_warrior, p_drone
    import ai as aii

    aii.Ai.manage(aii, tk, canvas, p_drone, p_warrior, p_tanker)
    time.sleep(.1)  # add delay for csv files to update
