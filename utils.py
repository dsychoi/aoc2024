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
