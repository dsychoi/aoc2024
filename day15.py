from utils import fetch_data


def parse_data(data):
    result = []
    split_index = data.index('')
    grid, directions = data[:split_index], data[split_index + 1:][0]
    for line in grid:
        result.append([x for x in line])
    return result, directions


def move_robot(grid, robot, direction):
    dy, dx = {
        '^': (-1, 0),
        'v': (1, 0),
        '>': (0, 1),
        '<': (0, -1),
    }[direction]

    dy, dx = (0, 1)

    boxes = []
    robot_x, robot_y = robot
    current_x = robot_x + dx
    current_y = robot_y + dy
    print(grid)
    print(current_x, current_y)
    print(grid[current_y][current_x])

    while grid[current_y][current_x] == 'O':
        boxes.append((current_x, current_y))
        current_x += dx
        current_y += dy

    print(grid[1])

    if grid[current_y][current_x] == '.':
        for box_x, box_y in boxes:
            grid[box_y][box_x] = '.'

        for box in boxes:
            grid[current_y][current_x] = 'O'
            current_x -= dx
            current_y -= dy

        grid[robot_y][robot_x] = '.'

        robot_x = robot_x + dx
        robot_y = robot_y + dy
        grid[robot_y][robot_x] = '@'

    return grid, (robot_x, robot_y)


def sum_gps(grid, directions):
    robot = (0, 0)
    for row_index in range(len(grid)):
        for column_index in range(len(grid[0])):
            if grid[row_index][column_index] == '@':
                robot = (row_index, column_index)
                break
    for direction in directions:
        grid, robot = move_robot(grid, robot, direction)
        print(robot)

    total = 0
    for row_index in range(len(grid)):
        for column_index in range(len(grid[0])):
            if grid[row_index][column_index] != 'O':
                continue
            total += 100 * row_index + column_index
    return total


# raw_data = fetch_data(15)
raw_data = [
    '########',
    '#..@OO.#',
    '##..O..#',
    '#...O..#',
    '#.#.O..#',
    '#...O..#',
    '#......#',
    '########',
    '',
    '<^^>>>vv<v>>v<<'
]
grid, directions = parse_data(raw_data)
sum_gps = sum_gps(grid, directions)
print(sum_gps)