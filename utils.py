## utils

def read_day1_inputs(filepath):
    with open(filepath, "r") as f:
        file = f.read().splitlines()
    file = [int(num) for num in file]
    return file


def read_day2_inputs(filepath):
    with open(filepath, "r") as f:
        file = f.read().splitlines()
    file = [line.split(": ") for line in file]
    return file


def read_day3_inputs(filepath):
    with open(filepath, "r") as f:
        file = f.read().splitlines()
    return file


def read_day4_inputs(filepath):
    with open(filepath, "r") as f:
        file = f.read().splitlines()

    passports = []
    passport = {}
    for line in file:
        if not line:
            passports.append(passport)
            passport = {}
        else:
            key_val_pairs = [key_val.split(":") for key_val in line.split(" ")]
            for key, val in key_val_pairs:
                passport[key] = val
    if passport:
        passports.append(passport)
    return passports


def read_day5_inputs(filepath):
    with open(filepath, "r") as f:
        file = f.read().splitlines()
    return file


def read_day6_inputs(filepath):
    with open(filepath, "r") as f:
        file = f.read().splitlines()

    groups = []
    group = []
    for line in file:
        if not line:
            groups.append(group)
            group = []
        else:
            group.append(line)
    if group:
        groups.append(group)
    return groups
