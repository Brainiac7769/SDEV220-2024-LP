#Lynn Prout
#Module 3.1 - 3.6
seconds_in_minutes: int = 60
mins_in_hour: int = 60
#3.2
seconds_per_hour: int = (mins_in_hour * seconds_in_minutes)
print("Seconds in an hour", mins_in_hour * seconds_in_minutes)
hours_per_day: int = 24
#3.3
print("Seconds per day", hours_per_day * seconds_per_hour)
#3.4
seconds_per_day: int = (hours_per_day * seconds_per_hour)
#3.5
print("Seconds per day divided by seconds per hour", seconds_per_day / seconds_per_hour)
#3.6
print("Seconds per day divided by seconds per hour", seconds_per_day // seconds_per_hour) 