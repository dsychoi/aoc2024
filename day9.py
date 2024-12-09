from utils import fetch_data


def get_puzzle_id(puzzle):
    files = [int(puzzle[i]) for i in range(len(puzzle)) if i % 2 == 0]
    free_space = [int(puzzle[i]) for i in range(len(puzzle)) if i % 2 != 0]
    result = []
    for i in range(len(files)):
        for number in range(files[i]):
            result.append(i)
        if len(free_space) > i:
            for space in range(free_space[i]):
                result.append('.')
    return result


def get_puzzle_id_updated(puzzle):
    files = [int(puzzle[i]) for i in range(len(puzzle)) if i % 2 == 0]
    free_space = [int(puzzle[i]) for i in range(len(puzzle)) if i % 2 != 0]
    result = []
    for i in range(len(files)):
        result.append((files[i], i))
        if len(free_space) > i:
            result.append((free_space[i], '.'))
    return result


def compact_puzzle(puzzle_id):
    while True:
        moved = False
        for i in range(len(puzzle_id)):
            if puzzle_id[i] == '.':
                for j in range(len(puzzle_id) - 1, i, -1):
                    if puzzle_id[j] != '.':
                        puzzle_id[i], puzzle_id[j] = puzzle_id[j], puzzle_id[i]
                        moved = True
                        break

        if not moved:
            break

    while puzzle_id and puzzle_id[-1] == '.':
        puzzle_id.pop()

    return puzzle_id


def consolidate_free_spaces(puzzle_id):
    consolidated = []
    temp_sum = 0

    for count, value in puzzle_id:
        if value == '.':
            temp_sum += count
        else:
            if temp_sum > 0:
                consolidated.append((temp_sum, '.'))
                temp_sum = 0
            consolidated.append((count, value))

    if temp_sum > 0:
        consolidated.append((temp_sum, '.'))

    return consolidated

def compact_puzzle_updated(puzzle_id):
    while True:
        moved = False
        j = len(puzzle_id) - 1

        while j >= 0:
            if puzzle_id[j][1] != '.' and puzzle_id[j][0] > 0:
                for i in range(j):
                    if puzzle_id[i][1] == '.':
                        if puzzle_id[i][0] == puzzle_id[j][0] * len(str(puzzle_id[j][1])):
                            puzzle_id[i], puzzle_id[j] = puzzle_id[j], (len(str(puzzle_id[j][1]) * puzzle_id[j][0]), '.')
                            moved = True
                            break
                        elif puzzle_id[i][0] > puzzle_id[j][0] * len(str(puzzle_id[j][1])):
                            puzzle_id[i] = (puzzle_id[i][0] - (len(str(puzzle_id[j][1]) * puzzle_id[j][0])), puzzle_id[i][1])
                            temp_j = puzzle_id[j]
                            puzzle_id.insert(i, puzzle_id[j])
                            puzzle_id[j + 1] = ((len(str(temp_j[1])) * temp_j[0]), '.')

                            moved = True
                            break

            j -= 1

        if not moved:
            break

    return [tuple for tuple in puzzle_id if tuple[0] != 0]


def get_checksum(puzzle_id_list):
    result = 0
    for i in range(len(puzzle_id_list)):
        result += i * int(puzzle_id_list[i])
    return result


def get_checksum(puzzle_id_list):
    result = 0
    unpacked_list = unpack_list(puzzle_id_list)
    for index, num in enumerate(unpacked_list):
        if num != '.':
            result += index * num

    return result


def unpack_list(list):
    unpacked_list = []
    for tuple in list:
        for i in range(tuple[0]):
            unpacked_list.append(tuple[1])
    return unpacked_list


# puzzle = '351632342'
puzzle = fetch_data(9)[0]
# puzzle_id = get_puzzle_id(puzzle)
# print(puzzle_id)
# finished_puzzle = compact_puzzle(puzzle_id)
# print(finished_puzzle)
# checksum = get_checksum(finished_puzzle)

puzzle_id_updated = get_puzzle_id_updated(puzzle)
print(len(''.join([str(i) for i in unpack_list(puzzle_id_updated)])))
finished_puzzle_updated = compact_puzzle_updated(puzzle_id_updated)
print(len(''.join([str(i) for i in unpack_list(finished_puzzle_updated)])))
checksum_updated = get_checksum(finished_puzzle_updated)
# 6467287700366 too low
# 14402909062923 too high
# 13985513481853 not right
# 14381147236629 not right

# print(checksum)
print(checksum_updated)

