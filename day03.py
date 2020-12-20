def create_array(input_lines):
    res = []
    for l in input_lines:
        row = []
        for c in l:
            row.append(c)
        res.append(row)
    return res


def solve(fname, row_steps, col_steps):
    with open(fname) as f:
        lines = f.read().split('\n')
    tree_array = create_array(lines)
    row = 0
    col = 0
    tree_counter = 0
    while row <= len(tree_array) - 1:
        if tree_array[row][col] == '#':
                tree_counter += 1
        col = (col + col_steps) % len(tree_array[row])
        row += row_steps
    return tree_counter


if __name__ == "__main__":
    fname = 'day03.txt'
    print(solve(fname, 1, 1) * solve(fname, 1, 3) * solve(fname, 1, 5) * solve(fname, 1, 7) * solve(fname, 2, 1))
