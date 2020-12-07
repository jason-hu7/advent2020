from utils import read_day7_inputs
from collections import defaultdict
import re


def build_graphs(color_inputs):
    contains = defaultdict(list)
    contained_in = defaultdict(list)
    for color_input in color_inputs:
        parent_color = re.findall(r'^(.+?) bags', color_input)[0]
        for cnt, color in re.findall(r'(\d+) (.+?) bags?[,.]', color_input):
            contains[parent_color].append((int(cnt), color))
            if parent_color not in contained_in[color]:
                contained_in[color].append(parent_color)
    return contains, contained_in


def contain_target_color(contained_graph, target_color):
    all_contains = set()
    def helper(color):
        for c in contained_graph[color]:
            all_contains.add(c)
            helper(c)
    helper(target_color)
    return len(all_contains)


if __name__ == "__main__":

    """
    process the luggage bags:
    """

    # test
    test1 = read_day7_inputs("inputs/day7_test.txt")
    contains, contained_in = build_graphs(test1)
    assert contain_target_color(contained_in, "shiny gold") == 4

    # part1
    color_rules = read_day7_inputs("inputs/day7.txt")
    contains, contained_in = build_graphs(color_rules)
    print("part 1: ", contain_target_color(contained_in, "shiny gold"))
