import pytest

from ltv_entity import *


def test_one_user():
    ltv = CustomerLifetimeValue("../test/model/LTV=USD34.96.csv")
    assert ltv.compute_relative_user_conversion_rate_or_raise_error([1, 1, 1, 1, 1])
    assert ltv.compute_ltv_main() == pytest.approx(34.965, 0.004)



def test_ltv_when_number_of_users_is_two():
    ltv = CustomerLifetimeValue("../test/model/two_users.csv")
    assert ltv.compute_relative_user_conversion_rate_or_raise_error([2, 2, 2, 2, 1, 1]) == [1, 1, 1, 0.5, 1]
    assert ltv.compute_ltv_main() == pytest.approx(9.99 * 0.7 * 8 / 2, 0.004)


def test_conversion_rate():
    ltv = CustomerLifetimeValue("../test/model/LTV=USD34.96.csv")
    assert ltv.compute_relative_user_conversion_rate_or_raise_error(ltv.compute_retention()) == [1.0, 1.0, 1.0, 1.0, 1.0]
    ltv = CustomerLifetimeValue("../test/model/dummy.csv")
    assert ltv.compute_relative_user_conversion_rate_or_raise_error([3, 3, 2, 1, 1]) == [1.0, pytest.approx(2 / 3, 0.0001), 0.50, 1]


def test_ltv_for_three_users():
    ltv = CustomerLifetimeValue("../test/model/three_users.csv")
    assert ltv.compute_retention() == [3, 3, 3, 2, 1]

    assert ltv.compute_relative_user_conversion_rate_or_raise_error([3, 3, 3, 2, 1]) == [1, 1, pytest.approx(2 / 3, 0.0001), 0.5]
    assert ltv.compute_lifetime_value_using_conversions([1, 1, 2 / 3, 0.5]) == (9)*9.99*.7 / 3


def test_compute_lifetime_value_when_four_users():
    ltv = CustomerLifetimeValue("../test/model/four_users_all_trial.csv")
    assert ltv.compute_ltv_main() == 0
    ltv = CustomerLifetimeValue("../test/model/four_users_one_subscriber.csv")
    assert ltv.compute_ltv_main() == 9.99 * 0.7 * 3 / 4



def test_compute_relative_user_conversion_rate():
    ltv = CustomerLifetimeValue("model/LTV=USD34.96.csv")
    assert ltv.compute_relative_user_conversion_rate_or_raise_error([8, 4]) == [0.5]
    assert ltv.compute_relative_user_conversion_rate_or_raise_error([8, 4, 3]) == [0.5, 0.75]
    assert ltv.compute_relative_user_conversion_rate_or_raise_error([15, 13, 12, 11, 10, 3]) == [13 / 15, 12 / 13, 11 / 12, 10 / 11, 3 / 10]

    with pytest.raises(ValueError):
        ltv.compute_relative_user_conversion_rate_or_raise_error([3,4])


def test_functions_talk():
    ltv = CustomerLifetimeValue("model/dummy.csv")
    num_of_trial_users = 5
    #trial, week1, w2, w3,w4,w5
    #  [5,   5,    3,  3, 1, 1]
    assert ltv.compute_lifetime_value_using_conversions([5/5, 3/5, 3/3, 1/3, 1/1]) == pytest.approx((5+3+3+1+1)*9.99*0.7 / num_of_trial_users, 0.001)

    at_least_subscription = (2, 4, 6)



def test_integration_whole_system_total_ltv():
    ltv = CustomerLifetimeValue("../src/data_analytics.csv")
    assert 5 < ltv.compute_ltv_main() < 40
    assert ltv.compute_ltv_main() == pytest.approx(9.34, 0.001)