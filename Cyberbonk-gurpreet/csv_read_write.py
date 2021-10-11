import csv
from tempfile import NamedTemporaryFile
import random

t_file = NamedTemporaryFile(mode='w', delete=False)


class CSVRW:
    def __init__(self):
        pass

    def read_weapons(self):
        w = []
        with open('indexs.csv', 'r') as csv_f:
            w_csv = csv.reader(csv_f, delimiter=',')
            line = 0
            for row in w_csv:
                if line == 0:
                    line += 1
                else:
                    w.append(row)
                    line += 1
            csv_f.close()
        return w

    def writer(self, top, data, option, p_ai):
        if p_ai == 'p':
            with open('p_info.csv', "w", newline="") as csvfile:
                if option == "write":

                    info = csv.writer(csvfile)
                    info.writerow(top)
                    for x in data:
                        info.writerow(x)
                elif option == "update":
                    writer = csv.DictWriter(csvfile, fieldnames=top)
                    writer.writeheader()
                    writer.writerows(data)
                else:
                    print("Option is not known")
            csvfile.close()
        elif p_ai == 'ai':
            with open('ai_info.csv', "w", newline="") as csvfile:
                if option == "write":

                    info = csv.writer(csvfile)
                    info.writerow(top)
                    for x in data:
                        info.writerow(x)
                elif option == "update":
                    writer = csv.DictWriter(csvfile, fieldnames=top)
                    writer.writeheader()
                    writer.writerows(data)
                else:
                    print("Option is not known")
            csvfile.close()

    def enter_name(self, num, name, p_ai):
        if p_ai == 'p':
            with open('p_info.csv', newline="") as file:
                read = [row for row in csv.DictReader(file)]
                name_str = str(name)
                if num == 1:
                    read[0]['name'] = name
                elif num == 2:
                    read[1]['name'] = name
                elif num == 3:
                    read[2]['name'] = name

            readHeader = read[0].keys()
            CSVRW.writer(CSVRW, readHeader, read, "update", 'p')
            file.close()
        elif p_ai == 'ai':
            with open('p_info.csv', newline="") as file:
                read = [row for row in csv.DictReader(file)]
                name_str = str(name)
                if num == 1:
                    read[0]['name'] = name
                elif num == 2:
                    read[1]['name'] = name
                elif num == 3:
                    read[2]['name'] = name

            readHeader = read[0].keys()
            CSVRW.writer(CSVRW, readHeader, read, "update", 'ai')
            file.close()

    def enter_hp(self, index, p_ai, hp):
        if p_ai == 'p':
            with open('p_info.csv', newline="") as file:
                read = [row for row in csv.DictReader(file)]

                hp_str = str(hp)
                if index == 0:
                    read[0]['hp'] = hp_str
                elif index == 1:
                    read[1]['hp'] = hp_str
                elif index == 2:
                    read[2]['hp'] = hp_str


            readHeader = read[0].keys()
            CSVRW.writer(CSVRW, readHeader, read, "update", 'p')
            file.close()
        elif p_ai == 'ai':
            with open('ai_info.csv', newline="") as file:
                read = [row for row in csv.DictReader(file)]

                hp_str = str(hp)
                if index == 0:
                    read[0]['hp'] = hp_str
                elif index == 1:
                    read[1]['hp'] = hp_str
                elif index == 2:
                    read[2]['hp'] = hp_str

            readHeader = read[0].keys()
            CSVRW.writer(CSVRW, readHeader, read, "update", 'ai')
            file.close()

    def enter_index(self, num, index, name):
        # if p_ai == 'p':
        with open('p_info.csv', newline="") as file:
            read = [row for row in csv.DictReader(file)]

            n_str = str(name)
            if num == 1:
                read[0]['index'] = index
                read[0]['name'] = n_str
            elif num == 2:
                read[1]['index'] = index
                read[1]['name'] = n_str
            elif num == 3:
                read[2]['index'] = index
                read[2]['name'] = n_str


            readHeader = read[0].keys()
            CSVRW.writer(CSVRW, readHeader, read, "update", 'p')
            file.close()
            # elif p_ai == 'ai':

        file.close()
        with open('ai_info.csv', newline="") as file:
            read = [row for row in csv.DictReader(file)]

            n_str = str(name)
            randnum1 = random.randrange(555, 777)
            randnum2 = random.randrange(111, 333)
            randnum3 = random.randrange(888, 999)
            ai1 = 'ai' + str(randnum1)
            ai2 = 'ai' + str(randnum2)
            ai3 = 'ai' + str(randnum3)
            if num == 1:
                read[0]['index'] = index
                read[0]['name'] = ai1
            elif num == 2:
                read[1]['index'] = index
                read[1]['name'] = ai2
            elif num == 3:
                read[2]['index'] = index
                read[2]['name'] = ai3


        readHeader = read[0].keys()
        CSVRW.writer(CSVRW, readHeader, read, "update", 'ai')
        file.close()

    def reader_hp(self, num):
        with open('p_info.csv', newline="") as file:
            read = [row for row in csv.DictReader(file)]
            file.close()
            return int(read[num]['hp'])

    def reader(self):
        with open('p_info.csv', newline="") as file:
            read = [row for row in csv.DictReader(file)]
            file.close()
            return read

    def reader_ai(self):
        with open('ai_info.csv', newline="") as file:
            read = [row for row in csv.DictReader(file)]
            file.close()
            return read

    def clean(self):
        with open('p_info.csv', 'w') as csv_w:
            w_csv = csv.writer(csv_w, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            w_csv.writerow(['num', 'name', 'type', 'damage', 'hp'])
            w_csv.writerow(['1', '.', '.', '.', '100'])
            w_csv.writerow(['2', '.', '.', '.', '100'])
            w_csv.writerow(['3', '.', '.', '.', '100'])
            csv_w.close()
        with open('ai_info.csv', 'w') as csv_w:
            w_csv = csv.writer(csv_w, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            w_csv.writerow(['num', 'name', 'type', 'damage', 'hp'])
            w_csv.writerow(['0', '.', '.', '.', '100'])
            w_csv.writerow(['1', '.', '.', '.', '100'])
            w_csv.writerow(['2', '.', '.', '.', '100'])
            csv_w.close()

    def reader_drone_hp(self, p_ai):
        if p_ai == 'p':
            read = CSVRW.reader(CSVRW)
        elif p_ai == 'ai':
            read = CSVRW.reader_ai(CSVRW)
        drone = 0

        index = []
        drone_hp = []
        drone_hp1 = False
        drone_hp2 = False
        for i, ch in enumerate(read):
            if read[i]['type'] == 'drone':
                drone += 1
                index.append(i)
                drone_hp.append(read[i]['hp'])
        if drone == 1:
            drone_hp1 = drone_hp[0]
        elif drone == 2:
            drone_hp1 = drone_hp[0]
            drone_hp2 = drone_hp[1]

        return drone_hp1, drone_hp2, index

    def reader_warrior_hp(self, p_ai):
        if p_ai == 'p':
            read = CSVRW.reader(CSVRW)
        elif p_ai == 'ai':
            read = CSVRW.reader_ai(CSVRW)
        warrior = 0
        index = []
        warrior_hp = []
        warrior_hp1 = False
        warrior_hp2 = False
        warrior_hp3 = False
        for i, ch in enumerate(read):
            if read[i]['type'] == 'warrior':
                warrior += 1
                index.append(i)
                warrior_hp.append(read[i]['hp'])
        if warrior == 1:
            warrior_hp1 = int(warrior_hp[0])
        elif warrior == 2:
            warrior_hp1 = int(warrior_hp[1])
            warrior_hp2 = int(warrior_hp[1])
        elif warrior == 3:
            warrior_hp1 = int(warrior_hp[0])
            warrior_hp2 = int(warrior_hp[1])
            warrior_hp3 = int(warrior_hp[2])

        return warrior_hp1, warrior_hp2, warrior_hp3, index

    def reader_tank_hp(self, p_ai):
        if p_ai == 'p':
            read = CSVRW.reader(CSVRW)
        elif p_ai == 'ai':
            read = CSVRW.reader_ai(CSVRW)
        tank = 0
        index = []
        tank_hp = []
        tank_hp1 = False

        for i, ch in enumerate(read):
            if read[i]['type'] == 'tanker':
                tank += 1
                index.append(i)
                tank_hp.append(read[i]['hp'])
        if tank == 1:
            tank_hp1 = tank_hp[0]

        return tank_hp1, index

    def enter_type(self, num, type, name):

        with open('p_info.csv', newline="") as file:
            read = [row for row in csv.DictReader(file)]

            n_str = str(name)
            if num == 1:
                read[0]['type'] = type
                read[0]['name'] = n_str
            elif num == 2:
                read[1]['type'] = type
                read[1]['name'] = n_str
            elif num == 3:
                read[2]['type'] = type
                read[2]['name'] = n_str


            readHeader = read[0].keys()
            CSVRW.writer(CSVRW, readHeader, read, "update", 'p')
            file.close()


        file.close()
        with open('ai_info.csv', newline="") as file:
            read = [row for row in csv.DictReader(file)]

            n_str = str(name)
            randnum1 = random.randrange(555, 777)
            randnum2 = random.randrange(111, 333)
            randnum3 = random.randrange(888, 999)
            ai1 = 'ai' + str(randnum1)
            ai2 = 'ai' + str(randnum2)
            ai3 = 'ai' + str(randnum3)
            if num == 1:
                read[0]['type'] = type
                read[0]['name'] = ai1
            elif num == 2:
                read[1]['type'] = type
                read[1]['name'] = ai2
            elif num == 3:
                read[2]['type'] = type
                read[2]['name'] = ai3


        readHeader = read[0].keys()
        CSVRW.writer(CSVRW, readHeader, read, "update", 'ai')
        file.close()
