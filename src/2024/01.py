from aocd import data

first, second = [], []

for l in data.splitlines():
    a, b = map(int, l.split())
    first.append(a)
    second.append(b)

first.sort()
second.sort()

distance = 0
for i in range(len(first)):
    distance += abs(first[i] - second[i])

print(distance)
