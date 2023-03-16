# 김진우
import sys
import time
sys.setrecursionlimit(10000)


def Hierarchical_Graph(cluster, graph):
    while 1:
        min_density = float("inf")
        for line in cluster:
            for line2 in graph[line]:
                density = float(len(set(graph[line]) & set(graph[line2]))+2) / float(len(set(graph[line]) | set(graph[line2])))
                if min_density > density:
                    min_density = density
                    min_vertex1 = line
                    min_vertex2 = line2
        if min_density <= 0.4:
            graph[min_vertex1].remove(min_vertex2)
            graph[min_vertex2].remove(min_vertex1)
            new_clusters1 = sorted(dfs(graph, min_vertex1))
            new_clusters2 = sorted(dfs(graph, min_vertex2))
            if new_clusters1 != new_clusters2:
                break
        else:
            return
    Hierarchical_Graph(new_clusters1, graph)
    Hierarchical_Graph(new_clusters2, graph)
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
gene = []
with open(sys.argv[1], 'r') as file:
    for line in file:
        data = []
        data = line.strip().split('\r\n')
        for time_point in data:
            gene.append(time_point.split('\t'))
# sort
information = []
for line in gene:
    line.sort()
    information.append(line)
information.sort()

graph = dict()
for line in information:
    line.sort()
    [n1, n2] = line
    try:
        graph[n1].add(n2)
    except KeyError:
        graph[n1] = {n2}
    try:
        graph[n2].add(n1)
    except KeyError:
        graph[n2] = {n1}

for line in graph:
    graph.update({line: sorted(graph[line])})

clusters = check_connection(graph)
for cluster in clusters:
    Hierarchical_Graph(cluster, graph)
clusters = check_connection(graph)
print(len(clusters))

# output file
f = open('../project/assignment6_2output.txt', 'w')

for n in range(len(clusters)):
    f.write("%d: " % len(clusters[n]))
    for j in range(len(clusters[n])):
        f.write("%s " % clusters[n][j])
    f.write("\n")
f.close()

end = time.time()
print(f"{end-start: .5f} sec")