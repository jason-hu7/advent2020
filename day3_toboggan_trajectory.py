# toboggan trajectory
from utils import read_day3_inputs

def count_trees(area_map, slope=(3, 1)):
    right, down = slope
    trees = 0
    rows = len(area_map)
    map_width = len(area_map[0])
    start = (0, 0)
    while start[0] < rows:
        i, j = start
        if area_map[i][j%map_width] == "#":
            trees += 1
        start = (i+down, j+right)
    return trees


def count_trees_recur(area_map, i, j, trees, slope):
    if i >= len(area_map):
        return trees
    right, down = slope
    return count_trees_recur(area_map, i+down, j+right, trees+(area_map[i][j%len(area_map[0])]=="#"), slope)


if __name__ == "__main__":

    test1 = read_day3_inputs("inputs/day3_test1.txt")
    assert count_trees(test1) == 7
    assert count_trees_recur(test1, 0, 0, 0, (3,1)) == 7

    # part 1
    FILEPATH = "inputs/day3.txt"
    map1 = read_day3_inputs(FILEPATH)
    print("part1: ", count_trees(map1))

    # part 2
    assert count_trees(test1, (1, 1)) == 2
    assert count_trees(test1, (3, 1)) == 7
    assert count_trees(test1, (5, 1)) == 3
    assert count_trees(test1, (7, 1)) == 4
    assert count_trees(test1, (1, 2)) == 2
    assert count_trees_recur(test1, 0, 0, 0, (1,1)) == 2
    assert count_trees_recur(test1, 0, 0, 0, (3,1)) == 7
    assert count_trees_recur(test1, 0, 0, 0, (5,1)) == 3
    assert count_trees_recur(test1, 0, 0, 0, (7,1)) == 4
    assert count_trees_recur(test1, 0, 0, 0, (1,2)) == 2

    print("part2: ", count_trees(map1, (1,1))*count_trees(map1, (3,1))* count_trees(map1, (5,1)) * count_trees(map1, (7,1)) * count_trees(map1, (1,2)))
