

def read_day1_inputs(filepath):
    with open(filepath, "r") as f:
        file = f.read().splitlines()
    file = [int(num) for num in file]
    return file
