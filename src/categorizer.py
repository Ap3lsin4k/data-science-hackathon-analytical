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
