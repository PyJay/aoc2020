from collections import Counter

def solve(fname):
    with open(fname) as f:
        all_groups = f.read().splitlines()
    split_groups = []
    group = set()
    for entry in all_groups:
        if entry == '':
            split_groups.append(group)
            group = set()
        else:
            group.update(list(entry))
    # add the last group - not very graceful
    split_groups.append(group)
    return sum(len(x) for x in split_groups)

def solve_two(fname):
    with open(fname) as f:
        all_groups = f.read().splitlines()
    split_groups = []
    group = []
    for entry in all_groups:
        if entry == '':
            split_groups.append(group)
            group = []
        else: 
            group.append(list(entry))
    # add the last group - not very graceful
    split_groups.append(group)
    yes_counts = []
    for group in split_groups:
        yes_count = 0
        group_count = len(group)
        counter = Counter()
        for survey in group:
            counter.update(survey)
        for res in counter:
            if counter.get(res, 0) == group_count:
                yes_count += 1
        yes_counts.append(yes_count)
            
    return sum(yes_counts)


if __name__ == "__main__":
    print(solve_two('day06.txt'))