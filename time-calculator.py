def add_time(start, duration, day_req = "N/A"):
    #Extracting data...
    start_h = int(start.split(":")[0])
    if "PM" in start: #Converting time to 24 hour format as that would be easier to deal with
        start_h += 12
    start_min = int(start.split(":")[1].split()[0])

    dur_h = int(duration.split(":")[0])
    dur_min = int(duration.split(":")[1])
    #...Done with extracting

    days_later = int((start_h + dur_h + int((start_min + dur_min) / 60)) / 24) #How many days have passed

    fut_h = (start_h + dur_h + int((start_min + dur_min) / 60)) % 24 #Calculating hour(24 hour format)
    PM = False  
    if fut_h >= 12: #Calculating PM or AM and converting time back to AM PM format       
        fut_h -= 12
        if fut_h == 0:#so htat 1am isnt shown as 0
            fut_h = 12
        PM = True

    if fut_h == 0:#so htat 1am isnt shown as 0
            fut_h = 12

    fut_min = str((start_min + dur_min) % 60).zfill(2) #Calculating minute

    if day_req == "N/A":  #If day isnt requested
        if days_later > 1:
            if PM:
                new_time = f"{fut_h}:{fut_min} PM ({days_later} days later)"
            else:
                new_time = f"{fut_h}:{fut_min} AM ({days_later} days later)"
        elif days_later == 1:
            if PM:
                new_time = f"{fut_h}:{fut_min} PM (next day)"
            else:
                new_time = f"{fut_h}:{fut_min} AM (next day)"
        else:
            if PM:
                new_time = f"{fut_h}:{fut_min} PM"
            else:
                new_time = f"{fut_h}:{fut_min} AM"
    else: #If day is requested
        days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") 
        day = days[(days.index(day_req.capitalize()) + 1 + days_later) % 7 - 1] #Calculating day
        if days_later > 1:
            if PM:
                new_time = f"{fut_h}:{fut_min} PM, {day} ({days_later} days later)"
            else:
                new_time = f"{fut_h}:{fut_min} AM, {day} ({days_later} days later)"
        elif days_later == 1:
            if PM:
                new_time = f"{fut_h}:{fut_min} PM, {day} (next day)"
            else:
                new_time = f"{fut_h}:{fut_min} AM, {day} (next day)"
        else:
            if PM:
                new_time = f"{fut_h}:{fut_min} PM, {day}"
            else:
                new_time = f"{fut_h}:{fut_min} AM, {day}"

    return new_time
