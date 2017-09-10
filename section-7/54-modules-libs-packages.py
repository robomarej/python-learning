import os
print(os.listdir())
print(os.path.dirname(os.__file__))
print(os.listdir(os.path.dirname(os.__file__)))
