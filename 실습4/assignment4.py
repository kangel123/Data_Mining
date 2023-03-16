# 김진우
import sys
import time


# initial clusters (초기값)
def clusters_create(genes):
    clusters_number = []  # cluster 번호
    i = int(0)
    while i < len(genes):
        line = []
        line.append(i)
        clusters_number.append(line)
        i += 1

    clusters_distance = []  # cluster 사이의 거리
    for i in clusters_number:
        line = []
        for j in clusters_number:
            distance = 0
            n = i[0]
            m = j[0]
            for k in range(len(genes[0])):
                distance += (float(genes[n][k]) - float(genes[m][k])) ** 2
            distance = round(distance ** 0.5, 3)
            line.append(distance)
        clusters_distance.append(line)
    return clusters_number, clusters_distance
# single_link
def single_link(cluster_number, cluster_distance):
    count = 0
    while 1:
        # 가장 작은 값 찾기
        min_distance = float("inf")  # 변경할 cluster 찾기위한 가장 작은 거리
        for i in range(len(clusters_distance)):
            for j in range(len(clusters_distance)):
                if i < j:
                    if min_distance > clusters_distance[i][j]:
                        min_distance = clusters_distance[i][j]
                        a = i
                        b = j
                        x = clusters_number[i]
                        y = clusters_number[j]
        if min_distance >= 5:  # 거리가 5이상 이면 종료
            break
        # clusters_distance 삽입
        new_clusters_distance = []
        for i in range(len(clusters_distance)):
            new_distance = min(clusters_distance[i][a], clusters_distance[i][b])
            clusters_distance[i].append(new_distance)
            new_clusters_distance.append(new_distance)
        new_clusters_distance.append(0)
        clusters_distance.append(new_clusters_distance)
        # clusters_distance 삭제
        del clusters_distance[a]
        del clusters_distance[b]
        for i in range(len(clusters_distance)):
            del clusters_distance[i][a]
            del clusters_distance[i][b]
        # clusters_number 통합
        z = []
        for j in y:
            z.append(j)
        for i in x:
            z.append(i)
        clusters_number.remove(x)
        clusters_number.remove(y)
        clusters_number.append(z)
        count += 1
    return clusters_number

# complex_link
def complex_link(cluster_number, cluster_distance):
    count = 0
    while 1:
        # 가장 작은 값 찾기
        min_distance = float("inf")  # 변경할 cluster 찾기위한 가장 작은 거리
        for i in range(len(clusters_distance)):
            for j in range(len(clusters_distance)):
                if i < j:
                    if min_distance > clusters_distance[i][j]:
                        min_distance = clusters_distance[i][j]
                        a = i
                        b = j
                        x = clusters_number[i]
                        y = clusters_number[j]
        if min_distance >= 5:  # 거리가 5이상이면 종료
            break
        # clusters_distance 삽입
        new_clusters_distance = []
        for i in range(len(clusters_distance)):
            new_distance = max(clusters_distance[i][a], clusters_distance[i][b])
            clusters_distance[i].append(new_distance)
            new_clusters_distance.append(new_distance)
        new_clusters_distance.append(0)
        clusters_distance.append(new_clusters_distance)
        # clusters_distance 삭제
        del clusters_distance[a]
        del clusters_distance[b]
        for i in range(len(clusters_distance)):
            del clusters_distance[i][a]
            del clusters_distance[i][b]
        # clusters_number 통합
        z = []
        for j in y:
            z.append(j)
        for i in x:
            z.append(i)
        clusters_number.remove(x)
        clusters_number.remove(y)
        clusters_number.append(z)
        count += 1
    return clusters_number


start = time.time()
# genes list
genes = []
with open(sys.argv[1], 'r') as file:
    for line in file:
        data = []
        data = line.strip().split('\r\n')
        for time_point in data:
            genes.append(time_point.split('\t'))

clusters_number, clusters_distance = clusters_create(genes)     # 초기값 함수
single_clusters_number = single_link(clusters_number, clusters_distance)    # single_link 함수
clusters_number, clusters_distance = clusters_create(genes)
complex_clusters_number = complex_link(clusters_number, clusters_distance)  # complex_link 함수

# output file
f = open('assignment4_output1.txt', 'w')
for n in range(len(single_clusters_number)):
    f.write("%d: " % len(single_clusters_number[n]))
    for j in range(len(single_clusters_number[n])):
        f.write("%d " % single_clusters_number[n][j])
    f.write("\n")
f.close()

f = open('assignment4_output2.txt', 'w')
for n in range(len(complex_clusters_number)):
    f.write("%d: " % len(complex_clusters_number[n]))
    for j in range(len(complex_clusters_number[n])):
        f.write("%d " % complex_clusters_number[n][j])
    f.write("\n")
f.close()

end = time.time()
print(f"{end-start: .5f} sec")
