def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return"Impossible temperature!"
    else:
        return celsius * 9/5 + 32

celsius_list = [10,-20,-289,100]
for celsius in celsius_list:
    print(celsius_to_fahrenheit(celsius))
