from day02 import check_password, parse_text, check_password_two


def test_part_one():
    policy = (1, 3, "a")
    password_one = "abcd"
    password_two = "abacd"
    password_three = "abaad"
    password_four = "abaada"
    password_zero = "zbzzdz"
    assert check_password(*policy, password_one) == True
    assert check_password(*policy, password_two) == True
    assert check_password(*policy, password_three) == True
    assert check_password(*policy, password_four) == False
    assert check_password(*policy, password_zero) == False


def test_part_two():
    policy = (1, 3, "a")
    password_one = "abcd"  # valid
    password_two = "abacd"  # invalid
    password_three = "abbacd"  # valid
    password_four = "bbdada"  # invalid
    assert check_password_two(*policy, password_one) == True
    assert check_password_two(*policy, password_two) == False
    assert check_password_two(*policy, password_three) == True
    assert check_password_two(*policy, password_four) == False


def test_parse_text():
    assert [
        (9, 10, "x", "xxxxxxxxzv"),
        (2, 5, "q", "xdqbjj"),
        (17, 19, "n", "nnnnnnnnnnnnnnnnrnsn"),
    ] == parse_text("day02_test.txt")
