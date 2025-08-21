import re

from aocd import data

pattern = r"mul\((\d+),(\d+)\)"
matches = re.finditer(pattern, data)

total = 0

for match in matches:
    num1 = int(match.group(1))
    num2 = int(match.group(2))
    total += num1 * num2

print(total)
