PERIOD_DURATION = 12
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def add_time(start, duration, weekday = ""):
    # split start into time and period
    start_parts = start.split() 
    time = start_parts[0]
    period = start_parts[1]

    # split time into hour and minute
    time_parts = time.split(":") 
    start_hour = int(time_parts[0])
    start_minute = int(time_parts[1])

    # split duration into hour and minute
    duration_parts = duration.split(":")
    duration_hour = int(duration_parts[0])
    duration_minute = int(duration_parts[1])

    # convert to 24-hour-clock
    if period == "PM":
        start_hour += PERIOD_DURATION

    # calculate new hour and time
    new_hour = add_duration(start_hour, duration_hour)
    new_minute = add_duration(start_minute, duration_minute)

    # convert surplus minutes to hour
    if new_minute >= MINUTES_PER_HOUR:
        new_hour += 1
        new_minute %= MINUTES_PER_HOUR

    # convert surplus hours to days
    days_later = 0
    if new_hour >= HOURS_PER_DAY:
        days_later = new_hour // HOURS_PER_DAY
        new_hour %= HOURS_PER_DAY

    # get new period for 12-hour-clock
    new_period = get_new_period(new_hour)
    
    # convert new hour to 12-hour-clock value
    new_hour = get_12_hour_clock_value(new_hour)
    
    new_weekday = get_new_weekday(weekday, days_later)
    
    return build_return_message(new_hour, new_minute, new_period, new_weekday, days_later)
    
def conform_weekday(weekday):
    return weekday.lower().capitalize()

def add_duration(start, duration):
    return int(start) + int(duration)

def get_days_later_message(days_later):
    if days_later == 0:
        return ""
    elif days_later == 1:
        return " (next day)"
    return " (" + str(days_later) + " days later)"

def get_new_period(new_hour):
    return "PM" if new_hour / PERIOD_DURATION >= 1 else "AM"

def get_12_hour_clock_value(new_hour):
    new_hour %= PERIOD_DURATION
    if new_hour == 0:
        return 12
    return new_hour

def get_new_weekday(weekday, days_later):
    if weekday != "":
        weekday = conform_weekday(weekday)
        index = WEEKDAYS.index(weekday)
        index += days_later
        index %= len(WEEKDAYS)
        return WEEKDAYS[index]
    return ""

def build_return_message(new_hour, new_minute, new_period, new_weekday, days_later):
    time = str(new_hour) + ":" + str(new_minute).zfill(2) + " " + new_period
    if new_weekday != "":
        new_weekday = ", " + new_weekday
    return time + new_weekday + get_days_later_message(days_later)