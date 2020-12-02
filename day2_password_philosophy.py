from utils import read_day2_inputs
from collections import Counter


def password_valid1(password, policy):
    occurances, letter = policy.split(" ")
    occr_min, occr_max = [int(occr) for occr in occurances.split("-")]
    counts = Counter(password)
    if occr_min <= counts[letter] <= occr_max:
        return True
    return False


def password_valid2(password, policy):
    occurances, letter = policy.split(" ")
    ind1, ind2 = map(int, occurances.split("-"))
    if (password[ind1-1] == letter) != (password[ind2-1] == letter):
        return 1
    return 0


if __name__ == "__main__":
    # read input
    FILEPATH = "inputs/day2.txt"
    policypass = read_day2_inputs(FILEPATH)

    # tests
    policy1, pass1 = "1-3 a", "abcde"
    policy2, pass2 = "1-3 b", "cdefg"
    policy3, pass3 = "2-9 c", "ccccccccc"
    assert password_valid1(pass1, policy1)
    assert not password_valid1(pass2, policy2)
    assert password_valid1(pass3, policy3)
    assert password_valid2(pass1, policy1)
    assert not password_valid2(pass2, policy2)
    assert not password_valid2(pass3, policy3)

    # part1
    valid_password1 = 0
    valid_password2 = 0
    for policy, password in policypass:
        if password_valid1(password, policy):
            valid_password1 += 1
        valid_password2 += password_valid2(password, policy)
    print("part1: ", valid_password1)
    print("part2: ", valid_password2)



