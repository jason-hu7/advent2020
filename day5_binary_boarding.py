# seat people using binary partitioning
# first 7 characters are F or B
# 128 rows on the plane
# 8 cols on the plane
# unique_id = 8 * row + col
from utils import read_day5_inputs
import math


ROWS = 128
COLS = 8


def get_row(boarding_pass):
    left, right = 0, ROWS - 1
    curr_ind = 0
    curr_code = boarding_pass[curr_ind]
    while curr_code in ("F", "B"):
        if curr_code == "F":
            right = (left+right) // 2
        if curr_code == "B":
            left = math.ceil((left+right) / 2)
        curr_ind += 1
        if curr_ind >= len(boarding_pass):
            raise Exception("wrong")
        curr_code = boarding_pass[curr_ind]
    last_ind = curr_ind - 1
    return left if boarding_pass[last_ind] == "F" else right


def get_col(boarding_pass):
    left, right = 0, COLS - 1
    curr_ind = 0
    while curr_ind < len(boarding_pass):
        curr_code = boarding_pass[curr_ind]
        if curr_code == "L":
            right = (left+right) // 2
        if curr_code == "R":
            left = math.ceil((left+right) / 2)
        curr_ind += 1
    return left if boarding_pass[-1] == "L" else right


def get_id(row, col):
    return 8 * row + col



if __name__ == "__main__":
    # tests
    test1 = "BFFFBBFRRR"
    test2 = "FFFBBBFRRR"
    test3 = "BBFFBBFRLL"
    assert get_row(test1) == 70
    assert get_col(test1) == 7
    assert get_row(test2) == 14
    assert get_col(test2) == 7
    assert get_row(test3) == 102
    assert get_col(test3) == 4

    boarding_passes = read_day5_inputs("inputs/day5.txt")
    ids = []
    for boarding_pass in boarding_passes:
        row = get_row(boarding_pass)
        col = get_col(boarding_pass)
        ids.append(get_id(row, col))
    print("part1", max(ids))

    ids_len = len(ids)
    missing_id = (min(ids)+max(ids))//2*(ids_len+1) - sum(ids)
    print("part2", missing_id)
