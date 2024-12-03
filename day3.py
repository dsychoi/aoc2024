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
    pattern = r"mul\(\d+,\d+\)"
    total = 0

    matches = re.findall(pattern, memory)
    for match in matches:
        numbers = match.split('(')[1].split(')')[0]
        left_number, right_number = numbers.split(',')
        product = int(left_number) * int(right_number)
        total += product
    return total


def scan_conditional_corrupted_memory(memory):
    pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
    total = 0
    skip = False

    matches = re.findall(pattern, memory)
    for match in matches:
        if match.startswith("mul"):
            numbers = match.split('(')[1].split(')')[0]
            left_number, right_number = numbers.split(',')
            product = int(left_number) * int(right_number)
            if not skip:
                total += product
        elif match == "don't()":
            skip = True
        elif match == "do()":
            skip = False
    return total


print(scan_corrupted_memory(parsed_data))
print(scan_conditional_corrupted_memory(parsed_data))
