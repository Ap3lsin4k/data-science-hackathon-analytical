from LTV_calc import *


def test_nothing():
    assert compute_lifetime_value("../test/LTV=USD34.96.csv") == 34.965


def test_number_of_users_is_one():
    assert get_number_of_users("../test/LTV=USD34.96.csv") == 1
