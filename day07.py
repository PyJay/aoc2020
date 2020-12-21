import re
from collections import deque


def create_mapping(fname):
    with open(fname) as f:
        rules = f.read().splitlines()
    mapping = {}
    pattern = re.compile('(.+) bags contain|(\d+) (.+?) bag')
    for r in rules:
        matches = re.findall(pattern, r)
        parent, *children = matches
        parent = parent[0]
        children = {child[2]: int(child[1]) for child in children}
        mapping[parent] = children
    return mapping


def search_parents(mapping, node):
    all_parents = set()
    visited = set()
    to_check = deque([node])
    while to_check:
        child = to_check.pop()
        parents = []
        for bag in mapping:
            if child not in visited and child in mapping[bag]:
                parents.append(bag)
        to_check.extendleft(parents)
        all_parents.update(parents)
    return all_parents


def total_bags(mapping, bag):
    counter = 1 # the bag itself
    for inside_bag, number in mapping[bag].items():
        if not mapping[inside_bag]:
            counter += number
        else:
            inside_bag_count = (number * total_bags(mapping, inside_bag))
            counter += inside_bag_count
    return counter


if __name__ == "__main__":
    res = create_mapping('day07.txt')
    # print(len(search_parents(res, 'shiny gold')))
    print(total_bags(res, 'shiny gold')- 1  )