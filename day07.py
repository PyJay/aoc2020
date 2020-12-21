import re


def create_mapping(fname):
    with open(fname) as f:
        rules = f.read().splitlines()
    mapping = {}
    parent_pattern = re.compile('(.+) bags')
    child_pattern = re.compile('(\d+) (.+) bag[s]?|no other bag.')
    for r in rules:
        # res = re.match(pattern, r)
        parent_text, children_text = r.split('contain')
        result = re.match(parent_pattern, parent_text)
        parent = result.groups()[0]
        children_texts = children_text.split(',')
        children_texts = [c.strip() for c in children_texts]
        children = {}
        for c in children_texts:
            result = re.match(child_pattern, c)
            groups = result.groups()
            if not groups[1]:
                children = {}
            else:
                children[groups[1]] = groups[0]
        mapping[parent] = children
    return mapping


def search_parents(parent_mapping, node):
    counter = 0

    def exists_in_bag(bag, node):
        bag = parent_mapping[bag]
        if node in bag:
            return True
        for child in bag:
            return exists_in_bag(child, node)
        return False
    
    for bag in parent_mapping:
        if exists_in_bag(bag, node):
            counter += 1
    return counter


if __name__ == "__main__":
    res = create_mapping('day07.txt')
    breakpoint()
    print(search_parents(res, 'shiny gold'))
