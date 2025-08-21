from aocd import data

reports = [list(map(int, line.split())) for line in data.strip().split("\n")]


def is_safe_report(levels: list[int]) -> bool:
    if len(levels) < 2:
        return True

    differences = []
    for i in range(len(levels) - 1):
        diff = abs(levels[i + 1] - levels[i])
        if diff < 1 or diff > 3:
            return False
        differences.append(levels[i + 1] - levels[i])

    if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
        return True

    return False


def part_1() -> int:
    safe_reports = 0

    for report in reports:
        if is_safe_report(report):
            safe_reports += 1

    return safe_reports


print(part_1())
