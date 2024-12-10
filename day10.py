from utils import fetch_data


def parse_data(data):
    result = []
    for line in data:
        temp_line = []
        for i in line:
            if i != '.':
                temp_line.append(int(i))
            else:
                temp_line.append(i)
        result.append(temp_line)
    return result


def score_trailheads(map):
    result = 0

    for row_index, row in enumerate(map):
        for column_index, value in enumerate(row):
            if value == 0:
                visited = set()
                traverse_trail(map, (row_index, column_index), visited)
                for visited_row, visited_column in visited:
                    if map[visited_row][visited_column] == 9:
                        result += 1
    return result


def traverse_trail(map, start, visited):
    row, column = start
    is_invalid_row = row < 0 or row >= len(map)
    is_invalid_column = column < 0 or column >= len(map[0])

    if is_invalid_row or is_invalid_column:
        return
    if start in visited:
        return

    visited.add(start)
    current = map[row][column]

    if 0 <= row - 1 < len(map):
        if map[row - 1][column] == current + 1:
            traverse_trail(map, (row - 1, column), visited)
    if 0 <= row + 1 < len(map):
        if map[row + 1][column] == current + 1:
            traverse_trail(map, (row + 1, column), visited)
    if 0 <= column - 1 < len(map[0]):
        if map[row][column - 1] == current + 1:
            traverse_trail(map, (row, column - 1), visited)
    if 0 <= column + 1 < len(map[0]):
        if map[row][column + 1] == current + 1:
            traverse_trail(map, (row, column + 1), visited)


def find_unique_paths(grid):
    def is_valid_move(current_row, current_column, next_row, next_column, visited):
        if (next_row < 0 or next_row >= len(grid) or
                next_column < 0 or next_column >= len(grid[0])):
            return False

        if grid[next_row][next_column] != grid[current_row][current_column] + 1:
            return False

        return (next_row, next_column) not in visited

    def dfs(row, column, visited, path_length=1):
        if grid[row][column] == 9:
            return [(path_length, list(visited))]

        unique_paths = []

        moves = [
            (row - 1, column),
            (row + 1, column),
            (row, column - 1),
            (row, column + 1)
        ]

        for next_row, next_column in moves:
            if is_valid_move(row, column, next_row, next_column, visited):
                new_visited = visited.copy()
                new_visited.add((next_row, next_column))

                unique_paths.extend(
                    dfs(next_row, next_column, new_visited, path_length + 1)
                )

        return unique_paths

    all_unique_paths = []

    for row_index, row in enumerate(grid):
        for column_index, value in enumerate(row):
            if value == 0:
                visited = {(row_index, column_index)}
                all_unique_paths.extend(
                    dfs(row_index, column_index, visited)
                )

    return all_unique_paths

data = fetch_data(10)
# test_data = [
#     '89010123',
#     '78121874',
#     '87430965',
#     '96549874',
#     '45678903',
#     '32019012',
#     '01329801',
#     '10456732',
# ]

# test_data = [
#     '...0...',
#     '...1...',
#     '...2...',
#     '6543456',
#     '7.....7',
#     '8.....8',
#     '9.....9',
# ]

parsed_data = parse_data(data)
result = score_trailheads(parsed_data)
unique_paths = find_unique_paths(parsed_data)
print(result)
print(len(unique_paths))