def minutes_to_hours(minutes, seconds):
    hours = minutes / 60 + seconds / 3600
    # hours = minutes / 60.0 # in python 2
    return hours

print(minutes_to_hours(60, 300))

# Traceback (most recent call last):
#   File "27-functions-advanced.py", line 12, in <module>
#     print(minutes_to_hours(60))
# TypeError: minutes_to_hours() missing 1 required positional argument: 'seconds'
print(minutes_to_hours(60))
