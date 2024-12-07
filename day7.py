from utils import fetch_data
from itertools import product


def get_calibration_result(data):
    total = 0

    for line in data:
        left, right = line.split(':')
        left = int(left)
        right = right.strip().split()
        right = [int(num) for num in right]
        for operator_combinations in product(['+', '*', '||'], repeat=len(right) - 1):
            if evaluate(left, right, operator_combinations):
                total += left
                break
    return total


def evaluate(result, numbers, operators):
    total = numbers[0]
    for index, operator in enumerate(operators):
        if operator == '*':
            total *= numbers[index + 1]
        elif operator == '+':
            total += numbers[index + 1]
        elif operator == '||':
            total = int(str(total) + str(numbers[index + 1]))
    if result == total:
        return True
    return False


result = get_calibration_result(fetch_data(7))
print(result)

