import random, time
import datetime as dt
#This will offset the server time on heroku it is UTC+0, Change this accordingly.
utc_timezone = +8
#Time the script will be ran
run_time = '06:00'

def job():
    randomSleep = random.randint(10,300)
    print("Sleeping for: %ds" % randomSleep)
    time.sleep(randomSleep)
    exec(open('./genshin-os.py').read())

print("Script Started")

while True:
    st = dt.datetime.now()
    years = st.strftime("%d/%m/%Y")
    tme = years + " " + run_time
    tt = dt.datetime.strptime(tme, "%d/%m/%Y %H:%M")
    oneday = dt.timedelta(days = 1)
    hoursremoved = dt.timedelta(hours = utc_timezone)
    lrt = tt - hoursremoved

    if lrt < st:
        runtime = lrt + oneday
        runin = runtime - st
        zzz = runin.seconds

    elif lrt > st:
        runin = lrt - st
        zzz = runin.seconds

    time.sleep(zzz)
    job()
