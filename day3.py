from urllib import request
import os
from dotenv import load_dotenv

load_dotenv()

url = 'https://adventofcode.com/2024/day/3/input'
token = os.getenv('aoc_token')
req = request.Request(
    url, headers={'Cookie': f'session={token}'}
)

response = request.urlopen(req)
raw_lines = response.read().decode('utf-8').strip().splitlines()


def parse_data(data):
    parsed_data = []
    for line in data:
        split_line = line.split()
        parsed_data.append(split_line)
    return parsed_data


print(parse_data(raw_lines))
