from LTV_calc import CustomerLifetimeValue


def test_retention_for_one_user():
    ltv = CustomerLifetimeValue("model/LTV=USD34.96.csv")
    res = ltv.compute_retention()
    assert len(res) == 6
    assert res[0] == 1


def test_retention_for_two_users():
    ltv = CustomerLifetimeValue("model/two_users.csv")
    res = ltv.compute_retention()
    assert res == [2, 2, 2, 2, 1, 1]
    assert len(res) == 6
    assert res[0] == 2



