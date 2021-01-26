import pandas as pd
import numpy as np


class CustomerLifetimeValue:
    def __init__(self, data_analysis_path):
        self.transactions = pd.read_csv(data_analysis_path)
        self.transactions['Event Date'] = self.transactions['Event Date'].astype('datetime64')
        # grouping data by users: finding out amount of their subscriptions and registration dates
        grouped = self.transactions.groupby('Subscriber ID')
        # aggregating transcations in a table with columns for ID, number of subscriptions for every customer, and registation date, making it easier to later calculate total amounts
        self.aggregated = grouped.agg({'Event Date': ['count', 'max']})['Event Date'].rename(
            columns={"max": "registration", "count": "subscriptions"})

    # conversion in the meaning of what percentage of those who bought x subscriptions also bought the (x+1) one
    def compute_conversion_percents(self):
        statTable = self.help_compute_user_retention()
        # calculating conversion rates
        Client_amounts = statTable[
            'registration']  # third column: amount of people who bought exactly x subscriptions(x from 0 to 5)
        Conversion_percents = [1.] + list(np.array(Client_amounts[1:]) / np.array(Client_amounts[:-1]))
        return Conversion_percents

    def compute_ltv_from_conversions(self, conversion_rates_without_trial):
        convs = conversion_rates_without_trial
        dev_proceeds = 9.99 * 0.7  # including deduction of subscription cost of 30% by Apple
        # calculating LTV using the formula given in the task
        values = [dev_proceeds]
        for _ in range(len(convs)):
            values.append(values[-1] * convs[_])
        ltv = sum(values[1:])
        print("\nLTV = ", ltv)
        return ltv  # paid_weeks*dev_proceeds/len(self.statTable)

    def compute_lifetime_value(self):
        return self.compute_ltv_from_conversions(self.compute_conversion_percents()[1:])  # paid_weeks*dev_proceeds/len(self.statTable)


    def get_number_of_users(self, parm):
        print(self.aggregated.count())
        return len(self.aggregated)

    # As all users in dataset have complete lifetimes, we can count conversions using all records on each step
    def __count_how_much_users_having_specific_amount_of_subcriptions(self):
        # statTable = aggregated.groupby('subscriptions').count().reset_index()
        statTable = self.aggregated.groupby(by="subscriptions").count().reset_index()
        statTable = statTable.sort_values('subscriptions', ascending=False)
        return statTable

    def help_compute_user_retention(self):
        statTable = self.__count_how_much_users_having_specific_amount_of_subcriptions()
        # counting the statistics Table - what amount of users have at least a specific amount(x) of subscriptions
        statTable['registration'] = np.cumsum(statTable['registration'])
        return statTable.sort_values('subscriptions')

    def compute_retention(self):
        user_retention = self.help_compute_user_retention()
        return self.extract_active_users(user_retention['subscriptions'], user_retention['registration'])#self.aggregated #[1, 0, 1, 1, 1, 1]

    def compute_active_users_for_each_week(self):
        self.transactions['Event Date'] = self.transactions['Event Date'].astype('datetime64')
        # grouping data by users: finding out amount of their subscriptions and registration dates
        grouped = self.transactions.groupby('Subscriber ID')
        return self.aggregated

    def extract_active_users(self, using_period_in_weeks, users_for_given_week):
        users = []
        three_weeks = 0

        if len(using_period_in_weeks) != len(users_for_given_week):
            raise ValueError

        for i in range(1, using_period_in_weeks[len(using_period_in_weeks)-1] + 1):
            if i > using_period_in_weeks[three_weeks]:
                three_weeks += 1

            users.append(users_for_given_week[three_weeks])
        return users

    def compute_relative_user_conversion_rate_or_raise_error(self, user_retentions):
        if (all(user_retentions[i] <= user_retentions[i + 1] for i in range(len(user_retentions) - 1))):
            raise ValueError("Number of users who paid at least ${A money} cannot be greater than number of users who paid ${A money} + ${B money} because one is subset of the other. str(broken_user_retentions): "+str(user_retentions))
        return list(np.array(user_retentions[1:])/np.array(user_retentions[:-1]))

    def compute_lifetime_value_using_numbers_of_user_retention(self, at_least_subscription, user_retention):
        convs = self.compute_relative_user_conversion_rate_or_raise_error(self.extract_active_users(at_least_subscription, user_retention))
        dev_proceeds = 9.99 * 0.7  # including deduction of subscription cost of 30% by Apple
        # calculating LTV using the formula given in the task
        values = [dev_proceeds]
        for _ in range(len(convs)):
            values.append(values[-1] * convs[_])
        ltv = sum(values[1:])
        return ltv