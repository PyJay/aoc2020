def get_id(boarding_pass):
    upper_row = 127
    lower_row = 0
    upper_col = 7
    lower_col = 0
    boarding_pass = list(boarding_pass)
    for _ in range(7):
        letter = boarding_pass.pop(0)
        assert letter in ['F', 'B']
        mid_point = (upper_row - lower_row) // 2
        if letter == 'F':
            upper_row = lower_row + mid_point
        if letter == 'B':
            lower_row = lower_row + mid_point + 1

    for _ in range(3):
        letter = boarding_pass.pop(0)
        assert letter in ['L', 'R']
        mid_point = (upper_col - lower_col) // 2
        if letter == 'L':
            upper_col = lower_col + mid_point
        if letter == 'R':
           lower_col = lower_col + mid_point + 1
    col = lower_col
        
    row = lower_row
    return row * 8 + col

if __name__ == "__main__":
    with open('day05.txt') as f:
        passes = f.read().splitlines()
    ids = [get_id(p) for p in passes]
    max_id = max(ids)
    print(max_id)
    min_id = min(ids)
    full_set = {i for i in range(min_id, max_id+1)}
    print(full_set - set(ids))