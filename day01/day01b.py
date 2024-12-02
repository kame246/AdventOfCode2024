first = []
second = []

with open('real.txt') as fin:
    for line in fin:
        a, b = line.split()
        first.append(int(a))
        second.append(int(b))


similarity = sum([first[i] * second.count(first[i]) for i in range(len(first))])
print(similarity)



