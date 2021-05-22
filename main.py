import random, time, os, schedule
import datetime as dt
#This will offset the server time on heroku it is UTC+0, Change this accordingly.
utc_timezone = +8
#Time the script will be ran
run_time = '06:30'

tt = dt.datetime.strptime(run_time, '%H:%M')
ha = dt.timedelta(hours = utc_timezone)
lt = tt + ha
fot = lt.strftime("%H:%M")

def job():
    randomSleep = random.randint(10,300)
    print("Sleeping for: %ds" % randomSleep)
    time.sleep(randomSleep)
    exec(open('./run.py').read())
    rs = True

schedule.every().day.at(fot).do(job)

print("Script Started")

while True:
    schedule.run_pending()
    time.sleep(10)
