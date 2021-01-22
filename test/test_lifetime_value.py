import pytest

from LTV_calc import *

ltv = CustomerLifetimeValue()

def test_nothing():
    assert ltv.compute_lifetime_value("../test/LTV=USD34.96.csv") == pytest.approx(34.965, 0.004)

def test_number_of_users_is_one():
    assert ltv.get_number_of_users("../test/LTV=USD34.96.csv") == 1
