from heapq import heappush, heappop
from collections import defaultdict
from utils import fetch_data


def get_shortest_path(graph, start, end):
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    visited = set()
    queue = [(0, start, 0)]

    while queue:
        score, position, direction = heappop(queue)

        if position == end:
            return score

        if (position, direction) in visited:
            continue
        visited.add((position, direction))

        next_position = (position[0] + directions[direction][0],
                    position[1] + directions[direction][1])

        if next_position in graph[position]:
            heappush(queue, (score + 1, next_position, direction))

        for rotation in [1, -1]:
            new_direction = (direction + rotation) % 4
            heappush(queue, (score + 1000, position, new_direction))

    return None


def parse_data(data):
    result = []
    for line in data:
        result.append([x for x in line])
    return result


def get_graph(grid):
    graph = defaultdict(set)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.' or grid[i][j] == 'E' or grid[i][j] == 'S':
                if grid[i + 1][j] == '.' or grid[i + 1][j] == 'E' or grid[i + 1][j] == 'S':
                    graph[(i, j)].add((i + 1, j))
                if grid[i - 1][j] == '.' or grid[i - 1][j] == 'E' or grid[i - 1][j] == 'S':
                    graph[(i, j)].add((i - 1, j))
                if grid[i][j + 1] == '.' or grid[i][j + 1] == 'E' or grid[i][j + 1] == 'S':
                    graph[(i, j)].add((i, j + 1))
                if grid[i][j - 1] == '.' or grid[i][j - 1] == 'E' or grid[i][j - 1] == 'S':
                    graph[(i, j)].add((i, j - 1))
    return graph


def get_start_and_end(grid):
    start = 0
    end = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
            if grid[i][j] == 'E':
                end = (i, j)
    return start, end


raw_data = fetch_data(16)
# raw_data = [
#     '###############',
#     '#.......#....E#',
#     '#.#.###.#.###.#',
#     '#.....#.#...#.#',
#     '#.###.#####.#.#',
#     '#.#.#.......#.#',
#     '#.#.#####.###.#',
#     '#...........#.#',
#     '###.#.#####.#.#',
#     '#...#.....#.#.#',
#     '#.#.#.###.#.#.#',
#     '#.....#...#.#.#',
#     '#.###.#.#.#.#.#',
#     '#S..#.....#...#',
#     '###############',
# ]

parsed_data = parse_data(raw_data)
start, end = get_start_and_end(parsed_data)
graph = get_graph(parsed_data)
shortest_path = get_shortest_path(graph, start, end)
print(shortest_path)