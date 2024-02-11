from main_functions import check_number


def test_check_number_more():
    assert check_number(10, 8) == 'more'


def test_check_number_less():
    assert check_number(8, 10) == 'less'


def test_check_number_equal():
    assert check_number(8, 8) == 'equal'