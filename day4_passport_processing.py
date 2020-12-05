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
import re

def valid_passports(passports, required_fields):
    valid = 0
    for passport in passports:
        if required_fields.issubset(set(passport.keys())):
            valid += 1
    return valid


def valid_passports2(passports, required_fields):
    """
    New rules for part 2:
        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.
    """
    valid = 0
    for passport in passports:
        if required_fields.issubset(set(passport.keys())):
            byr = passport["byr"]
            if len(byr)!=4 or int(byr) < 1920 or int(byr) > 2002:
                continue
            iyr = passport["iyr"]
            if len(iyr)!=4 or int(iyr) < 2010 or int(iyr) > 2020:
                continue
            eyr = passport["eyr"]
            if len(eyr)!=4 or int(eyr) < 2020 or int(eyr) > 2030:
                continue
            hgt = passport["hgt"]
            if "cm" in hgt:
                cm = int(re.findall(r"\d+", hgt)[0])
                if cm < 150 or cm > 193:
                    continue
            elif "in" in hgt:
                inch = int(re.findall(r"\d+", hgt)[0])
                if inch < 59 or inch > 76:
                    continue
            else:
                continue
            hcl = passport["hcl"]
            if not re.fullmatch(r"#[0-9a-f]{6}", hcl):
                continue
            ecl = passport["ecl"]
            valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if ecl not in valid_colors:
                continue
            pid = passport["pid"]
            if not re.fullmatch(r"^[0-9]{9}", pid):
                continue
            valid += 1
    return valid


if __name__ == "__main__":
    required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

    # test
    test_path = "inputs/day4_test.txt"
    test_passports = read_day4_inputs(test_path)
    assert valid_passports(test_passports, required_fields) == 2
    test_path2 = "inputs/day4_test2.txt"
    test_passports2 = read_day4_inputs(test_path2)
    assert valid_passports2(test_passports2, required_fields) == 4

    # part 1
    input_path = "inputs/day4.txt"
    passports = read_day4_inputs(input_path)
    print("part1: ", valid_passports(passports, required_fields))

    # part 2
    print("part2: ", valid_passports2(passports, required_fields))
