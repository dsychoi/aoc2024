from utils import fetch_data

directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]


def count_xmas_in_directions(row, column, grid):
    count = 0
    for row_direction, column_direction in directions:
        if is_xmas_in_direction(row, column, grid, row_direction, column_direction):
            count += 1
    return count


def is_xmas_in_direction(row, column, grid, row_direction, column_direction):
    for index in range(len("XMAS")):
        new_row = row + index * row_direction
        new_column = column + index * column_direction
        if not (0 <= new_row < len(grid) and 0 <= new_column < len(grid[0])) or grid[new_row][new_column] != "XMAS"[index]:
            return False
    return True


def traverse_word_search(word_search):
    total = 0
    for row in range(len(word_search)):
        for column in range(len(word_search[row])):
            if word_search[row][column] == 'X':
                total += count_xmas_in_directions(row, column, word_search)
    return total


raw_data = fetch_data(4)
print(traverse_word_search(raw_data))


def traverse_fixed_word_search(grid):
    total = 0
    rows = len(grid)
    columns = len(grid[0])

    for row in range(1, rows - 1):
        for column in range(1, columns - 1):
            if check_x_mas_pattern(row, column, grid):
                total += 1
    return total


def is_mas(first_char, second_char, third_char):
    return (first_char + second_char + third_char == "MAS") or (first_char + second_char + third_char == "SAM")


def check_x_mas_pattern(row, column, grid):
    diagonal_1_1 = grid[row - 1][column - 1] + grid[row][column] + grid[row + 1][column + 1]
    diagonal_1_2 = grid[row + 1][column + 1] + grid[row][column] + grid[row - 1][column - 1]

    diagonal_2_1 = grid[row - 1][column + 1] + grid[row][column] + grid[row + 1][column - 1]
    diagonal_2_2 = grid[row + 1][column - 1] + grid[row][column] + grid[row - 1][column + 1]

    has_diagonal_1 = is_mas(diagonal_1_1[0], diagonal_1_1[1], diagonal_1_1[2]) or is_mas(
        diagonal_1_2[0], diagonal_1_2[1],
        diagonal_1_2[2])
    has_diagonal_2 = is_mas(diagonal_2_1[0], diagonal_2_1[1], diagonal_2_1[2]) or is_mas(
        diagonal_2_2[0], diagonal_2_2[1],
        diagonal_2_2[2])

    return has_diagonal_1 and has_diagonal_2


print(traverse_fixed_word_search(raw_data))
