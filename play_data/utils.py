import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from config import DATA_PATH

import pandas as pd
import numpy as np


def get_time_period(start=None,
                    end="2016-10-31",
                    fillna=None,
                    log2=True):
    """
    get data within a time period from `start` to `end`
    @param start a date string, such as "2016-01-15", if None start from "2015-07-01"
    @param end a date string, such as "2016-10-15"
    @param fillna how to deal with NA, if None then only select shops that has no NA
    in this period
    @param log2 return log2 transformed data
    """
    sales = pd.read_csv(os.path.join(DATA_PATH, 'day_by_sales.csv'))
    sales['date'] = pd.to_datetime(sales.date)
    sales.set_index(keys="date", inplace=True)
    if log2:
        sales = np.log2(sales)
    if start is None:
        start = "2015-07-01"
    sel_sales = sales[start:end]
    if fillna is None:
        sel_sales = sel_sales.dropna(axis=1, how="any")
    else:
        raise NotImplementedError
    return sel_sales


def get_all_score(pred_da, real_da, log2=True):
    """
    """
    if type(pred_da) is not np.ndarray:
        if log2:
            pred = 2**pred_da.values
        else:
            pred = pred_da.values
    else:
        if log2:
            pred = 2**pred_da
        else:
            pred = pred_da
    if type(real_da) is not np.ndarray:
        if log2:
            real = 2**real_da.values
        else:
            real = real_da.values
    else:
        if log2:
            real = 2**real_da
        else:
            real = real_da
    return np.sum(np.abs((pred-real)/(pred+real)))/(pred_da.shape[0]*pred_da.shape[1])


if __name__ == '__main__':
    pass
