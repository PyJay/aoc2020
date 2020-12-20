from day04 import (validate_hgt, validate_yr, BYR_LOWER,
                   BYR_UPPER, validate_pattern, HCL_PATTERN, ECL_PATTERN, PID_PATTERN)


def test_validate_yr():
    byr_valid = '2002'
    byr_invalid = '2003'
    assert True == validate_yr(byr_valid, BYR_LOWER, BYR_UPPER)
    assert False == validate_yr(byr_invalid, BYR_LOWER, BYR_UPPER)


def test_validate_hgt():
    hgt_valid_one = '60in'
    hgt_valid_two = '190cm'
    hgt_invalid_one = '190in'
    hgt_invalid_two = '190'
    assert True == validate_hgt(hgt_valid_one)
    assert True == validate_hgt(hgt_valid_two)
    assert False == validate_hgt(hgt_invalid_one)
    assert False == validate_hgt(hgt_invalid_two)


def test_validate_hcl():
    hcl_valid = '#123abc'
    hcl_invalid_one = '#123abz'
    hcl_invalid_two = '123abc'
    assert True == validate_pattern(hcl_valid, HCL_PATTERN)
    assert False == validate_pattern(hcl_invalid_one, HCL_PATTERN)
    assert False == validate_pattern(hcl_invalid_two, HCL_PATTERN)


def test_validate_ecl():
    ecl_valid = 'brn'
    ecl_invalid = 'wat'
    assert True == validate_pattern(ecl_valid, ECL_PATTERN)
    assert False == validate_pattern(ecl_invalid, ECL_PATTERN)


def test_validate_pid():
    pid_valid = '000000001'
    pid_invalid = '0123456789'
    assert True == validate_pattern(pid_valid, PID_PATTERN)
    assert False == validate_pattern(pid_invalid, PID_PATTERN)
