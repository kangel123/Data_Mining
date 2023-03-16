import matplotlib.pyplot as plt

month_average_temp = [[], [], [], [], [], [], [], []]

with open('Seoul.csv', 'r') as file:
    file.readline()
    for line in file:
        data = line.strip().split(',')
        if data[0] == '':
            break

        month_average_temp[int(data[2].split('-')[1])-1].append(float(data[3]))

plt.xlabel('month')
plt.ylabel('temperature')
plt.title('January to August')
plt.boxplot(month_average_temp)
plt.show()
