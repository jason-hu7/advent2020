# Find a combination of 2 numbers that sum to 2020

from utils import read_day1_inputs
import math


def two_sum(expenses, target=2020):
    seen = set()
    for expense in expenses:
        residual = target - expense
        if residual in seen:
            return (expense, residual)
        else:
            seen.add(expense)
    print("no pairs")
    return None


def three_sum(expenses, target=2020):
    expenses.sort()
    for i, expense in enumerate(expenses):
        residual = target - expense
        left, right = i+1, len(expenses)-1
        while left < right:
            curr_sum = expenses[left]+expenses[right]
            if curr_sum == residual:
                return (expense, expenses[left], expenses[right])
            if curr_sum < residual:
                left += 1
            else:
                right -= 1
    print("nothing")
    return (None, None, None)


if __name__ == "__main__":
    # tests
    test1 = [1721, 979, 366, 299, 675, 1456]
    test1_ans = two_sum(test1)
    assert math.prod(test1_ans) ==  514579

    test2_ans = three_sum(test1)
    assert math.prod(test2_ans) == 241861950

    # get ans
    INPUT_PATH = "inputs/day1.txt"
    expenses = read_day1_inputs(INPUT_PATH)
    ans = two_sum(expenses)
    print("day1 answer is: ", math.prod(ans))


    # get ans part 2
    assert len(set(expenses)) == len(expenses)
    ans2 = three_sum(expenses)
    print("part2 answer is: ", math.prod(ans2))






