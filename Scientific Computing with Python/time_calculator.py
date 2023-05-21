# calculadora de tiempo

def add_time(start, duration, day = ""):
    d1 = (int(duration.split(":")[0]))
    d2 = duration.split(":")[1]
    days = {"monday":1, "tuesday":2, "wednesday":3, "thursday":4, "friday":5, "saturday":6, "sunday":7}
    dias = 0
    horas_extra = 0
    new_time = start.replace(":", " ").split(" ")
    day = day.lower()
    if new_time[2] == "PM":
        new_time[0] = int(new_time[0]) + 12
    
    new_time[0] = (int(new_time[0])) + int(d1)
    new_time[1] = int(new_time[1]) + int(d2)
    
    if new_time[1] > 60:
        horas_extra = int(new_time[1]) // 60
        new_time[1] = int(new_time[1]) - (60 * horas_extra)
        new_time[0] = int(new_time[0]) + horas_extra
    
    if new_time[1] < 10:
        new_time[1] = "0" + str(new_time[1])
    
    if new_time[0] > 24:
        dias = int(new_time[0]) // 24
        new_time[0] = int(new_time[0]) - (24 * dias)

    if new_time[0] > 12:
        new_time[0] = int(new_time[0]) - 12
        new_time[2] = "PM"
    elif new_time[0] == 12 and new_time[2] == "AM" and int(new_time[1]) > 0:
        new_time[2] = "PM"
    else:
        new_time[2] = "AM"
    
    if new_time[0] == 0:
        new_time[0] = 12
    
    if day != "":
        x = int(days[day])
        print(dias)
        if x + dias > 7:
            y = (x + dias) % 7
            if y == 0:
                y = 1
            day = ", " + str(list(days.keys())[list(days.values()).index(y)]).capitalize()
        else:
            day = ", " + str(list(days.keys())[list(days.values()).index(x + dias)]).capitalize()
    
    
    if dias == 1:
        new_time = str(new_time[0]) + ":" + str(new_time[1]) + " " + str(new_time[2]) + day + " (next day)"
    elif dias > 1:
        new_time = str(new_time[0]) + ":" + str(new_time[1]) + " " + str(new_time[2]) + day + " (" + str(dias) + " days later)"
    else:
        new_time = str(new_time[0]) + ":" + str(new_time[1]) + " " + str(new_time[2]) + day
    

    
    return new_time

print(add_time("2:59 AM", "244:00", "friday"))

