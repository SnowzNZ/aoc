from aocd import data

word_search = [
    [char for char in "".join(line.split())] for line in data.strip().split("\n")
]


def count_occurrences(word_search, word) -> int:
    n = len(word_search)
    m = len(word_search[0])
    count = 0

    directions = [
        (-1, -1),  # top-left
        (-1, 0),  # top
        (-1, 1),  # top-right
        (0, -1),  # left
        (0, 1),  # right
        (1, -1),  # bottom-left
        (1, 0),  # bottom
        (1, 1),  # bottom-right
    ]

    for i in range(n):
        for j in range(m):
            if word[0] == word_search[i][j]:
                for dr, dc in directions:
                    if find_in_direction(word_search, word, i, j, dr, dc):
                        count += 1

    return count


def find_in_direction(word_search, word, row, col, dr, dc, i=0) -> bool:
    if i == len(word):
        return True

    if (
        row >= len(word_search)
        or row < 0
        or col >= len(word_search[0])
        or col < 0
        or word[i] != word_search[row][col]
    ):
        return False

    original_char = word_search[row][col]
    word_search[row][col] = "*"

    result = find_in_direction(word_search, word, row + dr, col + dc, dr, dc, i + 1)

    word_search[row][col] = original_char

    return result


print(count_occurrences(word_search, "MAS"))
