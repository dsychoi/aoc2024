from utils import fetch_data


def count_guard_positions(map):
    visited = set()
    stack = []

    for row_number, row in enumerate(map):
        for column_number, value in enumerate(row):
            if value == '^':
                starting_position = (row_number, column_number)
                starting_direction = (-1, 0)
                stack.append((starting_position, starting_direction))

    while stack:
        position, direction = stack.pop()
        row, column = position

        if row < 0 or row >= len(map) or column < 0 or column >= len(map[0]):
            continue

        visited.add((row, column))

        next_row = row + direction[0]
        next_column = column + direction[1]

        if next_row < 0 or next_row >= len(map) or next_column < 0 or next_column >= len(map[0]):
            continue

        if map[next_row][next_column] == '#':
            if direction == (-1, 0):
                new_direction = (0, 1)
            elif direction == (0, 1):
                new_direction = (1, 0)
            elif direction == (1, 0):
                new_direction = (0, -1)
            else:
                new_direction = (-1, 0)

            next_position = (row + new_direction[0], column + new_direction[1])
            stack.append((next_position, new_direction))
        else:
            next_position = (next_row, next_column)
            stack.append((next_position, direction))

    return len(visited)

map_data = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..."
]

data = fetch_data(6)
print(count_guard_positions(data))