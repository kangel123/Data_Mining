# 김진우
import sys

with open(sys.argv[1], 'r') as file:
    # genes list
    genes = []
    for total in file:
        line = []
        line = total.strip().split('\r\n')
        for time_point in line:
            genes.append(time_point.split('\t'))
    print("genes list : ", genes)
    print()

# k-means initialization
k = 10
count = 1           # number of attempts
kmeans_ID = []
kmeans_average = []
number = float(len(genes)/k)
for n in range(k):      # k-means_ID
    line = []
    for i in range(int(number*n), int(number*(n+1))):
        line.append(i)
    kmeans_ID.append(line)
print("number of attempts : ", count)
print("k-means ID list : ", kmeans_ID)

# k-means algorithm
while 1:
    # new_k-means_ID
    new_kmeans_ID = []
    for n in range(k):
        line = []
        new_kmeans_ID.append(line)

    # k-means_average
    kmeans_average = []
    number = 0
    for n in range(k):
        line = []
        m = len(kmeans_ID[n])
        for j in range(len(genes[0])):
            result = 0
            for i in range(number, number + m):
                t = kmeans_ID[n][i-number]
                result += float(genes[t][j])
            line.append(round(result/m, 3))
        kmeans_average.append(line)
        number += m
    print("k-means average list : ", kmeans_average)
    print()

    # euclidean_distance, new_kmeans_ID
    for i in range(len(genes)):
        euclidean_distance = float("inf")
        for n in range(k):
            sum = 0
            for j in range(len(genes[0])):
                sum += (float(kmeans_average[n][j]) - float(genes[i][j])) ** 2
            result = sum ** 0.5
            if euclidean_distance > result:
                euclidean_distance = result
                x = n
        new_kmeans_ID[x].append(i)

    if kmeans_ID == new_kmeans_ID:
        break
    else:
        kmeans_ID = new_kmeans_ID
        count += 1
        print("number of attempts : ", count)
        print("k-means ID list : ", kmeans_ID)

# output file
f = open('assignment2_output.txt', 'w')

for n in range(k):
    f.write("%d: " % len(kmeans_ID[n]))
    for j in range(len(kmeans_ID[n])):
        f.write("%d " % kmeans_ID[n][j])
    f.write("\n")
f.close()
