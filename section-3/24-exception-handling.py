def divide(number,by):
    try:
        return number/by
    except ZeroDivisionError:
        print("Zerro division is meaningless") # print and continue

print(divide(10,0))
