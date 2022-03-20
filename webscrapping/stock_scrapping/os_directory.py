import os

print(os.getcwd())
# print(os.listdir())
path = "./"
print(os.path.abspath(path))

print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
