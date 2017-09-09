c = "Hi there!"
print(c[3]) # "t"
print(c[len(c)-1]) # "!"
print(c[0:1]) # "H" - upper bound is not included !
print(c[0:2]) # "Hi"
print(c[:2]) # "Hi" - nothing works as 0
print(c[:]) # "Hi there!" - nothing works as 0
print(c[3:]) # "Hi there!" - nothing works as 0 (shorter than print(c[len(c)-1]) # "!")
print(c[-1:]) # ! negative indexes start from the end
print(c[-6:-1]) # negative indexes start from the end
