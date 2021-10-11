import csv_read_write as csv
import attack as attack
import gui as gui
import save_log as log



class AttackConditions:
    def __init__(self):
        pass

    def w1(self, p_ai, tk, canvas, pai, a, b):

        w_hp = csv.CSVRW.reader_warrior_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)

        if w_hp[0]:
            whp = int(w_hp[0])
            wdhp = attack.Attack.warrior_at_warrior(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[3][0]), p_ai, wdhp)

            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[3][0])]['name'] + ' damaged ' + p_data[int(w_hp[3][0])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[3][0])]['name'] + ' damaged ' + ai_data[int(w_hp[3][0])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def w2(self, p_ai, tk, canvas, pai, a, b):

        w_hp = csv.CSVRW.reader_warrior_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)
        if w_hp[1]:
            whp = int(w_hp[1])
            wdhp = attack.Attack.warrior_at_warrior(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[3][1]), p_ai, wdhp)
            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[3][1])]['name'] + ' damaged ' + p_data[int(w_hp[3][1])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[3][1])]['name'] + ' damaged ' + ai_data[int(w_hp[3][1])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def w3(self, p_ai, tk, canvas, pai, a, b):

        w_hp = csv.CSVRW.reader_warrior_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)
        if w_hp[2]:
            whp = int(w_hp[2])
            wdhp = attack.Attack.warrior_at_warrior(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[3][2]), p_ai, wdhp)

            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[3][2])]['name'] + ' damaged ' + p_data[int(w_hp[3][2])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[3][2])]['name'] + ' damaged ' + ai_data[int(w_hp[3][2])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def d1(self, p_ai, tk, canvas, pai, a, b):
        w_hp = csv.CSVRW.reader_drone_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)
        if w_hp[0]:
            whp = int(w_hp[0])
            wdhp = attack.Attack.drone_at_drone(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[2][0]), p_ai, wdhp)
            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[2][0])]['name'] + ' damaged ' + p_data[int(w_hp[2][0])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[2][0])]['name'] + ' damaged ' + ai_data[int(w_hp[2][0])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def d2(self, p_ai, tk, canvas, pai, a, b):
        w_hp = csv.CSVRW.reader_drone_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)
        if w_hp[1]:
            whp = int(w_hp[1])
            wdhp = attack.Attack.drone_at_drone(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[2][1]), p_ai, wdhp)
            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[2][1])]['name'] + ' damaged ' + p_data[int(w_hp[2][1])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[2][1])]['name'] + ' damaged ' + ai_data[int(w_hp[2][1])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def d_w1(self, p_ai, tk, canvas, pai, a, b):
        w_hp = csv.CSVRW.reader_warrior_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)

        if w_hp[0]:
            whp = int(w_hp[0])
            wdhp = attack.Attack.drone_at_warrior(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[3][0]), p_ai, wdhp)

            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[3][0])]['name'] + ' damaged ' + p_data[int(w_hp[3][0])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[3][0])]['name'] + ' damaged ' + ai_data[int(w_hp[3][0])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def d_w2(self, p_ai, tk, canvas, pai, a, b):
        w_hp = csv.CSVRW.reader_warrior_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)
        if w_hp[1]:
            whp = int(w_hp[1])
            wdhp = attack.Attack.drone_at_warrior(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[3][1]), p_ai, wdhp)
            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[3][1])]['name'] + ' damaged ' + p_data[int(w_hp[3][1])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[3][1])]['name'] + ' damaged ' + ai_data[int(w_hp[3][1])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def d_w3(self, p_ai, tk, canvas, pai, a, b):
        w_hp = csv.CSVRW.reader_warrior_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)
        if w_hp[2]:
            whp = int(w_hp[2])
            wdhp = attack.Attack.drone_at_warrior(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[3][2]), p_ai, wdhp)
            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[3][2])]['name'] + ' damaged ' + p_data[int(w_hp[3][2])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[3][2])]['name'] + ' damaged ' + ai_data[int(w_hp[3][2])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def w_d1(self, p_ai, tk, canvas, pai, a, b):
        w_hp = csv.CSVRW.reader_drone_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)
        if w_hp[0]:
            whp = int(w_hp[0])
            wdhp = attack.Attack.warrior_at_drone(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[2][0]), p_ai, wdhp)
            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[2][0])]['name'] + ' damaged ' + p_data[int(w_hp[2][0])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[2][0])]['name'] + ' damaged ' + ai_data[int(w_hp[2][0])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def w_d2(self, p_ai, tk, canvas, pai, a, b):
        w_hp = csv.CSVRW.reader_drone_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)
        if w_hp[1]:
            whp = int(w_hp[1])
            wdhp = attack.Attack.warrior_at_drone(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[2][1]), p_ai, wdhp)
            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[2][1])]['name'] + ' damaged ' + p_data[int(w_hp[2][1])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[2][1])]['name'] + ' damaged ' + ai_data[int(w_hp[2][1])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def w_t(self, p_ai, tk, canvas, pai, a, b):
        w_hp = csv.CSVRW.reader_tank_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)

        if w_hp[0]:
            whp = int(w_hp[0])
            wdhp = attack.Attack.warrior_at_tank(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[1][0]), p_ai, wdhp)
            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[1][0])]['name'] + ' damaged ' + p_data[int(w_hp[1][0])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[1][0])]['name'] + ' damaged ' + ai_data[int(w_hp[1][0])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def d_t(self, p_ai, tk, canvas, pai, a, b):
        w_hp = csv.CSVRW.reader_tank_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)
        if w_hp[0]:
            whp = int(w_hp[0])
            wdhp = attack.Attack.drone_at_tank(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[1][0]), p_ai, wdhp)
            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[1][0])]['name'] + ' damaged ' + p_data[int(w_hp[1][0])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[1][0])]['name'] + ' damaged ' + ai_data[int(w_hp[1][0])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def t_d1(self, p_ai, tk, canvas, pai, a, b):
        w_hp = csv.CSVRW.reader_drone_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)
        if w_hp[0]:
            whp = int(w_hp[0])
            wdhp = attack.Attack.tank_at_drone(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[2][0]), p_ai, wdhp)
            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[2][0])]['name'] + ' damaged ' + p_data[int(w_hp[2][0])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[2][0])]['name'] + ' damaged ' + ai_data[int(w_hp[2][0])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def t_d2(self, p_ai, tk, canvas, pai, a, b):
        w_hp = csv.CSVRW.reader_drone_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)
        if w_hp[1]:
            whp = int(w_hp[1])
            wdhp = attack.Attack.tank_at_drone(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[2][1]), p_ai, wdhp)
            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[2][1])]['name'] + ' damaged ' + p_data[int(w_hp[2][1])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[2][1])]['name'] + ' damaged ' + ai_data[int(w_hp[2][1])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def t_w1(self, p_ai, tk, canvas, pai, a, b):
        w_hp = csv.CSVRW.reader_warrior_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)
        if w_hp[0]:
            whp = int(w_hp[0])
            wdhp = attack.Attack.warrior_at_warrior(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[3][0]), p_ai, wdhp)
            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[3][0])]['name'] + ' damaged ' + p_data[int(w_hp[3][0])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[3][0])]['name'] + ' damaged ' + ai_data[int(w_hp[3][0])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def t_w2(self, p_ai, tk, canvas, pai, a, b):
        w_hp = csv.CSVRW.reader_warrior_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)
        if w_hp[1]:
            whp = int(w_hp[1])
            wdhp = attack.Attack.warrior_at_warrior(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[3][1]), p_ai, wdhp)
            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[3][1])]['name'] + ' damaged ' + p_data[int(w_hp[3][1])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[3][1])]['name'] + ' damaged ' + ai_data[int(w_hp[3][1])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def t_w3(self, p_ai, tk, canvas, pai, a, b):
        w_hp = csv.CSVRW.reader_warrior_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)
        if w_hp[2]:
            whp = int(w_hp[2])
            wdhp = attack.Attack.warrior_at_warrior(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[3][2]), p_ai, wdhp)
            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[3][2])]['name'] + ' damaged ' + p_data[int(w_hp[3][2])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[3][2])]['name'] + ' damaged ' + ai_data[int(w_hp[3][2])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass

    def t(self, p_ai, tk, canvas, pai, a, b):
        w_hp = csv.CSVRW.reader_tank_hp(csv, p_ai)
        ai_data = csv.CSVRW.reader_ai(csv)
        p_data = csv.CSVRW.reader(csv)
        if w_hp[0]:
            whp = int(w_hp[0])
            wdhp = attack.Attack.tank_at_tank(attack, whp)
            csv.CSVRW.enter_hp(csv, int(w_hp[1][0]), p_ai, wdhp)
            if pai == 'p':
                read = csv.CSVRW.reader(csv)
                text1 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                text1.place(x=a, y=b)
                text3 = tk.Label(canvas.master,
                                 text=ai_data[int(w_hp[1][0])]['name'] + ' damaged ' + p_data[int(w_hp[1][0])][
                                     'name'] + ' and now hp is ' + str(wdhp) + "/100")
                text3.place(x=700, y=410)
                log.Log.log_file(log, text3.cget("text"))
            elif pai == 'ai':
                if whp > 0:
                    read = csv.CSVRW.reader_ai(csv)
                    text2 = tk.Label(canvas.master, text='hp ' + str(wdhp) + "/100")
                    text2.place(x=a, y=b)
                    text4 = tk.Label(canvas.master,
                                     text=p_data[int(w_hp[1][0])]['name'] + ' damaged ' + ai_data[int(w_hp[1][0])][
                                         'name'] + ' and now hp is ' + str(wdhp) + "/100")
                    text4.place(x=100, y=410)
                    log.Log.log_file(log, text4.cget("text"))

                    gui.ai()
                elif whp < 0:
                    pass
