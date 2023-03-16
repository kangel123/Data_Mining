from random import randint
import matplotlib.pyplot as plt

# 그래프
# x_val = [1, 2, 3, 4]
# y_val =[1, 4, 8, 16]

# plt.plot(x_val, x_val, color='b', label='y=x')
# plt.plot(x_val, y_val, color='r', label='y=x**2')

# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('graph')
# plt.legend()
# plt.show()

# 히스토그램
# data = [1, 1, 2, 3, 3, 4, 4, 4, 5, 7, 7, 8, 10]
# plt.hist(data, bins=5)
# plt.show()

# Box plot
data1 = []
data2 = []
for i in range(30):
    data1.append(randint(1, 100))
    data2.append(randint(1,50))

plt.boxplot([data1, data2])
plt.show()
