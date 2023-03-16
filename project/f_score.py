import sys

def make_cluster(infor):
    gene = []
    with open(infor, 'r') as file:
        for line in file:
            data = []
            t = line.strip().split(' ')
            for i in range(len(t)):
                if i > 0:
                    data.append(t[i])
            gene.append(data)
    return gene

def find_f_score(gene):
    f_average = 0
    for line1 in gene:
        f_score = 0
        for line2 in truth:
            Precision = float(len(list(set(line1) & set(line2)))) / float(len(line1))
            Recall = float(len(list(set(line1) & set(line2)))) / float(len(line2))
            if Precision != 0 or Recall != 0:
                F = 2 * Precision * Recall / (Precision + Recall)
                if f_score < F:
                    f_score = F
        f_average += f_score
    f_average /= len(gene)
    return f_average


# ground_truth
truth = []
with open(sys.argv[1], 'r') as file:
    for line in file:
        data = []
        data = line.strip().split('\r\n')
        for time_point in data:
            truth.append(time_point.split(' '))

f_score = {}
for k in range(len(sys.argv)-2):
    f_score[sys.argv[k+2]] = find_f_score(make_cluster(sys.argv[k+2]))

# output file
f = open('f_score_output.txt', 'w')

for n in f_score:
    f.write("%s: %f" % (n, f_score[n]))
    f.write("\n")
f.close()
