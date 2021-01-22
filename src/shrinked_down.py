import pandas as pd
import numpy as np

# importing data
inp = pd.read_csv("data_analytics.csv")
inp['Event Date'] = inp['Event Date'].astype('datetime64')

# grouping data by users: finding out amount of their subscriptions and registration dates
grouped = inp.groupby('Subscriber ID')
# aggregating transcations in a table with columns for ID, number of subscriptions for every customer, and registation date, making it easier to later calculate total amounts
aggregated = grouped.agg({'Event Date': ['count', 'max']})['Event Date'].rename(
    columns={"max": "registration", "count": "subscriptions"})
print("Aggregated", aggregated)

aggregated.to_csv("new_dataanalytics.csv", index=True)
# As all users in dataset have complete lifetimes, we can count conversions using all records on each step

def count_how_much_users_having_specific_amount_of_subcriptions():
    statTable = aggregated.groupby('subscriptions').count().reset_index()
    print(statTable)

count_how_much_users_having_specific_amount_of_subcriptions()
