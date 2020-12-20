from day05 import get_id

def test_example():
    boarding_pass = 'FBFBBFFRLR'
    assert 357 == get_id(boarding_pass)