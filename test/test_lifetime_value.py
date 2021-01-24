import pytest

from LTV_calc import *

ltv = CustomerLifetimeValue()

def test_nothing():
    assert ltv.compute_lifetime_value("../test/LTV=USD34.96.csv") == pytest.approx(34.965, 0.004)

# TODO write more tests with different LTV


def test_number_of_users_is_one():
    assert ltv.get_number_of_users("../test/LTV=USD34.96.csv") == 1


def test_ltv_when_number_of_users_is_two():
    assert ltv.compute_lifetime_value("../test/two_users") == pytest.approx(5.544, 0.004)