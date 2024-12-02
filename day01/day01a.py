first = []
second = []

with open('real.txt') as fin:
    for line in fin:
        a, b = line.split()
        first.append(int(a))
        second.append(int(b))

first.sort()
second.sort()
distance = sum([abs(first[i] - second[i]) for i in range(len(first))])
print(distance)



