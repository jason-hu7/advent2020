# day 4 passport processing
"""
passports are required to have the following fields:
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

* cid is optional for now
"""
from utils import read_day4_inputs

def valid_passports(passports, required_fields):
    valid = 0
    for passport in passports:
        if required_fields.issubset(set(passport.keys())):
            valid += 1
    return valid



if __name__ == "__main__":
    required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

    # test
    test_path = "inputs/day4_test.txt"
    test_passports = read_day4_inputs(test_path)
    assert valid_passports(test_passports, required_fields) == 2

    # part 1
    input_path = "inputs/day4.txt"
    passports = read_day4_inputs(input_path)
    print("part1: ", valid_passports(passports, required_fields))
