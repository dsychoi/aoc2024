from collections import defaultdict
from itertools import combinations
from utils import fetch_data


def parse_map(data):
    parsed_map = defaultdict(list)
    for row_index, row in enumerate(data):
        for column_index, value in enumerate(row):
            if value != '.':
                parsed_map[value].append((row_index, column_index))
    return parsed_map


def is_within_grid_bounds(row, column, grid_size):
    return 0 <= row < grid_size and 0 <= column < grid_size


def get_antinodes(first_antenna, second_antenna, grid_size):
    first_row, first_column = first_antenna
    second_row, second_column = second_antenna

    opposite_row_first = first_row - (second_row - first_row)
    opposite_column_first = first_column - (second_column - first_column)
    opposite_row_second = second_row + (second_row - first_row)
    opposite_column_second = second_column + (second_column - first_column)

    antinodes_list = []

    if is_within_grid_bounds(opposite_row_first, opposite_column_first, grid_size):
        antinodes_list.append((opposite_row_first, opposite_column_first))
    if is_within_grid_bounds(opposite_row_second, opposite_column_second, grid_size):
        antinodes_list.append((opposite_row_second, opposite_column_second))

    return antinodes_list


def count_antinodes(data):
    grid_size = len(data)
    antinodes = set()

    antenna_locations = parse_map(data)

    for frequency in antenna_locations:
        locations = antenna_locations[frequency]
        for first_antenna, second_antenna in combinations(locations, r=2):
            for antinode in get_antinodes(first_antenna, second_antenna, grid_size):
                antinodes.add(antinode)

    return len(antinodes)


def get_updated_antinodes(first_antenna, second_antenna, grid_size):
    first_row, first_column = first_antenna
    second_row, second_column = second_antenna

    row_diff, col_diff = second_row - first_row, second_column - first_column

    antinodes_list = []

    i = 0
    while is_within_grid_bounds(
        first_row - row_diff * i, first_column - col_diff * i, grid_size
    ):
        antinodes_list.append((first_row - row_diff * i, first_column - col_diff * i))
        i += 1

    i = 0
    while is_within_grid_bounds(
        second_row + row_diff * i, second_column + col_diff * i, grid_size
    ):
        antinodes_list.append((second_row + row_diff * i, second_column + col_diff * i))
        i += 1

    return antinodes_list


def count_updated_antinodes(data):
    grid_size = len(data)
    antinodes = set()

    antenna_locations = parse_map(data)

    for frequency in antenna_locations:
        locations = antenna_locations[frequency]
        for first_antenna, second_antenna in combinations(locations, r=2):
            for antinode in get_updated_antinodes(first_antenna, second_antenna, grid_size):
                antinodes.add(antinode)

    return len(antinodes)


print(count_updated_antinodes(fetch_data(8)))
