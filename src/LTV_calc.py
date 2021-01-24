import pandas as pd
import numpy as np
inp = pd.read_csv("data_analytics.csv")
inp['Event Date'] = inp['Event Date'].astype('datetime64')
# grouping data by users: finding out amount of their subscriptions and registration dates
grouped = inp.groupby('Subscriber ID')
# aggregating transcations in a table with columns for ID, number of subscriptions for every customer, and registation date, making it easier to later calculate total amounts
aggregated = grouped.agg({'Event Date': ['count', 'min']})['Event Date'].rename(
            columns={"min": "registration", "count": "subscriptions"})
def count_how_much_users_having_specific_amount_of_subcriptions():
    #statTable = aggregated.groupby('subscriptions').count().reset_index()
    statTable = aggregated.groupby(by="subscriptions").count().reset_index()
    statTable = statTable.sort_values('subscriptions', ascending=False)
    return statTable

statTable = count_how_much_users_having_specific_amount_of_subcriptions()
# counting the statistics Table - what amount of users have at least a specific amount(x) of subscriptions
statTable['registration'] = np.cumsum(statTable['registration'])
statTable = statTable.sort_values('subscriptions')
# calculating conversion rates
Client_amounts = statTable['registration']  # third column: amount of people who bought exactly x subscriptions(x from 0 to 5)
Conversion_percents = [1.] + list(np.array(Client_amounts[1:]) / np.array(Client_amounts[:-1]))
# conversion in the meaning of what percentage of those who bought x subscriptions also bought the (x+1) one
statTable['conversion'] = Conversion_percents
convs = np.array(statTable['conversion'][1:])
dev_proceeds = 9.99 * 0.7  # including deduction of subscription cost of 30% by Apple
# calculating LTV using the formula given in the task
values = [dev_proceeds]
for _ in range(len(convs)):
    values.append(values[-1] * convs[_])
ltv = sum(values[1:])
print("\nLTV = ", ltv)
