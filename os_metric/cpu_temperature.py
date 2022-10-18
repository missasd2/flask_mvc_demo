import psutil
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)
battery = psutil.sensors_battery()
print(battery)

print(psutil.cpu_freq())
#print("charge = %s%%, time left = %s" % (batt.percent, secs2hours(batt.secsleft)))


