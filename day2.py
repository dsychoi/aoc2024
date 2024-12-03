from utils import fetch_data


def parse_data(data):
    numbers = []
    for line in data:
        split_line = line.split()
        numbers.append([int(number) for number in split_line])
    return numbers


def is_safe(nums):
    is_increasing = all(1 <= nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1))
    is_decreasing = all(1 <= nums[i] - nums[i + 1] <= 3 for i in range(len(nums) - 1))

    return is_increasing or is_decreasing


def get_safe_reports(reports):
    return sum(1 for report in reports if is_safe(report))


def is_safe_tolerant(nums):
    is_increasing = all(1 <= nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1))
    is_decreasing = all(1 <= nums[i] - nums[i + 1] <= 3 for i in range(len(nums) - 1))

    if is_increasing or is_decreasing:
        return True

    for index, num in enumerate(nums):
        nums_copy = nums.copy()
        nums_copy.pop(index)
        is_increasing = all(1 <= nums_copy[i + 1] - nums_copy[i] <= 3 for i in range(len(nums_copy) - 1))
        is_decreasing = all(1 <= nums_copy[i] - nums_copy[i + 1] <= 3 for i in range(len(nums_copy) - 1))
        if is_increasing or is_decreasing:
            return True
    return False


def get_safe_tolerant_reports(reports):
    return sum(1 for report in reports if is_safe_tolerant(report))


raw_data = fetch_data(2)

print(get_safe_reports(parse_data(raw_data)))
print(get_safe_tolerant_reports(parse_data(raw_data)))

