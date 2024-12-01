from collections import Counter
from urllib import request
import os
from dotenv import load_dotenv

load_dotenv()

url = 'https://adventofcode.com/2024/day/1/input'
token = os.getenv('aoc_token')
req = request.Request(
    url, headers={'Cookie': f'session={token}'}
)

response = request.urlopen(req)
lines = response.read().decode('utf-8').strip().splitlines()  # Read and buffer once


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


print(get_distance(lines))
print(get_similarity(lines))
