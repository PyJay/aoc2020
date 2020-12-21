from collections import Counter

def solve(jolts_str):
    jolts = [int(j) for j in jolts_str]
    jolts.sort(reverse=True)
    current = 0
    diffs = []
    while jolts:
        next_adapter = jolts.pop()
        diff =  next_adapter - current
        assert diff in [1,2,3]
        diffs.append(diff)
        current = next_adapter
    diffs.append(3) # difference between device and final joltage
    return Counter(diffs)

test_text = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

def test_example():
    foo = solve(test_text.splitlines())
    assert {1: 22, 3: 10} == foo

if __name__ == "__main__":
    with open('day10.txt') as f:
        lines = f.read().splitlines()
    res = solve(lines)
    print(res[3] * res[1])