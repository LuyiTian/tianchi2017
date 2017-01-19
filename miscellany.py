"""Miscellaneous classes and functions."""

from __future__ import absolute_import

from config import DATA_PATH
from collections import defaultdict
from datetime import datetime

import os
import pandas as pd


def data_path(filename):
    return os.path.join(DATA_PATH, filename)


def aggregate_sales_by_shop_day():
    # Read data
    user_pay = pd.read_csv(data_path('user_pay.txt'),
                           sep=',', header=None, engine='c')

    # Strip date
    user_pay[2] = pd.to_datetime(user_pay[2].map(lambda x: x[:10]))

    # Name columns
    user_pay.columns = ['user_id', 'shop_id', 'date']

    # Count payment
    count = user_pay.groupby(['shop_id', 'date']).agg('count')

    # Long date to wide data
    count.reset_index(inplace=True)
    count = count.pivot(index='shop_id', columns='date', values='user_id')

    # Output
    count.to_csv(data_path('sales_by_day.csv'))


if __name__ == '__main__':
    aggregate_sales_by_shop_day()
