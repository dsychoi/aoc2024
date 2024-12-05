from utils import fetch_data
from collections import defaultdict
import re


def parse_data(data):
    separator_index = data.index("")
    top, bottom = data[:separator_index], data[separator_index + 1:]

    rules = [tuple(map(int, line.split("|"))) for line in top]
    updates = [list(map(int, line.split(","))) for line in bottom]

    return rules, updates


def get_ordered_updates(rules, updates):
    total = 0

    for update in updates:
        ordered = True
        for left, right in rules:
            if left in update and right in update:
                left_index = update.index(left)
                right_index = update.index(right)

                if left_index > right_index:
                    ordered = False
                    break

        if ordered:
            mid_index = len(update) // 2
            total += update[mid_index]

    return total


raw_data = fetch_data(5)


def get_reordered_updates(rules, updates):
    total = 0

    for update in updates:
        ordered = True
        for left, right in rules:
            if left in update and right in update:
                left_index = update.index(left)
                right_index = update.index(right)

                if left_index > right_index:
                    ordered = False
                    break

        if not ordered:
            reordered = update.copy()

            changed = True
            while changed:
                changed = False
                for left, right in rules:
                    if left in reordered and right in reordered:
                        left_index = reordered.index(left)
                        right_index = reordered.index(right)

                        if left_index > right_index:
                            reordered[left_index], reordered[right_index] = reordered[right_index], reordered[
                                left_index]
                            changed = True

            mid_index = len(reordered) // 2
            total += reordered[mid_index]

    return total


rules, updates = parse_data(raw_data)

print(get_ordered_updates(rules, updates))
print(get_reordered_updates(rules, updates))
