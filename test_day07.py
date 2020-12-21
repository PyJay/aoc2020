from day07 import create_mapping, search_parents

def test_example():
    res = create_mapping('day07_test.txt')
    counter = search_parents(res, 'shiny gold')
    assert 4 == counter