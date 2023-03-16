import matplotlib.pyplot as plt

avg_temp = []
with open('Seoul.csv', 'r') as file:
    file.readline()
    for line in file:
        data = line.strip().split(',')

        if data[0] == '':
            break

        if data[2].split('-')[1] == '01':
            avg_temp.append(float(data[3]))

plt.plot(range(len(avg_temp)), avg_temp)

plt.xlabel('day')
plt.ylabel('average temperature')
plt.title('January')
plt.show()
