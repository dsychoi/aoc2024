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

    return len(visited), visited


def count_stuck_positions(map):
    distance, guard_path = count_guard_positions(map)

    map = [list(row) for row in map]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    total = 0
    guard_position = (0, 0)

    for row_number, row in enumerate(map):
        for column_number, value in enumerate(row):
            if value == '^':
                guard_position = (row_number, column_number)

    for row_number, row in enumerate(map):
        for column_number, value in enumerate(row):
            if value == '^' or value == '#':
                continue

            if (row_number, column_number) in guard_path:
                visited = set()
                map[row_number][column_number] = '#'

                direction_index = 0
                current_row, current_column = guard_position

                while current_row in range(len(map)) and current_column in range(len(map[0])) and (
                current_row, current_column, direction_index) not in visited:
                    visited.add((current_row, current_column, direction_index))

                    while True:
                        current_direction = directions[direction_index]
                        new_row, new_column = current_row + current_direction[0], current_column + current_direction[1]

                        if new_row in range(len(map)) and new_column in range(len(map[0])) and map[new_row][
                            new_column] == '#':
                            direction_index = (direction_index + 1) % 4
                        else:
                            current_row, current_column = new_row, new_column
                            break

                if (current_row, current_column, direction_index) in visited:
                    total += 1
                map[row_number][column_number] = "."

    return total


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
print(count_guard_positions(data)[0])
print(count_stuck_positions(data))
