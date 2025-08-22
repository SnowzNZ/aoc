import re

from aocd import data


def part_1() -> int:
    mul_pattern = r"mul\((\d+),(\d+)\)"
    mul_matches = re.finditer(mul_pattern, data)

    total = 0

    for match in mul_matches:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        total += num1 * num2

    return total


def part_2() -> int:
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    instructions = []

    for match in re.finditer(do_pattern, data):
        instructions.append((match.start(), "do"))

    for match in re.finditer(dont_pattern, data):
        instructions.append((match.start(), "dont"))

    instructions.sort(key=lambda x: x[0])

    mul_pattern = r"mul\((\d+),(\d+)\)"
    mul_matches = list(re.finditer(mul_pattern, data))

    total = 0

    for mul_match in mul_matches:
        mul_pos = mul_match.start()

        enabled = True

        for control_pos, control_type in reversed(instructions):
            if control_pos < mul_pos:
                enabled = control_type == "do"
                break

        if enabled:
            num1 = int(mul_match.group(1))
            num2 = int(mul_match.group(2))
            total += num1 * num2

    return total


print(part_1())
print(part_2())
