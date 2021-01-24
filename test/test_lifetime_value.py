import pytest

from LTV_calc import *

ltv = CustomerLifetimeValue()

def test_one_user():
    assert ltv.compute_lifetime_value("../test/model/LTV=USD34.96.csv") == pytest.approx(34.965, 0.004)

# TODO write more tests with different LTV


def test_number_of_users_is_one():
    assert ltv.get_number_of_users("../test/model/LTV=USD34.96.csv") == 1


def test_ltv_when_number_of_users_is_two():
    assert ltv.compute_lifetime_value("../test/model/two_users.csv") == pytest.approx(27.971999999999998, 0.004)


def test_conversion_rate():
    ltv.compute_lifetime_value("../test/model/LTV=USD34.96.csv") == pytest.approx(34.965, 0.004)
    assert ltv.Conversion_percents == [1.0]

    ltv.compute_lifetime_value("../test/model/three_users.csv") == pytest.approx(34.965, 0.004)
    assert ltv.Conversion_percents == [1.0, pytest.approx(2/3, 0.0001), 0.50]


def test_stat_table_one_user():
    ltv.compute_lifetime_value("../test/model/LTV=USD34.96.csv")
    print(":-", ltv.statTable)
    assert ltv.statTable['subscriptions'][0] == 6

# def test_stat_table():
#     ltv.compute_lifetime_value("../test/model/three_users.csv")
#     print(":-", ltv.statTable)
#     print("_", np.array(ltv.statTable['conversion'][:]), "len", len(np.array(ltv.statTable['conversion'][1:])))
#     assert ltv.statTable == 0
#
# def test_stat_table():
#     ltv.compute_lifetime_value("../test/model/two_users.csv")
#     print(":-", ltv.statTable)
#     print("_", np.array(ltv.statTable['conversion'][:]), "len", len(np.array(ltv.statTable['conversion'][1:])))
#     assert ltv.statTable == 0
#def test_ltv_when_number_of_users_is_two():
#    assert ltv.compute_lifetime_value("../test/three_users") == pytest.approx(9*0.99*0.7, 0.004)