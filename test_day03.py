from day03 import create_array, solve


def test_create_array():
    test_input = (
        "..#.",
        ".#..",
        "#...",
    )
    result = create_array(test_input)
    expect = [
        ['.', '.', '#', '.'],
        ['.', '#', '.', '.'],
        ['#', '.', '.', '.']
        ]
    assert expect == result


def test_solve():
    fname = 'day03_test.txt'
    assert 7 == solve(fname, 1, 3)
    assert 2 == solve(fname, 1, 1)
    assert 3 == solve(fname, 1, 5)
    assert 4 == solve(fname, 1, 7)
    assert 2 == solve(fname, 2, 1)
