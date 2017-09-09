c = ["H", 2, "Hello"]
print(c)
print(type(c)) # <class 'list'>
print(c[:2]) # ['H', 2]
print(type(c[:2])) # <class 'list'> List spling is also of type list
c.append(3)
print(c) # ['H', 2, 'Hello', 3] - lists are not immutable
c.remove(3)
print(c) # removes FIRST OCCURENCE
print(c.remove(2)) # None - remove doesn't have return value
print(c) # ['H', 'Hello']
