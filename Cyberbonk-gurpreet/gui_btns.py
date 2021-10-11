import attack_conditions as ac
import csv_read_write as csv


def btn_setup(tk, canvas):
    global warrior_hp1, warrior_hp2, warrior_hp3, drone_hp1, drone_hp2, tank_hp1, warrior_hp, drone_hp, tank_hp
    read = csv.CSVRW.reader(csv)
    read_ai = csv.CSVRW.reader_ai(csv)
    p_warrior = 0
    p_drone = 0
    p_tanker = 0

    warrior_name = []
    drone_name = []
    tanker_name = []
    ai_warrior_name = []
    ai_drone_name = []
    ai_tanker_name = []
    for i, ch in enumerate(read):
        if read[i]['type'] == 'warrior':
            p_warrior += 1
            warrior_name.append(read[i]['name'])
            ai_warrior_name.append(read_ai[i]['name'])
        elif read[i]['type'] == 'drone':
            p_drone += 1
            drone_name.append(read[i]['name'])
            ai_drone_name.append(read_ai[i]['name'])
        elif read[i]['type'] == 'tanker':
            p_tanker += 1
            tanker_name.append(read[i]['name'])
            ai_tanker_name.append(read_ai[i]['name'])

    if p_warrior == 3:

        text = tk.Label(canvas.master, text='Warrior ' + warrior_name[0])
        text.place(x=18, y=70)
        text11 = tk.Label(canvas.master, text='Warrior ' + ai_warrior_name[0])
        text11.place(x=820, y=70)
        button1 = tk.Button(canvas.master, text='Ai_W1',
                            command=lambda: ac.AttackConditions.w1(ac, 'ai', tk, canvas, 'ai', 820, 90))
        canvas.create_window(-460, -60, window=button1)

        button2 = tk.Button(canvas.master, text='Ai_W2',
                            command=lambda: ac.AttackConditions.w2(ac, 'ai', tk, canvas, 'ai', 820, 210))
        canvas.create_window(-400, -60, window=button2)

        button3 = tk.Button(canvas.master, text='Ai_W3',
                            command=lambda: ac.AttackConditions.w3(ac, 'ai', tk, canvas, 'ai', 820, 330))
        canvas.create_window(-340, -60, window=button3)

        text = tk.Label(canvas.master, text='Warrior ' + warrior_name[1])
        text.place(x=18, y=190)
        text12 = tk.Label(canvas.master, text='Warrior ' + ai_warrior_name[1])
        text12.place(x=820, y=190)
        button1 = tk.Button(canvas.master, text='Ai_W1',
                            command=lambda: ac.AttackConditions.w1(ac, 'ai', tk, canvas, 'ai', 820, 90))
        canvas.create_window(-460, 60, window=button1)

        button2 = tk.Button(canvas.master, text='Ai_W2',
                            command=lambda: ac.AttackConditions.w2(ac, 'ai', tk, canvas, 'ai', 820, 210))
        canvas.create_window(-400, 60, window=button2)

        button3 = tk.Button(canvas.master, text='Ai_W3',
                            command=lambda: ac.AttackConditions.w3(ac, 'ai', tk, canvas, 'ai', 820, 330))
        canvas.create_window(-340, 60, window=button3)

        text = tk.Label(canvas.master, text='Warrior ' + warrior_name[2])
        text.place(x=18, y=310)
        text13 = tk.Label(canvas.master, text='Warrior ' + ai_warrior_name[2])
        text13.place(x=820, y=310)
        button1 = tk.Button(canvas.master, text='Ai_W1',
                            command=lambda: ac.AttackConditions.w1(ac, 'ai', tk, canvas, 'ai', 820, 90))
        canvas.create_window(-460, 180, window=button1)

        button2 = tk.Button(canvas.master, text='Ai_W2',
                            command=lambda: ac.AttackConditions.w2(ac, 'ai', tk, canvas, 'ai', 820, 210))
        canvas.create_window(-400, 180, window=button2)

        button3 = tk.Button(canvas.master, text='Ai_W3',
                            command=lambda: ac.AttackConditions.w3(ac, 'ai', tk, canvas, 'ai', 820, 330))
        canvas.create_window(-340, 180, window=button3)

    elif p_warrior == 2 and p_drone == 1:
        text = tk.Label(canvas.master, text='Drone User ' + drone_name[0])
        text.place(x=18, y=70)
        text11 = tk.Label(canvas.master, text='Drone User ' + ai_drone_name[0])
        text11.place(x=820, y=70)
        button1 = tk.Button(canvas.master, text='Ai_D1',
                            command=lambda: ac.AttackConditions.d1(ac, 'ai', tk, canvas, 'ai', 820, 90))
        canvas.create_window(-460, -60, window=button1)

        button2 = tk.Button(canvas.master, text='Ai_W1',
                            command=lambda: ac.AttackConditions.d_w1(ac, 'ai', tk, canvas, 'ai', 820, 210))
        canvas.create_window(-400, -60, window=button2)

        button3 = tk.Button(canvas.master, text='Ai_W2',
                            command=lambda: ac.AttackConditions.d_w2(ac, 'ai', tk, canvas, 'ai', 820, 330))
        canvas.create_window(-340, -60, window=button3)

        text = tk.Label(canvas.master, text='Warrior ' + warrior_name[0])
        text.place(x=18, y=190)
        text13 = tk.Label(canvas.master, text='Warrior ' + ai_warrior_name[0])
        text13.place(x=820, y=190)
        button1 = tk.Button(canvas.master, text='Ai_D1',
                            command=lambda: ac.AttackConditions.w_d1(ac, 'ai', tk, canvas, 'ai', 820, 90))
        canvas.create_window(-460, 60, window=button1)

        button2 = tk.Button(canvas.master, text='Ai_W2',
                            command=lambda: ac.AttackConditions.w1(ac, 'ai', tk, canvas, 'ai', 820, 210))
        canvas.create_window(-400, 60, window=button2)

        button3 = tk.Button(canvas.master, text='Ai_W3',
                            command=lambda: ac.AttackConditions.w2(ac, 'ai', tk, canvas, 'ai', 820, 330))
        canvas.create_window(-340, 60, window=button3)

        text = tk.Label(canvas.master, text='Warrior ' + warrior_name[1])
        text.place(x=18, y=310)
        text12 = tk.Label(canvas.master, text='Warrior ' + ai_warrior_name[1])
        text12.place(x=820, y=70)
        button1 = tk.Button(canvas.master, text='Ai_D1',
                            command=lambda: ac.AttackConditions.w_d1(ac, 'ai', tk, canvas, 'ai', 820, 90))
        canvas.create_window(-460, 180, window=button1)

        button2 = tk.Button(canvas.master, text='Ai_W2',
                            command=lambda: ac.AttackConditions.w1(ac, 'ai', tk, canvas, 'ai', 820, 210))
        canvas.create_window(-400, 180, window=button2)

        button3 = tk.Button(canvas.master, text='Ai_W3',
                            command=lambda: ac.AttackConditions.w2(ac, 'ai', tk, canvas, 'ai', 820, 330))
        canvas.create_window(-340, 180, window=button3)

    elif p_warrior == 1 and p_drone == 2:
        text = tk.Label(canvas.master, text='Drone User ' + drone_name[0])
        text.place(x=18, y=70)
        text11 = tk.Label(canvas.master, text='Drone User ' + ai_drone_name[0])
        text11.place(x=820, y=70)
        button1 = tk.Button(canvas.master, text='Ai_D1',
                            command=lambda: ac.AttackConditions.d1(ac, 'ai', tk, canvas, 'ai', 820, 90))
        canvas.create_window(-460, -60, window=button1)

        button2 = tk.Button(canvas.master, text='Ai_D2',
                            command=lambda: ac.AttackConditions.d2(ac, 'ai', tk, canvas, 'ai', 820, 210))
        canvas.create_window(-400, -60, window=button2)

        button3 = tk.Button(canvas.master, text='Ai_W1',
                            command=lambda: ac.AttackConditions.d_w1(ac, 'ai', tk, canvas, 'ai', 820, 330))
        canvas.create_window(-340, -60, window=button3)

        text = tk.Label(canvas.master, text='Drone User ' + drone_name[1])
        text.place(x=18, y=190)
        text13 = tk.Label(canvas.master, text='Drone User ' + ai_drone_name[1])
        text13.place(x=820, y=190)
        button1 = tk.Button(canvas.master, text='Ai_D1',
                            command=lambda: ac.AttackConditions.d1(ac, 'ai', tk, canvas, 'ai', 820, 90))
        canvas.create_window(-460, 60, window=button1)

        button2 = tk.Button(canvas.master, text='Ai_D2',
                            command=lambda: ac.AttackConditions.d2(ac, 'ai', tk, canvas, 'ai', 820, 210))
        canvas.create_window(-400, 60, window=button2)

        button3 = tk.Button(canvas.master, text='Ai_W1',
                            command=lambda: ac.AttackConditions.d_w1(ac, 'ai', tk, canvas, 'ai', 820, 330))
        canvas.create_window(-340, 60, window=button3)

        text = tk.Label(canvas.master, text='Warrior ' + warrior_name[0])
        text.place(x=18, y=310)
        text12 = tk.Label(canvas.master, text='Warrior ' + ai_warrior_name[0])
        text12.place(x=820, y=310)
        button1 = tk.Button(canvas.master, text='Ai_D1',
                            command=lambda: ac.AttackConditions.w_d1(ac, 'ai', tk, canvas, 'ai', 820, 90))
        canvas.create_window(-460, 180, window=button1)

        button2 = tk.Button(canvas.master, text='Ai_D2',
                            command=lambda: ac.AttackConditions.w_d2(ac, 'ai', tk, canvas, 'ai', 820, 210))
        canvas.create_window(-400, 180, window=button2)

        button3 = tk.Button(canvas.master, text='Ai_W1',
                            command=lambda: ac.AttackConditions.w1(ac, 'ai', tk, canvas, 'ai', 820, 330))
        canvas.create_window(-340, 180, window=button3)

    elif p_warrior == 2 and p_tanker == 1:
        text = tk.Label(canvas.master, text='Warrior ' + warrior_name[0])
        text.place(x=18, y=70)
        text11 = tk.Label(canvas.master, text='Warrior ' + ai_warrior_name[0])
        text11.place(x=820, y=70)
        button1 = tk.Button(canvas.master, text='Ai_W1',
                            command=lambda: ac.AttackConditions.w1(ac, 'ai', tk, canvas, 'ai', 820, 90))
        canvas.create_window(-460, -60, window=button1)

        button2 = tk.Button(canvas.master, text='Ai_W2',
                            command=lambda: ac.AttackConditions.w2(ac, 'ai', tk, canvas, 'ai', 820, 210))
        canvas.create_window(-400, -60, window=button2)

        button3 = tk.Button(canvas.master, text='Ai_T',
                            command=lambda: ac.AttackConditions.w_t(ac, 'ai', tk, canvas, 'ai', 820, 330))
        canvas.create_window(-340, -60, window=button3)

        text = tk.Label(canvas.master, text='Warrior ' + warrior_name[1])
        text.place(x=18, y=190)
        text14 = tk.Label(canvas.master, text='Warrior ' + ai_warrior_name[1])
        text14.place(x=820, y=190)
        button1 = tk.Button(canvas.master, text='Ai_W1',
                            command=lambda: ac.AttackConditions.w1(ac, 'ai', tk, canvas, 'ai', 820, 90))
        canvas.create_window(-460, 60, window=button1)

        button2 = tk.Button(canvas.master, text='Ai_W2',
                            command=lambda: ac.AttackConditions.w2(ac, 'ai', tk, canvas, 'ai', 820, 210))
        canvas.create_window(-400, 60, window=button2)

        button3 = tk.Button(canvas.master, text='Ai_T',
                            command=lambda: ac.AttackConditions.w_t(ac, 'ai', tk, canvas, 'ai', 820, 330))
        canvas.create_window(-340, 60, window=button3)

        text = tk.Label(canvas.master, text='Tanker ' + tanker_name[0])
        text.place(x=18, y=310)
        text13 = tk.Label(canvas.master, text='Tanker ' + ai_tanker_name[0])
        text13.place(x=820, y=310)
        button1 = tk.Button(canvas.master, text='Ai_W1',
                            command=lambda: ac.AttackConditions.t_w1(ac, 'ai', tk, canvas, 'ai', 820, 90))
        canvas.create_window(-460, 180, window=button1)

        button2 = tk.Button(canvas.master, text='Ai_W2',
                            command=lambda: ac.AttackConditions.t_w2(ac, 'ai', tk, canvas, 'ai', 820, 210))
        canvas.create_window(-400, 180, window=button2)

        button3 = tk.Button(canvas.master, text='Ai_T',
                            command=lambda: ac.AttackConditions.t(ac, 'ai', tk, canvas, 'ai', 820, 330))
        canvas.create_window(-340, 180, window=button3)

    if p_warrior == 1 and p_tanker == 1 and p_drone == 1:
        text = tk.Label(canvas.master, text='Drone User ' + drone_name[0])
        text.place(x=18, y=70)
        text11 = tk.Label(canvas.master, text='Drone User ' + ai_drone_name[0])
        text11.place(x=820, y=70)
        button1 = tk.Button(canvas.master, text='Ai_D1',
                            command=lambda: ac.AttackConditions.d1(ac, 'ai', tk, canvas, 'ai', 820, 90))
        canvas.create_window(-460, -60, window=button1)

        button2 = tk.Button(canvas.master, text='Ai_W1',
                            command=lambda: ac.AttackConditions.d_w1(ac, 'ai', tk, canvas, 'ai', 820, 210))
        canvas.create_window(-400, -60, window=button2)

        button3 = tk.Button(canvas.master, text='Ai_T',
                            command=lambda: ac.AttackConditions.d_t(ac, 'ai', tk, canvas, 'ai', 820, 330))
        canvas.create_window(-340, -60, window=button3)

        text = tk.Label(canvas.master, text='Warrior ' + warrior_name[0])
        text.place(x=18, y=190)
        text12 = tk.Label(canvas.master, text='Warrior ' + ai_warrior_name[0])
        text12.place(x=820, y=190)
        button1 = tk.Button(canvas.master, text='Ai_D1',
                            command=lambda: ac.AttackConditions.w_d1(ac, 'ai', tk, canvas, 'ai', 820, 90))
        canvas.create_window(-460, 60, window=button1)

        button2 = tk.Button(canvas.master, text='Ai_W1',
                            command=lambda: ac.AttackConditions.w1(ac, 'ai', tk, canvas, 'ai', 820, 210))
        canvas.create_window(-400, 60, window=button2)

        button3 = tk.Button(canvas.master, text='Ai_T',
                            command=lambda: ac.AttackConditions.w_t(ac, 'ai', tk, canvas, 'ai', 820, 330))
        canvas.create_window(-340, 60, window=button3)

        text = tk.Label(canvas.master, text='Tanker ' + tanker_name[0])
        text.place(x=18, y=310)
        text13 = tk.Label(canvas.master, text='Tanker ' + ai_tanker_name[0])
        text13.place(x=820, y=310)
        button1 = tk.Button(canvas.master, text='Ai_D1',
                            command=lambda: ac.AttackConditions.t_d1(ac, 'ai', tk, canvas, 'ai', 820, 90))
        canvas.create_window(-460, 180, window=button1)

        button2 = tk.Button(canvas.master, text='Ai_W1',
                            command=lambda: ac.AttackConditions.t_w1(ac, 'ai', tk, canvas, 'ai', 820, 210))
        canvas.create_window(-400, 180, window=button2)

        button3 = tk.Button(canvas.master, text='Ai_T',
                            command=lambda: ac.AttackConditions.t(ac, 'ai', tk, canvas, 'ai', 820, 330))
        canvas.create_window(-340, 180, window=button3)
