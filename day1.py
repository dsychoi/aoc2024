from collections import Counter
from utils import fetch_data


def parse_data(data):
    left_list = []
    right_list = []
    for line in data:
        split_line = line.split()
        left_list.append(int(split_line[0]))
        right_list.append(int(split_line[1]))
    return left_list, right_list


def get_distance(data):
    left_list, right_list = parse_data(data)
    left_list.sort()
    right_list.sort()
    distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
    return distance


def get_similarity(data):
    left_list, right_list = parse_data(data)
    right_dict = Counter(right_list)

    similarity = sum(left * right_dict[left] for left in left_list)
    return similarity


raw_data = fetch_data(1)

print(get_distance(raw_data))
print(get_similarity(raw_data))
