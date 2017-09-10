file = open("47-example.txt", "w")
file.write("Line 1")
file.close()

file = open("47-example.txt", "w") # this will remove Line 1 from the file
file.write("Line 2")
file.close()

file = open("47-example.txt", "w")
file.write("Line 1\nLine 2")
file.close()


lines = ["Line 1", "Line 2", "Line 3"]
file = open("47-example.txt", "w")
for line in lines:
    file.write(line+"\n")
file.close()
