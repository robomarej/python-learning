file = open("47-example.txt", "w")
file.write("Line 1")
file.close()

file = open("47-example.txt", "w") # this will remove Line 1 from the file
file.write("Line 2")
file.close()

file = open("47-example.txt", "w")
file.write("Line 1\nLine 2")
file.close()
