from utils import fetch_data, add_padding
from collections import defaultdict


def parse_data(raw_data):
    result = []
    for line in raw_data:
        result.append([x for x in line])
    padded_result = add_padding(result, 2, '.')
    return padded_result


def get_total_price(plots):
    total_price = 0
    visited = set()
    for row_index, row in enumerate(plots):
        for column_index, value in enumerate(row):
            if (row_index, column_index) not in visited and value != '.':
                total_price += calculate_pricing((row_index, column_index), plots, visited)
    return total_price


def get_total_new_price(plots):
    total_price = 0
    visited = set()
    for row_index, row in enumerate(plots):
        for column_index, value in enumerate(row):
            if (row_index, column_index) not in visited and value != '.':
                total_price += calculate_new_pricing((row_index, column_index), plots, visited)
    return total_price


def calculate_pricing(starting_position, plots, visited):
    queue = [starting_position]
    starting_row, starting_column = starting_position
    plant = plots[starting_row][starting_column]

    perimeter = 0
    area = 0

    while len(queue) > 0:
        row, column = queue.pop(0)
        if (row, column) in visited:
            continue
        area += 1
        visited.add((row, column))
        neighbors = 0
        if plots[row - 1][column] == plant:
            neighbors += 1
            if (row - 1, column) not in visited:
                queue.append((row - 1, column))
        if plots[row + 1][column] == plant:
            neighbors += 1
            if (row + 1, column) not in visited:
                queue.append((row + 1, column))
        if plots[row][column - 1] == plant:
            neighbors += 1
            if (row, column - 1) not in visited:
                queue.append((row, column - 1))
        if plots[row][column + 1] == plant:
            neighbors += 1
            if (row, column + 1) not in visited:
                queue.append((row, column + 1))
        perimeter += 4 - neighbors
    return perimeter * area


def calculate_new_pricing(starting_position, plots, visited):
    queue = [starting_position]
    starting_row, starting_column = starting_position
    plant = plots[starting_row][starting_column]

    perimeter = 0
    area = 0
    # an edge is a position and a direction
    # go through the edges and compare rows/columns/directions
    edges = []

    while len(queue) > 0:
        row, column = queue.pop(0)
        if (row, column) in visited:
            continue
        area += 1
        visited.add((row, column))
        neighbors = 0
        if plots[row - 1][column] == plant:
            neighbors += 1
            if (row - 1, column) not in visited:
                queue.append((row - 1, column))
        else:
            edges.append(((row, column), (-1, 0)))
        if plots[row + 1][column] == plant:
            neighbors += 1
            if (row + 1, column) not in visited:
                queue.append((row + 1, column))
        else:
            edges.append(((row, column), (1, 0)))
        if plots[row][column - 1] == plant:
            neighbors += 1
            if (row, column - 1) not in visited:
                queue.append((row, column - 1))
        else:
            edges.append(((row, column), (0, -1)))
        if plots[row][column + 1] == plant:
            neighbors += 1
            if (row, column + 1) not in visited:
                queue.append((row, column + 1))
        else:
            edges.append(((row, column), (0, 1)))
        perimeter += 4 - neighbors

    left = []
    right = []
    up = []
    down = []
    for edge in edges:
        if edge[1] == (-1, 0):
            up.append(edge)
        if edge[1] == (1, 0):
            down.append(edge)
        if edge[1] == (0, -1):
            left.append(edge)
        if edge[1] == (0, 1):
            right.append(edge)

    up_locations = [x[0] for x in up]
    down_locations = [x[0] for x in down]
    left_locations = [x[0] for x in left]
    right_locations = [x[0] for x in right]

    up_dict = defaultdict(list)
    down_dict = defaultdict(list)
    left_dict = defaultdict(list)
    right_dict = defaultdict(list)

    print(up_locations)

    for location in up_locations:
        up_dict[location[1]].append(location[0])
    for location in down_locations:
        down_dict[location[1]].append(location[0])
    for location in left_locations:
        left_dict[location[1]].append(location[0])
    for location in right_locations:
        right_dict[location[1]].append(location[0])

    perimeter = count_uniques(up_dict) + count_uniques(down_dict) + count_uniques(left_dict) + count_uniques(right_dict)
    print(up_dict)
    print(right_dict)
    print(perimeter, area)
    return perimeter * area


def count_uniques(dict):
    def count_uniques_in_list(dict_list):
        sorted_list = sorted(dict_list)

        if len(sorted_list) < 2:
            return 1

        unique_groups = []
        current_group = [sorted_list[0]]

        for i in range(1, len(sorted_list)):
            if sorted_list[i] - current_group[0] >= 2:
                unique_groups.append(current_group)
                current_group = [sorted_list[i]]
            else:
                current_group.append(sorted_list[i])

        unique_groups.append(current_group)

        return len(unique_groups)

    return sum(count_uniques_in_list(dict_list) for dict_list in dict.values())


# raw_data = fetch_data(12)
# raw_data = [
#     'RRRRIICCFF',
#     'RRRRIICCCF',
#     'VVRRRCCFFF',
#     'VVRCCCJFFF',
#     'VVVVCJJCFE',
#     'VVIVCCJJEE',
#     'VVIIICJJEE',
#     'MIIIIIJJEE',
#     'MIIISIJEEE',
#     'MMMISSJEEE',
# ]
raw_data = [
    'EEEEE',
    'EXXXX',
    'EEEEE',
    'EXXXX',
    'EEEEE',
]





parsed_data = parse_data(raw_data)
pricing = get_total_new_price(parsed_data)
print(pricing)

