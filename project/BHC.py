# 김진우
import sys
import time
sys.setrecursionlimit(10000)


def BHC(cluster, graph):
    max=[]
    while 1:
        k = -1
        for line1 in cluster:
            if len(graph[line1]) > k:
                max1 = -1
                for line2 in graph[line1]:
                    if max1 < len(graph[line2]):
                        if [line1, line2] not in max:
                            max_vertex1 = line1
                            max_vertex2 = line2
                            k = len(graph[line1])
                            max1 = len(graph[line2])

        if k > 5:
            density = float(len(set(graph[max_vertex1]) & set(graph[max_vertex2])) + 2) / float(len(set(graph[max_vertex1]) | set(graph[max_vertex2])))

            if density <= 0.4:
                graph[max_vertex1].remove(max_vertex2)
                graph[max_vertex2].remove(max_vertex1)
                new_clusters1 = sorted(dfs(graph, max_vertex1))
                new_clusters2 = sorted(dfs(graph, max_vertex2))
                if new_clusters1 != new_clusters2:
                    break
            else:
                max.append([max_vertex1, max_vertex2])
                max.append([max_vertex2, max_vertex1])
        else:
            return
    BHC(new_clusters1, graph)
    BHC(new_clusters2, graph)
    return

def check_connection(graph):
    cluster = []
    except_line = []
    for line in graph:
        if line not in except_line:
            connect = sorted(dfs(graph, line))
            for i in connect:
                except_line.append(i)
            if connect not in cluster:
                cluster.append(connect)
    return cluster


def dfs(graph, start):
    need_visited, visited = list(), list()
    need_visited.append(start)
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited


start = time.time()

# graph information
graph = dict()
with open(sys.argv[1], 'r') as file:
    for line in file:
        [n1, n2] = line.strip().split('\t')
        try:
            graph[n1].add(n2)
        except KeyError:
            graph[n1] = {n2}
        try:
            graph[n2].add(n1)
        except KeyError:
            graph[n2] = {n1}

clusters = check_connection(graph)



for cluster in clusters:
    BHC(cluster, graph)
clusters = check_connection(graph)

# output file
f = open('BHC_output_4.txt', 'w')

for n in range(len(clusters)):
    f.write("%d: " % len(clusters[n]))
    for j in range(len(clusters[n])):
        f.write("%s " % clusters[n][j])
    f.write("\n")
f.close()

end = time.time()
print(f"{end-start: .5f} sec")