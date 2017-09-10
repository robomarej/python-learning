def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        raise Exception("Impossible temperature!")
    else:
        return celsius * 9/5 + 32

celsius_list = [10,-20,-289,100]
with open("51-exercise.txt", "w") as file:
    for celsius in celsius_list:
        try:
            file.write("\n"+str(celsius_to_fahrenheit(celsius)))
        except Exception as e:
            print(repr(e))
