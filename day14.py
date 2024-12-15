from utils import fetch_data


def parse_data(data):
    results = []
    for line in data:
        position, velocity = line.split(' ')
        x, y = position.split('=')[1].split(',')
        dx, dy = velocity.split('=')[1].split(',')
        results.append(((int(x), int(y)), (int(dx), int(dy))))
    return results


def pass_one_second(robots):
    new_robots = []
    for robot in robots:
        position, velocity = robot
        x, y = position
        dx, dy = velocity
        new_x = (x + dx) % 101
        new_y = (y + dy) % 103
        new_robots.append(((new_x, new_y), velocity))
    return new_robots


def pass_x_seconds(x, robots):
    safety_scores = []
    for second in range(x):
        robots = pass_one_second(robots)
        safety_score = get_safe_robots(robots)
        safety_scores.append(safety_score)
    return robots, safety_scores


def get_safe_robots(robots):
    quadrant_1, quadrant_2, quadrant_3, quadrant_4 = [], [], [], []
    middle_x, middle_y = 101 // 2, 103 // 2
    for robot in robots:
        if robot[0][0] < middle_x and robot[0][1] < middle_y:
            quadrant_1.append(robot)
        elif robot[0][0] > middle_x and robot[0][1] < middle_y:
            quadrant_2.append(robot)
        elif robot[0][0] < middle_x and robot[0][1] > middle_y:
            quadrant_3.append(robot)
        elif robot[0][0] > middle_x and robot[0][1] > middle_y:
            quadrant_4.append(robot)

    return len(quadrant_1) * len(quadrant_2) * len(quadrant_3) * len(quadrant_4)


def print_grid(robots, second):
    grid = [['.'] * 101 for _ in range(103)]
    middle_x, middle_y = 101 // 2, 103 // 2

    for x in range(101):
        grid[middle_y][x] = '-'
    for y in range(103):
        grid[y][middle_x] = '|'
    grid[middle_y][middle_x] = '+'

    for i, robot in enumerate(robots):
        x, y = robot[0]
        grid[y][x] = '#'

    print(f"\nSecond {second}:")
    for row in grid:
        print(''.join(row))


def christmas_tree(robots):
    second = 0
    while True:
        row_counts = [0] * 103
        col_counts = [0] * 101
        for robot in robots:
            x, y = robot[0]
            row_counts[y] += 1
            col_counts[x] += 1

        max_row_count = max(row_counts)

        middle_start = 25
        middle_end = 75
        middle_col_counts = col_counts[middle_start:middle_end + 1]
        max_middle_col_count = max(middle_col_counts)

        if max_middle_col_count > 20 and max_row_count > 20:
            print(f"\nFound tree at second {second}")
            break

        robots = pass_one_second(robots)
        second += 1
    print_grid(robots, second)

    return robots, second

raw_data = fetch_data(14)
# raw_data = [
#     'p=0,4 v=3,-3',
#     'p=6,3 v=-1,-3',
#     'p=10,3 v=-1,2',
#     'p=2,0 v=2,-1',
#     'p=0,0 v=1,3',
#     'p=3,0 v=-2,-2',
#     'p=7,6 v=-1,-3',
#     'p=3,0 v=-1,-2',
#     'p=9,3 v=2,3',
#     'p=7,3 v=-1,2',
#     'p=2,4 v=2,-3',
#     'p=9,5 v=-3,-3',
# ]

parsed_data = parse_data(raw_data)
robots, safety_scores = pass_x_seconds(15000, parsed_data)
print(safety_scores.index(min(safety_scores)))
# safe_robots = get_safe_robots(robots)

