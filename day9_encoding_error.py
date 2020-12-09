
from utils import read_day9_inputs
from day1_report_repair import two_sum


"""
1
.
.
.
25th -> 25
26th -> 45
"""

def find_error_num(nums, preamble_len):
    assert len(nums) >= preamble_len
    left, right = 0, preamble_len
    while right <= len(nums):
        window = nums[left:right]
        if not two_sum(window, nums[right]):
            return nums[right]
        left += 1
        right += 1
    print("no error")
    return None


def get_contiguous_set(nums, target):
    nums_len = len(nums)
    for left in range(nums_len-1):
        for right in range(left+2, nums_len):
            if sum(nums[left:right]) == target:
                return nums[left:right]
            if sum(nums[left:right]) > target:
                break
    return None



if __name__ == "__main__":

    #tests
    test1 = read_day9_inputs("inputs/day9_test.txt")
    assert find_error_num(test1, 5) == 127
    contig_set = get_contiguous_set(test1, 127)
    assert (min(contig_set)+max(contig_set)) == 62

    # part 1
    nums = read_day9_inputs("inputs/day9.txt")
    error_num = find_error_num(nums, 25)
    print("part1: ", error_num)

    # part2
    contig_set = get_contiguous_set(nums, error_num)
    print("part2: ", min(contig_set)+max(contig_set))



