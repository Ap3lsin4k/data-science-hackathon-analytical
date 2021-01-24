import pytest

from LTV_calc import *

ltv = CustomerLifetimeValue()

def test_one_user():
    assert ltv.compute_lifetime_value("../test/model/LTV=USD34.96.csv") == pytest.approx(34.965, 0.004)

# TODO write more tests with different LTV


def test_number_of_users_is_one():
    assert ltv.get_number_of_users("../test/model/LTV=USD34.96.csv") == 1


def test_ltv_when_number_of_users_is_two():
    assert ltv.compute_lifetime_value("../test/model/two_users.csv") == pytest.approx(9.99*0.7*8/2, 0.004)


@pytest.mark.skip("Deprecated")
def test_conversion_rate():
    ltv.compute_lifetime_value("../test/model/LTV=USD34.96.csv")
    assert ltv.Conversion_percents == [1.0]

    ltv.compute_lifetime_value("../test/model/three_users.csv")
    assert ltv.Conversion_percents == [1.0, pytest.approx(2/3, 0.0001), 0.50]


def test_three_users():
    ltv.compute_lifetime_value("../test/model/three_users.csv")


def test_stat_table_one_user():
    ltv.compute_lifetime_value("../test/model/LTV=USD34.96.csv")
    print(":-", ltv.statTable)
    assert ltv.statTable['subscriptions'][0] == 6


def test_compute_lifetime_value_when_four_users():
    assert ltv.compute_lifetime_value("../test/model/four_users_all_trial.csv") == 0
    assert ltv.compute_lifetime_value("../test/model/four_users_one_subscriber.csv") == 9.99*0.7 * 3 / 4
    assert ltv.compute_lifetime_value("../test/model/four_users_02.csv") == 9.99*0.7
#def test_compute_lifetime_value_when_four_users():
#    assert ltv.compute_lifetime_value("../test/model/five_users.csv") == 10 * 0.7 * 9.


def test_integration_whole_system_total_ltv():
    assert 5 < ltv.compute_lifetime_value("../src/data_analytics.csv") < 40
    print(ltv.compute_lifetime_value("../src/data_analytics.csv"))
    #assert ltv.compute_lifetime_value("../src/data_analytics.csv") == -1

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