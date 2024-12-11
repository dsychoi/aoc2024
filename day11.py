from utils import fetch_data
from collections import Counter


def blink(stones, blinks):
    stone_counts = Counter(stones)

    while blinks > 0:
        new_counts = Counter()
        for stone, count in stone_counts.items():
            transformed = get_new_stone(stone)
            if isinstance(transformed, tuple):
                for part in transformed:
                    new_counts[part] += count
            else:
                new_counts[transformed] += count
        stone_counts = new_counts
        blinks -= 1

    return sum(stone_counts.values())


def get_new_stone(stone):
    if stone == 0:
        return 1
    if len(str(stone)) % 2 == 0:
        number = str(stone)
        midpoint = len(number) // 2
        left, right = int(number[:midpoint]), int(number[midpoint:])
        return left, right
    return stone * 2024


data = [int(x) for x in fetch_data(11)[0].split()]
# print(len(blink(data, 25)))
print(blink(data, 75))
