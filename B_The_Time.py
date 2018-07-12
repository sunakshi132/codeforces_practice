def new_time(hour, minutes,add_min):
    total_minutes = (hour*60) + (minutes) + add_min
    new_hour = total_minutes/60
    if new_hour == 24:
        new_hour = 0
    elif new_hour > 24:
        new_hour = new_hour%24
    new_hour = str(new_hour)
    new_min = str(total_minutes%60)
    if len(new_hour) < 2:
        new_hour = '0'+ new_hour
    if len(new_min) < 2:
        new_min = '0'+ new_min
    return new_hour+ ":"+new_min
    
    
    
if __name__ == "__main__":
    time = raw_input()
    add_min = input()
    hour,minutes= map(int,time.split(':'))
    print new_time(hour,minutes,add_min)
    
    