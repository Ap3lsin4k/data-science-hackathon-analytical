import pandas as pd
import numpy as np

class CustomerLifetimeValue:


    def __init__(self):
        pass

    def compute_lifetime_value(self, param):
        # importing data
        self.statTable = None
        inp = pd.read_csv(param)
        inp['Event Date'] = inp['Event Date'].astype('datetime64')

        # grouping data by users: finding out amount of their subscriptions and registration dates
        grouped = inp.groupby('Subscriber ID')
        #print(grouped)
        # aggregating transcations in a table with columns for ID, number of subscriptions for every customer, and registation date, making it easier to later calculate total amounts
        self.aggregated = grouped.agg({'Event Date': ['count', 'max']})['Event Date'].rename(
            columns={"max": "registration", "count": "subscriptions"})
        #print(self.aggregated)
        self.__count_how_much_users_having_specific_amount_of_subcriptions()

        # # counting the statistics Table - what amount of users have at least a specific amount(x) of subscriptions
        self.statTable['registration'] = np.cumsum(self.statTable['registration'])
        self.statTable = self.statTable.sort_values('subscriptions')
        # calculating conversion rates
        # 1.0
        Client_amounts = self.statTable['registration'] # third column: amount of people who bought exactly x subscriptions(x from 0 to 5)
        print(Client_amounts)
        self.Conversion_percents = [1.] + list(np.array(Client_amounts[1:]) / np.array(Client_amounts[:-1]))
        # # conversion in the meaning of what percentage of those who bought x subscriptions also bought the (x+1) one
        # convs = np.array(self.Conversion_percents[1:])
        dev_proceeds = 9.99 * 0.7  # including deduction of subscription cost of 30% by Apple
        # # calculating LTV using the formula given in the task
        paid_weeks = 0
        for i in self.statTable['subscriptions']:
            paid_weeks += (i-1)
        return paid_weeks*dev_proceeds/len(self.statTable)
       # ltv = statTable['subscriptions']  # sum(values[1:])
      #  first_client = 0
      #  print("\nLTV = ", ltv[first_client])
      #  trial = 1
       # return (ltv[first_client] - trial) * dev_proceeds  # 34.965

    def get_number_of_users(self, parm):
        print(self.aggregated.count())
        return len(self.aggregated)

    # As all users in dataset have complete lifetimes, we can count conversions using all records on each step
    def __count_how_much_users_having_specific_amount_of_subcriptions(self):
        self.statTable = self.aggregated.groupby('subscriptions').count().reset_index()
        print(self.statTable)
        self.statTable = self.statTable.sort_values('subscriptions', ascending=False)
        print(self.statTable['subscriptions'][0] -1)
