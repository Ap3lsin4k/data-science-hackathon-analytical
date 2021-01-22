import pandas as pd
import numpy as np

class CustomerLifetimeValue:


    def __init__(self):
        # importing data
        self.statTable = None
        inp = pd.read_csv("model/LTV=USD34.96.csv")
        inp['Event Date'] = inp['Event Date'].astype('datetime64')

        # grouping data by users: finding out amount of their subscriptions and registration dates
        grouped = inp.groupby('Subscriber ID')
        # aggregating transcations in a table with columns for ID, number of subscriptions for every customer, and registation date, making it easier to later calculate total amounts
        self.aggregated = grouped.agg({'Event Date': ['count', 'max']})['Event Date'].rename(
            columns={"max": "registration", "count": "subscriptions"})
       # print(self.aggregated)

    def compute_lifetime_value(self, param):
        self.__count_how_much_users_having_specific_amount_of_subcriptions()
        print(self.statTable['subscriptions'])
        dev_proceeds = 9.99 * 0.7  # including deduction of subscription cost of 30% by Apple
        ltv = self.statTable['subscriptions']#sum(values[1:])
        first_client = 0
        print("\nLTV = ", ltv[first_client])
        trial = 1
        return (ltv[first_client] - trial)*dev_proceeds #34.965

    def get_number_of_users(self, parm):
        print(self.aggregated.count())
        return len(self.aggregated)

    # As all users in dataset have complete lifetimes, we can count conversions using all records on each step
    def __count_how_much_users_having_specific_amount_of_subcriptions(self):
        self.statTable = self.aggregated.groupby('subscriptions').count().reset_index()
        print(self.statTable)
        self.statTable = self.statTable.sort_values('subscriptions', ascending=False)
