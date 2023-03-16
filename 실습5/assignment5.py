# 김진우
import sys
import time

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

# size-2 cliques
cliques = []
for line in information:
    cliques.append(line)

count = 1
while 1:
    new_cliques = []
    for line in cliques:
        new_cliques.append(line)
    for i in range(len(cliques)):
        line1 = cliques[i]
        for j in range(len(cliques)):
            if i < j:
                line2 = cliques[j]
                k = len(list(set(line1) & set(line2)))
                if k == count:
                    rem_line = list(set(line1) ^ set(line2))
                    rem_line.sort()
                    if rem_line in information:
                        add_line = list(set(line1) | set(line2))
                        add_line.sort()
                        if add_line not in new_cliques:
                            new_cliques.append(add_line)
                        if line1 in new_cliques:
                            new_cliques.remove(line1)
                        if line2 in new_cliques:
                            new_cliques.remove(line2)
                        if line2 in new_cliques:
                            new_cliques.remove(rem_line)

    if cliques == new_cliques:
        break
    cliques = new_cliques
    count += 1

# output file
f = open('../project/assignment5_2output.txt', 'w')

for n in range(len(cliques)):
    f.write("%d: " % len(cliques[n]))
    for j in range(len(cliques[n])):
        f.write("%s " % cliques[n][j])
    f.write("\n")

f.close()

end = time.time()
print(f"{end-start: .5f} sec")
