import pytest

from ltv_entity import CustomerLifetimeValue

def test_retention_for_one_user():
    ltv = CustomerLifetimeValue("model/LTV=USD34.96.csv")
    res = ltv.compute_retention()
    print("__",res)
    assert len(res) == 6
    assert res[0] == 1
    assert res[1] == res[2] == res[3] == res[4] == res[5] == 1


def test_retention_for_two_users():
    ltv = CustomerLifetimeValue("model/two_users.csv")
    res = ltv.compute_retention()
    assert res[0] == 2
    assert res[1] == 2
    assert res == [2, 2, 2, 2, 1, 1]
    assert len(res) == 6

@pytest.mark.skip("It aggregates instead of giving the result")
def test_conversion_percent():
    ltv = CustomerLifetimeValue("model/two_users.csv")
    assert ltv.compute_conversion_percents() == [1, 1, 1, 0.5, 0.5]


# TODO test for users with less than 5 subscriptions
@pytest.mark.skip("TODO")
def test_active_users_for_each_week_including_trial():
    ltv = CustomerLifetimeValue("model/two_users.csv")
    res = ltv.compute_active_users_for_each_week()
    assert res == [2, 2, 2, 2, 1, 1]
    assert len(res) == 6
    assert res[0] == 2


def test_extract_out_retention_weeks_including_trial():
    ltv = CustomerLifetimeValue("model/two_users.csv")
    res = ltv.extract_active_users((3, 6),(2, 1))
    assert res == [2, 2, 2, 1, 1, 1]

    res = ltv.extract_active_users((1, 2, 3, 5), (10, 5, 3, 1))
    assert res == [10, 5, 3, 1, 1]

    res = ltv.extract_active_users((3, 6),(2, 1))
    assert res == [2, 2, 2, 1, 1, 1]

    with pytest.raises(ValueError):
        ltv.extract_active_users((1,3,5), (10, 5, 3, 1))
