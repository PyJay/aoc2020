from day02 import check_password, parse_text

def test_basic_case():
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


def test_parse_text():
    assert [
        (9, 10, "x", "xxxxxxxxzv"),
        (2, 5, "q", "xdqbjj"),
        (17, 19, "n", "nnnnnnnnnnnnnnnnrnsn"),
    ] == parse_text("day02_test.txt")
