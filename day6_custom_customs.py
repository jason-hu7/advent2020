from utils import read_day6_inputs
from collections import Counter


def group_counts(group):
    all_inputs = "".join(group)
    counts = Counter(all_inputs)
    return len(counts)


def group_counts2(group):
    group_size = len(group)
    all_inputs = "".join(group)
    counts = Counter(all_inputs)
    ans = 0
    for i in counts.values():
        if i == group_size:
            ans+= 1
    return ans


if __name__ == "__main__":

    # tests
    test1 = read_day6_inputs("inputs/day6_test.txt")
    test1_sum = 0
    test2_sum = 0
    for group in test1:
        test1_sum += group_counts(group)
        test2_sum += group_counts2(group)
    assert test1_sum == 11
    assert test2_sum == 6


    # part1
    form_ans = read_day6_inputs("inputs/day6.txt")
    part1_sum = 0
    part2_sum = 0
    for group in form_ans:
        part1_sum += group_counts(group)
        part2_sum += group_counts2(group)
    print("part1: ", part1_sum)
    print("part2: ", part2_sum)


