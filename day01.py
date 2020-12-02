import itertools as it

def fix_expense_report_part_1(input_list):
    for i in input_list:
        other = 2020 - i
        if other in input_list:
            return i * other

def fix_expense_report_part_2(input_list):
    combinations = it.combinations(input_list, 2)
    sum_map = {sum(c): c for c in combinations}
    for i in input_list:
        rem = 2020 - i
        if rem in sum_map:
            j, k = sum_map[rem]
            return i * j * k

if __name__ == "__main__":
    with open('day01.txt') as f:
        input_list = f.readlines()
    input_list = [int(i) for i in input_list]
    print(fix_expense_report_part_2(input_list))