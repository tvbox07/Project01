
import numpy as np

list01 = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l']]
list02 = [[1,2,3],[4,5,6]]
list03 = [1,2,3]
list04 = [[1,2],[3,4]]
list05 = [1,2,3,4,5,6,7,8,9,10,9,8,7,6,4,3,2,1,1,1,1,1,1,1]
list06 = [2,1]

# list = int(list01) * int(list01)
print(list03*2)
p = np.multiply(list03,[3,4,5])
print(p)
p = np.convolve(list03,[1])
print(p)
p = np.convolve(list03,[2])
print(p)
p = np.convolve(list03,[1,0])
print(p)
p = np.convolve(list03,[1,1])
print(p)
p = np.convolve(list05,list03)
print(p)
p = np.convolve(list05,list06)
print(p)
p = np.convolve(list06,list05)
print(p)