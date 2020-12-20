import re
must_have = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
optional = {'cid'}

BYR_LOWER = 1920
BYR_UPPER = 2002
IYR_LOWER = 2010
IYR_UPPER = 2020
EYR_LOWER = 2020
EYR_UPPER = 2030
HCL_PATTERN = '#[0-9|a-f]{6}$'
ECL_PATTERN = '(amb|blu|brn|gry|grn|hzl|oth)$'
PID_PATTERN = '\d{9}$'

def validate_yr(yr_text, lower_lim, upper_lim):
    """
    byr: 1920, 2002
    iyr: 2010, 2020
    eyr: 2020, 2030
    """
    try:
        if len(yr_text) != 4:
            return False
        byr = int(yr_text)
        return lower_lim <= byr <= upper_lim
    except ValueError:
        return False


def validate_hgt(hgt_text):
    pattern = '(\d+)(in|cm)'
    pattern = re.compile(pattern)
    res = re.match(pattern, hgt_text)
    if res:
        num, unit = res.groups()
        if unit == 'cm':
            return 150 <= int(num) <= 193
        if unit == 'in':
            return 59 <= int(num) <= 76
    return False


def validate_pattern(text, pattern):
    pattern = re.compile(pattern)
    res = re.match(pattern, text)
    return bool(res)


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
    valid_docs = []
    for doc in docs:
        if must_have <= set(doc.keys()):
            valid_docs.append(doc)
    return valid_docs

def validate_doc(doc):
    validations = []
    # byr
    validations.append(validate_yr(doc['byr'], BYR_LOWER, BYR_UPPER))
    validations.append(validate_yr(doc['iyr'], IYR_LOWER, IYR_UPPER))
    validations.append(validate_yr(doc['eyr'], EYR_LOWER, EYR_UPPER))
    validations.append(validate_hgt(doc['hgt']))
    validations.append(validate_pattern(doc['hcl'], HCL_PATTERN))
    validations.append(validate_pattern(doc['ecl'], ECL_PATTERN))
    validations.append(validate_pattern(doc['pid'], PID_PATTERN))
    return all(validations)

def validate(docs):
    validated_docs= []
    for doc in docs:
        if validate_doc(doc):
            validated_docs.append(doc)
    return validated_docs

if __name__ == "__main__":
    # print(len(solve("day04_test.txt")))
    # 2
    # print(len(solve("day04.txt")))
    unvalidated_docs = solve("day04.txt")
    validated_docs = validate(unvalidated_docs)
    print(len(validated_docs))
