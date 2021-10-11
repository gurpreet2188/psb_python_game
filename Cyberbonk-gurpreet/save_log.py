from datetime import datetime


class Log:

    def __init__(self):
        pass

    def log_file(self, text):
        f = open('log.txt', 'a')
        now = datetime.now()
        c_date = str(now.date())
        c_time = str(now.strftime("%H:%M:%S"))
        f.write(c_date + ' ' + c_time + '\n           ' + text + '\n')
        f.close()
