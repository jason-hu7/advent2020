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
