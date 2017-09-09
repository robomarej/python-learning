# def minutes_to_hours(minutes=70, seconds):
#     hours = minutes / 60 + seconds / 3600
#     # hours = minutes / 60.0 # in python 2
#     return hours

def minutes_to_hours(seconds, minutes=70):
    hours = minutes / 60 + seconds / 3600
    # hours = minutes / 60.0 # in python 2
    return hours

print(minutes_to_hours(60, 300))

# Traceback (most recent call last):
#   File "27-functions-advanced.py", line 12, in <module>
#     print(minutes_to_hours(60))
# TypeError: minutes_to_hours() missing 1 required positional argument: 'seconds'
# print(minutes_to_hours(60))

# File "27-functions-advanced.py", line 1
#     def minutes_to_hours(minutes=70, seconds):
#                         ^
# SyntaxError: non-default argument follows default argument
# print(minutes_to_hours(60))

print(minutes_to_hours(60, 300)) # overrides default value for minutes (300 instead of 70)
print(minutes_to_hours(60)) # uses default value for minutes (70)
