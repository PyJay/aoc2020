must_have = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
optional = {'cid'}


def solve(fname):
    with open(fname) as f:
        text = f.read()
    travel_docs = text.split('\n\n')
    docs = []
    for doc in travel_docs:
        doc.replace('\n', ' ')
        k_v_pairs = doc.split()
        doc_list = [pair.split(':') for pair in k_v_pairs]
        docs.append(dict(doc_list))
    valid = 0
    for doc in docs:
        if must_have <= set(doc.keys()):
            valid += 1
    return valid


if __name__ == "__main__":
    # print(solve("day04_test.txt"))
    # 2
    print(solve("day04.txt"))
