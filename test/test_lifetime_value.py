import pytest

from LTV_calc import *

ltv = CustomerLifetimeValue("model/LTV=USD34.96.csv")

@pytest.mark.skip("Fix LTV computation in the code")
def test_one_user():
    assert ltv.compute_lifetime_value("../test/model/LTV=USD34.96.csv") == pytest.approx(34.965, 0.004)

# TODO write more tests with different LTV

@pytest.mark.skip("Fix LTV computation in the code")
def test_number_of_users_is_one():
    assert ltv.get_number_of_users("../test/model/LTV=USD34.96.csv") == 1


@pytest.mark.skip("Fix LTV computation in the code")
def test_ltv_when_number_of_users_is_two():
    assert ltv.compute_lifetime_value("../test/model/two_users.csv") == pytest.approx(9.99*0.7*8/2, 0.004)


@pytest.mark.skip("Deprecated")
def test_conversion_rate():
    ltv.compute_lifetime_value("../test/model/LTV=USD34.96.csv")
    assert ltv.Conversion_percents == [1.0]

    ltv.compute_lifetime_value("../test/model/three_users.csv")
    assert ltv.Conversion_percents == [1.0, pytest.approx(2/3, 0.0001), 0.50]


def test_three_users():
    ltv = CustomerLifetimeValue("../test/model/three_users.csv")
    ltv.compute_lifetime_value()

@pytest.mark.skip("Fix LTV computation in the code")
def test_stat_table_one_user():
    ltv.compute_lifetime_value("../test/model/LTV=USD34.96.csv")
    print(":-", ltv.statTable)
    assert ltv.statTable['subscriptions'][0] == 6

@pytest.mark.skip("LTV computation in the code")
def test_compute_lifetime_value_when_four_users():
    assert ltv.compute_lifetime_value("../test/model/four_users_all_trial.csv") == 0
    assert ltv.compute_lifetime_value("../test/model/four_users_one_subscriber.csv") == 9.99*0.7 * 3 / 4
    assert ltv.compute_lifetime_value("../test/model/four_users_02.csv") == 9.99*0.7
#def test_compute_lifetime_value_when_four_users():
#    assert ltv.compute_lifetime_value("../test/model/five_users.csv") == 10 * 0.7 * 9.

#@pytest.mark.skip("To be implemented by Valerii")
def test_compute_relative_user_conversion_rate():
    ltv = CustomerLifetimeValue("model/LTV=USD34.96.csv")
    assert ltv.compute_relative_user_conversion_rate_or_raise_error([8, 4]) == [0.5]
    assert ltv.compute_relative_user_conversion_rate_or_raise_error([8, 4, 3]) == [0.5, 0.75]
    assert ltv.compute_relative_user_conversion_rate_or_raise_error([15, 13, 12, 11, 10, 3]) == [13 / 15, 12 / 13, 11 / 12, 10 / 11, 3 / 10]

    with pytest.raises(ValueError):
        ltv.compute_relative_user_conversion_rate_or_raise_error([4, 3])
        
@pytest.mark.skip("To be implemented by Valerii")
def test_functions_talk():
    ltv = CustomerLifetimeValue("model/dummy.csv")
    at_least_subscription = (2, 4, 6)
    num_of_trial_users = 5
    user_retention = (num_of_trial_users, 3, 1)
    #trial, week1, w2, w3,w4,w5
    #  [5,   5,    3,  3, 1, 1]
    assert ltv.compute_lifetime_value_using_numbers_of_user_retention(at_least_subscription, user_retention) == (5+3+3+1+1)*9.99*0.7 / num_of_trial_users


def test_integration_whole_system_total_ltv():
    ltv = CustomerLifetimeValue("../src/data_analytics.csv")
    assert 5 < ltv.compute_lifetime_value() < 40
    print(ltv.compute_lifetime_value())
    #assert ltv.compute_lifetime_value("../src/data_analytics.csv") == -1