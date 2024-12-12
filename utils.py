import os
from urllib import request
from dotenv import load_dotenv

load_dotenv()


def fetch_data(day):
    token = os.getenv('aoc_token')
    if not token:
        raise ValueError("Advent of Code session token is not set in the environment variables.")

    url = f'https://adventofcode.com/2024/day/{day}/input'
    req = request.Request(url, headers={'Cookie': f'session={token}'})
    response = request.urlopen(req)
    return response.read().decode('utf-8').strip().splitlines()


def add_padding(matrix, padding_length, padding_char):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    padded_matrix = []

    for _ in range(padding_length):
        padded_matrix.append([padding_char] * (cols + 2 * padding_length))

    for row in matrix:
        padded_matrix.append(
            [padding_char] * padding_length + row + [padding_char] * padding_length
        )

    for _ in range(padding_length):
        padded_matrix.append([padding_char] * (cols + 2 * padding_length))

    return padded_matrix
