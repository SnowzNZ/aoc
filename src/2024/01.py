from aocd import data

first, second = [], []

for l in data.splitlines():
    a, b = map(int, l.split())
    first.append(a)
    second.append(b)

first.sort()
second.sort()


def part_1(first: list, second: list) -> int:
    distance = 0
    for i in range(len(first)):
        distance += abs(first[i] - second[i])

    return distance


def part_2(first: list, second: list) -> int:
    similarity_score = 0

    for i in range(len(first)):
        similarity_score += abs(first[i] * second.count(first[i]))

    return similarity_score


print(part_1(first, second))
print(part_2(first, second))
