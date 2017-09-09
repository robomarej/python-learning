def minutes_to_hours(minutes, seconds):
    hours = minutes / 60 + seconds / 3600
    # hours = minutes / 60.0 # in python 2
    return hours

print(minutes_to_hours(60, 300))
