from utils import read_day8_inputs
import copy


def run_program(instructions):
    accumulator = 0
    num_instructions = len(instructions)
    curr_ind = 0
    seen = set()
    while curr_ind < num_instructions:
        seen.add(curr_ind)
        instruction = instructions[curr_ind]
        code, num = instruction.split(" ")
        if code == "acc":
            accumulator += int(num)
            curr_ind += 1
        elif code == "jmp":
            curr_ind += int(num)
        else:
            curr_ind += 1
        if curr_ind in seen:
            break
    return accumulator


def run_program2(instructions):
    accumulator = 0
    num_instructions = len(instructions)
    curr_ind = 0
    seen = set()
    while curr_ind < num_instructions:
        seen.add(curr_ind)
        instruction = instructions[curr_ind]
        code, num = instruction.split(" ")
        if code == "acc":
            accumulator += int(num)
            curr_ind += 1
        elif code == "jmp":
            curr_ind += int(num)
        else:
            curr_ind += 1
        if curr_ind in seen:
            return None
    return accumulator


if __name__ == "__main__":

    #test
    test1 = read_day8_inputs("inputs/day8_test.txt")
    assert run_program(test1) ==  5

    # part1
    instructions = read_day8_inputs("inputs/day8.txt")
    print("part1: ", run_program(instructions))

    # part 2
    for i in range(len(instructions)):
        res = 0
        if "acc" in instructions[i]:
            res = run_program2(instructions)
        elif "jmp" in instructions[i]:
            copy1 = copy.deepcopy(instructions)
            copy1[i] =  copy1[i].replace("jmp", "nop")
            res = run_program2(copy1)
        elif "nop" in instructions[i]:
            copy1 = copy.deepcopy(instructions)
            copy1[i] =  copy1[i].replace("nop", "jmp")
            res = run_program2(copy1)
        if res:
            print("part2", res)
