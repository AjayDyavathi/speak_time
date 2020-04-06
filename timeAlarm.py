import datetime
import os
import time as t


def getTime():
    now = datetime.datetime.now()
    # print(now.time())
    return str(now.time())


def sayTime(hours, minutes):
    if int(hours) > 12:
        hours = int(hours) - 12
        os.system('say The time is {} {} PM'.format(hours, minutes))
    else:
        os.system('say The time is {} {} AM'.format(hours, minutes))


# Interval in minutes
interval = 1

while True:
    time = getTime()
    hours = time.split(':')[0]
    time = time.split(':')[1]
    minutes = time.split(':')[0]
    if int(minutes) % interval == 0:
        sayTime(hours, minutes)
        t.sleep(60)
