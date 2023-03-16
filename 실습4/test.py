import numpy as np

a = 0
arr = []
for i in range(10):
    line = []
    for j in range(10):
        line.append(a)
        a += 1
    arr.append(line)
B = np.array(arr)
print(B)