with open("50-example.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.write("Line 6") # write method is using "\n" by default
