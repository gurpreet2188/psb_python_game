import csv_read_write as csv
import attack_conditions as ac
import random


class Ai:  # aka dumb Ai....
    def __init__(self):
        pass

    def manage(self, tk, canvas, p_drone, p_warrior, p_tanker):

        # drone_hp1 = 1
        # drone_hp2 = 1
        # ai_drone_hp1 = 1
        # ai_drone_hp2 = 1
        # ai_warrior_hp1 = 1
        # ai_warrior_hp2 = 1
        # ai_warrior_hp3 = 1
        # ai_tank_hp1 = 1
        # warrior_hp1 = 1
        # warrior_hp2 = 1
        # warrior_hp3 = 1

        drone_hp = csv.CSVRW.reader_drone_hp(csv, 'p')
        warrior_hp = csv.CSVRW.reader_warrior_hp(csv, 'p')
        tank_hp = csv.CSVRW.reader_tank_hp(csv, 'p')

        ai_drone_hp = csv.CSVRW.reader_drone_hp(csv, 'ai')
        ai_warrior_hp = csv.CSVRW.reader_warrior_hp(csv, 'ai')
        ai_tank_hp = csv.CSVRW.reader_tank_hp(csv, 'ai')

        if p_drone == 2 and p_warrior == 1:
            # print(drone_hp1, warrior_hp1, tank_hp1)

            drone_hp1 = int(drone_hp[0])
            drone_hp2 = int(drone_hp[1])
            ai_drone_hp1 = int(ai_drone_hp[0])
            ai_drone_hp2 = int(ai_drone_hp[1])

            ai_warrior_hp1 = int(ai_warrior_hp[0])
            warrior_hp1 = int(warrior_hp[0])

            randnum = random.randrange(3)
            if ai_drone_hp1 >= 0 or ai_drone_hp2 >= 0 or ai_warrior_hp1 >= 0:

                if randnum == 0 and drone_hp1 >= 50:
                    ac.AttackConditions.d1(ac, 'p', tk, canvas, 'p', 18, 100)
                elif randnum == 1 and drone_hp2 >= 50:
                    ac.AttackConditions.d2(ac, 'p', tk, canvas, 'p', 18, 210)
                elif randnum == 2 and warrior_hp1 >= 50:
                    ac.AttackConditions.w1(ac, 'p', tk, canvas, 'p', 18, 330)
                elif drone_hp1 >= 0:
                    ac.AttackConditions.d1(ac, 'p', tk, canvas, 'p', 18, 100)
                elif drone_hp2 >= 0:
                    ac.AttackConditions.d2(ac, 'p', tk, canvas, 'p', 18, 210)
                elif warrior_hp1 >= 0:
                    ac.AttackConditions.w1(ac, 'p', tk, canvas, 'p', 18, 330)
            elif warrior_hp1 <= 0 and drone_hp1 <= 0 and drone_hp2 <= 0:

                text5 = tk.Label(canvas.master,
                                 text='**!!! Ai Won !!!**')
                text5.place(x=400, y=450)

            elif ai_drone_hp1 <= 0 and ai_drone_hp2 <= 0 and ai_warrior_hp1 <= 0:

                text5 = tk.Label(canvas.master,
                                 text='**!!! You Won !!!**')
                text5.place(x=400, y=450)
            print(warrior_hp1, drone_hp1, drone_hp2, ai_warrior_hp1, ai_drone_hp2, ai_drone_hp1)


        elif p_drone == 1 and p_warrior == 2:

            warrior_hp1 = int(warrior_hp[0])
            warrior_hp2 = int(warrior_hp[1])
            ai_warrior_hp1 = int(ai_warrior_hp[0])
            ai_warrior_hp2 = int(ai_warrior_hp[1])

            drone_hp1 = int(drone_hp[0])
            ai_drone_hp1 = int(ai_drone_hp[0])

            randnum = random.randrange(4)
            if ai_drone_hp1 >= 0 or ai_warrior_hp2 >= 0 or ai_warrior_hp1 >= 0:

                if (randnum == 0 or randnum == 3) and drone_hp1 >= 50:
                    ac.AttackConditions.d1(ac, 'p', tk, canvas, 'p', 18, 100)
                elif randnum == 1 and warrior_hp2 >= 50:
                    ac.AttackConditions.w2(ac, 'p', tk, canvas, 'p', 18, 330)
                elif randnum == 2 and warrior_hp1 >= 50:
                    ac.AttackConditions.w1(ac, 'p', tk, canvas, 'p', 18, 210)
                elif drone_hp1 >= 0:
                    ac.AttackConditions.d1(ac, 'p', tk, canvas, 'p', 18, 100)
                elif warrior_hp2 >= 0:
                    ac.AttackConditions.w2(ac, 'p', tk, canvas, 'p', 18, 330)
                elif warrior_hp1 >= 0:
                    ac.AttackConditions.w1(ac, 'p', tk, canvas, 'p', 18, 210)
            elif warrior_hp1 <= 0 and drone_hp1 <= 0 and warrior_hp2 <= 0:
                text5 = tk.Label(canvas.master,
                                 text='**!!! Ai Won !!!**')
                text5.place(x=400, y=450)

            elif ai_drone_hp1 <= 0 and ai_warrior_hp2 <= 0 and ai_warrior_hp1 <= 0:
                text5 = tk.Label(canvas.master,
                                 text='**!!! You Won !!!**')
                text5.place(x=400, y=450)
            print(warrior_hp1, drone_hp1, warrior_hp2, ai_drone_hp1, ai_warrior_hp1, ai_warrior_hp2)
        elif p_tanker == 1 and p_warrior == 2:

            warrior_hp1 = int(warrior_hp[0])
            warrior_hp2 = int(warrior_hp[1])
            ai_warrior_hp1 = int(ai_warrior_hp[0])
            ai_warrior_hp2 = int(ai_warrior_hp[1])

            tank_hp1 = int(tank_hp[0])
            ai_tank_hp1 = int(ai_tank_hp[0])

            randnum = random.randrange(4)
            if ai_tank_hp1 >= 0 or ai_warrior_hp2 >= 0 or ai_warrior_hp1 >= 0:

                if (randnum == 0 or randnum == 3) and tank_hp1 >= 50:
                    ac.AttackConditions.t(ac, 'p', tk, canvas, 'p', 18, 330)
                elif randnum == 1 and warrior_hp2 >= 50:
                    ac.AttackConditions.w2(ac, 'p', tk, canvas, 'p', 18, 210)
                elif randnum == 2 and warrior_hp1 >= 50:
                    ac.AttackConditions.w1(ac, 'p', tk, canvas, 'p', 18, 100)
                elif tank_hp1 >= 0:
                    ac.AttackConditions.t(ac, 'p', tk, canvas, 'p', 18, 330)
                elif warrior_hp2 >= 0:
                    ac.AttackConditions.w2(ac, 'p', tk, canvas, 'p', 18, 210)
                elif warrior_hp1 >= 0:
                    ac.AttackConditions.w1(ac, 'p', tk, canvas, 'p', 18, 100)
            elif warrior_hp1 <= 0 and tank_hp1 <= 0 and warrior_hp2 <= 0:
                text5 = tk.Label(canvas.master,
                                 text='**!!! Ai Won !!!**')
                text5.place(x=400, y=450)

            elif ai_tank_hp1 <= 0 and warrior_hp2 <= 0 and ai_warrior_hp1 <= 0:
                text5 = tk.Label(canvas.master,
                                 text='**!!! You Won !!!**')
                text5.place(x=400, y=450)
            print(warrior_hp1, warrior_hp2, tank_hp1, ai_warrior_hp1, ai_warrior_hp2, ai_tank_hp1)


        elif p_warrior == 3:

            warrior_hp1 = int(warrior_hp[0])
            warrior_hp2 = int(warrior_hp[1])
            warrior_hp3 = int(warrior_hp[2])
            ai_warrior_hp1 = int(ai_warrior_hp[0])
            ai_warrior_hp2 = int(ai_warrior_hp[1])
            ai_warrior_hp3 = int(ai_warrior_hp[2])

            randnum = random.randrange(3)
            if ai_warrior_hp1 >= 0 or ai_warrior_hp2 >= 0 or ai_warrior_hp3 >= 0:

                if randnum == 0 and warrior_hp1 >= 50:
                    ac.AttackConditions.w1(ac, 'p', tk, canvas, 'p', 18, 100)
                elif randnum == 1 and warrior_hp2 >= 50:
                    ac.AttackConditions.w2(ac, 'p', tk, canvas, 'p', 18, 210)
                elif randnum == 2 and warrior_hp3 >= 50:
                    ac.AttackConditions.w3(ac, 'p', tk, canvas, 'p', 18, 330)
                elif warrior_hp3 >= 0:
                    ac.AttackConditions.w3(ac, 'p', tk, canvas, 'p', 18, 330)
                elif warrior_hp2 >= 0:
                    ac.AttackConditions.w2(ac, 'p', tk, canvas, 'p', 18, 210)
                elif warrior_hp1 >= 0:
                    ac.AttackConditions.w1(ac, 'p', tk, canvas, 'p', 18, 100)
            elif warrior_hp3 <= 0 and warrior_hp1 <= 0 and warrior_hp2 <= 0:
                text5 = tk.Label(canvas.master,
                                 text='**!!! Ai Won !!!**')
                text5.place(x=400, y=450)

            elif ai_warrior_hp1 <= 0 and ai_warrior_hp2 <= 0 and ai_warrior_hp3 <= 0:
                text5 = tk.Label(canvas.master,
                                 text='**!!! You Won !!!**')
                text5.place(x=400, y=450)
            print(warrior_hp3, warrior_hp1, warrior_hp2, ai_warrior_hp1,ai_warrior_hp2, ai_warrior_hp3)


        elif p_warrior == 1 and p_drone == 1 and p_tanker == 1:

            warrior_hp1 = int(warrior_hp[0])
            tank_hp1 = int(tank_hp[0])
            drone_hp1 = int(drone_hp[0])
            ai_drone_hp1 = int(ai_drone_hp[0])
            ai_tank_hp1 = int(ai_tank_hp[0])
            ai_warrior_hp1 = int(ai_warrior_hp[0])

            randnum = random.randrange(4)
            if ai_tank_hp1 >= 0 or ai_warrior_hp1 >= 0 or ai_drone_hp1 >= 0:

                if randnum == 0 and drone_hp1 >= 50:
                    ac.AttackConditions.d1(ac, 'p', tk, canvas, 'p', 18, 100)
                elif randnum == 1 and warrior_hp1 >= 50:
                    ac.AttackConditions.w1(ac, 'p', tk, canvas, 'p', 18, 210)
                elif (randnum == 2 or randnum == 3) and tank_hp1 >= 50:
                    ac.AttackConditions.t(ac, 'p', tk, canvas, 'p', 18, 330)

                elif drone_hp1 >= 0:
                    ac.AttackConditions.d1(ac, 'p', tk, canvas, 'p', 18, 100)
                elif warrior_hp1 >= 0:
                    ac.AttackConditions.w1(ac, 'p', tk, canvas, 'p', 18, 210)
                elif tank_hp1 >= 0:
                    ac.AttackConditions.t(ac, 'p', tk, canvas, 'p', 18, 330)

            elif drone_hp1 <= 0 and warrior_hp1 <= 0 and tank_hp1 <= 0:
                text5 = tk.Label(canvas.master,
                                 text='**!!! Ai Won !!!**')
                text5.place(x=400, y=450)

            elif ai_tank_hp1 <= 0 and ai_drone_hp1 <= 0 and ai_warrior_hp1 <= 0:
                text5 = tk.Label(canvas.master,
                                 text='**!!! You Won !!!**')
                text5.place(x=400, y=450)

            print(drone_hp1, warrior_hp1, tank_hp1, ai_warrior_hp1,ai_drone_hp1, ai_tank_hp1)
