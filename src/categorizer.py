import pandas
from pandas import DataFrame


def categorize_by_devices(path):
    transactions = pandas.read_csv(path)
    print(type(transactions))
    iPhones = DataFrame()
    iPad = DataFrame()
    new_tran = transactions.groupby('Device')
    df = pandas.DataFrame([[1, 2], [3, 4]], columns=list('AB'))

    df2 = pandas.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
    df.append(df2)
    for i in range(len(transactions.index)+1):
        if transactions.iloc[i]['Device'] == 'iPhone':
            iPhones.append(transactions.iloc[i])
        else:
            iPad.append(transactions.iloc[i])

    return iPhones, iPad

def categorize_by_countries():
    transactions = pandas.read_csv('../src/data_analytics.csv')
    transactions['Country Date'] = transactions['Event Date'].astype('datetime64')
    # grouping data by users: finding out amount of their subscriptions and registration dates
    grouped = transactions.groupby('Subscriber ID')
    # aggregating transcations in a table with columns for ID, number of subscriptions for every customer, and registation date, making it easier to later calculate total amounts
    aggregated = grouped.agg({'Event Date': ['count', 'max']})['Event Date'].rename(
        columns={"max": "registration", "count": "subscriptions"})

