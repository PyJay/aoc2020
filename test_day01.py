from day01 import fix_expense_report_part_1, fix_expense_report_part_2

def test_basic_example():
    input_list = [1721, 979, 366, 299, 675, 1456]
    assert 514579 == fix_expense_report_part_1(input_list)

def test_basic_example_part_2():
    input_list = [2017, 10, 20, 30, 2, 1]
    assert 2017 * 2 * 1 == fix_expense_report_part_2(input_list)