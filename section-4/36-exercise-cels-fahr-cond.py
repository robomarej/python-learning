def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        print("Impossible temperature!")
    else:
        return celsius * 9/5 + 32

celsius = float(input("Please input a celsius temperature: "))
print(celsius_to_fahrenheit(celsius))
