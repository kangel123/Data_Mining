# 김진우
import sys
import time

start = time.time()
# genes list
genes = []
with open(sys.argv[1], 'r') as file:
    for line in file:
        data = []
        data = line.strip().split('\r\n')
        for time_point in data:
            genes.append(time_point.split('\t'))

# select initial medoids
k = 10
k_medoids = []      # initial medoids[[sum_distance, gene ID]]
k_medoids_ID = []       # [gene IDs]
for i in range(len(genes)):
    line = []       # [sum_distance, gene ID]
    sum_distance = 0    # sum of distance for each object
    for t in range(len(genes)):
        distance = 0    # the distance between every pair of objects
        for j in range(len(genes[0])):
            distance += (float(genes[i][j])-float(genes[t][j]))**2
        distance = distance ** 0.5
        sum_distance += distance
    line.append(round(sum_distance, 3))
    line.append(i)
    k_medoids.append(line)
k_medoids.sort()    # sort
while len(k_medoids) > k:   # Select k objects
    k_medoids.pop()

for t in range(k):
    k_medoids_ID.append(k_medoids[t][1])
print("initial k_medoids_ID : ", k_medoids_ID)

# initial clusters
clusters = []
for i in range(k):
    line = []
    clusters.append(line)

for i in range(len(genes)):
    distance = float("inf")
    for a in range(len(k_medoids_ID)):
        t = k_medoids_ID[a]
        result = 0
        for j in range(len(genes[0])):
            result += (float(genes[i][j]) - float(genes[t][j])) ** 2
        result = result ** 0.5
        if distance > result:
            distance = result
            x = a
    clusters[x].append(i)
print("initial clusters :", clusters)

# update modoids iteratively
process_clusters = []
count = 0
while 1:
    k_medoids_ID = []
    # new_clusters
    new_clusters = []
    for i in range(k):
        line = []
        new_clusters.append(line)

    count += 1
    print("number of attempts : ", count)

    for t in range(k):
        result = float("Inf")
        for n in range(len(clusters[t])):
            a = clusters[t][n]
            sum_distance = 0
            for m in range(len(clusters[t])):
                b = clusters[t][m]
                distance = 0
                for j in range(k):
                    distance += (float(genes[a][j])-float(genes[b][j]))**2
                distance = distance ** 0.5
                sum_distance += distance
            if result > sum_distance:
                result = sum_distance
                x = a
        k_medoids_ID.append(x)
    print("k_medids_ID : ", k_medoids_ID)

    for i in range(len(genes)):
        distance = float("inf")
        for a in range(len(k_medoids_ID)):
            t = k_medoids_ID[a]
            result = 0
            for j in range(len(genes[0])):
                result += (float(genes[i][j]) - float(genes[t][j])) ** 2
            result = result ** 0.5
            if distance > result:
                distance = result
                x = a
        new_clusters[x].append(i)
    print("new_clusters : ", new_clusters)
    if new_clusters in process_clusters:    # the clusters do not change.
        break
    else:                           # the clusters change.
        clusters = new_clusters
        process_clusters.append(new_clusters)

# output file
f = open('assignment3_output.txt', 'w')

for n in range(k):
    f.write("%d: " % len(clusters[n]))
    for j in range(len(clusters[n])):
        f.write("%d " % clusters[n][j])
    f.write("\n")
f.close()

end = time.time()
print(f"{end-start: .5f} sec")
