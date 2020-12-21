

def sum_possible(total, numbers):
    # given a list of numbers check if total is possibly by adding any two numbers
    for n in numbers:
        if total-n != n and (total - n) in numbers:
            return True
    return False

def solve(lines, preamble):
    lines = [int(i) for i in lines]
    numbers_start_index = 0
    numbers_stop_index = preamble
    while numbers_stop_index <= len(lines) - 1:
        # print(numbers_start_index, numbers_stop_index)
        total = lines[numbers_stop_index]
        numbers = lines[numbers_start_index:numbers_stop_index]
        if not sum_possible(total, numbers):
            return total
        numbers_start_index += 1
        numbers_stop_index += 1

def find_set(lines, number):
    lines = [int(i) for i in lines]
    start = 0
    stop = 1
    total = None
    while stop <= len(lines) + 1:
        total = sum(lines[start:stop])
        if total == number:
            return lines[start:stop]
        if total < number:
            stop += 1
        if total > number:
            start += 1
            stop = start + 1


def test_sum_possible():
    assert sum_possible(26, range(1, 26))
    assert sum_possible(49, range(1, 26))
    assert not sum_possible(100, range(1, 26))
    assert not sum_possible(50, range(1, 26))

test_text = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

def test_example():
    output = solve(lines=test_text.splitlines(), preamble=5)
    assert 127 == output

def test_example_two():
    output = find_set(lines=test_text.splitlines(), number=127)
    assert [15, 25, 47, 40] == output


if __name__ == "__main__":
    with open('day09.txt') as f:
        lines = f.read().splitlines()
    # print(solve(lines, 25))
    number_set = find_set(lines=lines, number=1038347917)
    print(min(number_set) + max(number_set))