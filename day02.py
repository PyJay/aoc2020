from collections import Counter

def check_password(min, max, letter, password): 
    counter = Counter(password)
    return min <= counter.get(letter, 0) <= max

def check_password_two(first, second, letter, password):
    return (password[first-1] == letter) ^ (password[second-1] == letter)

def parse_line(line):
    policy, letter_colon, password = line.split()
    min, max = policy.split('-')
    letter = letter_colon[0]
    return (int(min), int(max), letter, password)

def parse_text(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [parse_line(line) for line in lines]

if __name__ == "__main__":
    args_list = parse_text('day02.txt')
    res = [check_password_two(*args) for args in args_list]
    print(res.count(True))