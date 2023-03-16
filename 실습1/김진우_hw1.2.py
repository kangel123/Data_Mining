import matplotlib.pyplot as plt

jan_highest_temp = []
aug_highest_temp = []

with open('Seoul.csv', 'r') as file:
    file.readline()
    for line in file:
        data = line.strip().split(',')
        if data[0] == '':
            break

        if data[2].split('-')[1] == '01':
            if data[4] != '':
                jan_highest_temp.append(float(data[4]))
        if data[2].split('-')[1] == '08':
            if data[4] != '':
                aug_highest_temp.append(float(data[4]))

plt.hist(jan_highest_temp, bins=len(jan_highest_temp), color='blue')
plt.hist(aug_highest_temp, bins=len(aug_highest_temp), color='red')

plt.xlabel('temperature')
plt.ylabel('number of days')
plt.title('January and August')
plt.show()
