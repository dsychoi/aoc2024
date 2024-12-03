from utils import fetch_data
import re


def parse_data(data):
    result = []
    for line in data:
        result.append(line)
    joined_result = "".join(result)
    return joined_result


raw_data = fetch_data(3)
parsed_data = parse_data(raw_data)


def scan_corrupted_memory(memory):
    pattern = r"mul\((\d+),(\d+)\)"
    total = 0

    for match in re.finditer(pattern, memory):
        left_number, right_number = int(match.group(1)), int(match.group(2))
        product = int(left_number) * int(right_number)
        total += product
    return total


def scan_conditional_corrupted_memory(memory):
    pattern = r"mul\((\d+),(\d+)\)|don't\(\)|do\(\)"
    total = 0
    skip = False

    for match in re.finditer(pattern, memory):
        if match.group(0).startswith("mul"):
            left_number, right_number = int(match.group(1)), int(match.group(2))
            if not skip:
                total += left_number * right_number
        elif match.group(0) == "don't()":
            skip = True
        elif match.group(0) == "do()":
            skip = False

    return total


print(scan_corrupted_memory(parsed_data))
print(scan_conditional_corrupted_memory(parsed_data))
