file=open("46-example.txt", "r")
content = file.read()
print(content)
content = file.readlines() # prints nothing because the pointer is at the end of the file becouse of the previous file.read()
print(content)
file.seek(0) # reset pointer in file
content = file.readlines()
print(content)
content = [i.rstrip("\n") for i in content]
print(content)
file.close()
