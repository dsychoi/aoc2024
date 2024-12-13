from utils import fetch_data
from sympy import symbols, solve
from sympy.abc import x, y, z


def parse_data(data):
    lines = []
    current_line = []

    for line in data:
        if line.strip() == '':
            if current_line:
                lines.append(current_line)
                current_line = []
        else:
            current_line.append(line)
    if current_line:
        lines.append(current_line)

    result = []
    for line in lines:
        a = line[0]
        b = line[1]
        c = line[2]
        a_numbers = a.split(':')[1]
        b_numbers = b.split(':')[1]
        c_numbers = c.split(':')[1]
        x, y, z = a_numbers.split(','), b_numbers.split(','), c_numbers.split(',')
        x1, x2 = x[0].split('+')[1], x[1].split('+')[1]
        y1, y2 = y[0].split('+')[1], y[1].split('+')[1]
        z1, z2 = z[0].split('=')[1], z[1].split('=')[1]
        result.append([(int(x1), int(x2)), (int(y1), int(y2)), (int(z1) + 10000000000000, int(z2) + 10000000000000)])
    return result


def solve_machine(x0, y0, z0):

    x1, x2 = x0
    y1, y2 = y0
    z1, z2 = z0

    solution = solve([x1*x + y1*y - z1, x2*x + y2*y - z2], [x, y])
    for variable in solution:
        if '/' in str(solution[variable]):
            return None
    return int(solution[x]), int(solution[y])


def get_tokens(configurations):
    result = 0
    for configuration in configurations:
        solution = solve_machine(configuration[0], configuration[1], configuration[2])
        if solution:
            a, b = solution
            result += 3*a + b
    return result

raw_data = fetch_data(13)
parsed_data = parse_data(raw_data)
tokens = get_tokens(parsed_data)
print(tokens)

# 94x + 22y - 8400 = 0
# 34x + 67y - 5400 = 0

# print(solve([17*x + 84*y - 7870, 86*x + 37*y - 6450], [x, y]))
