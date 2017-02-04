## baseline functions

import pandas as pd
import numpy as np


def mean_predict(sales,
                 predit_days=14,
                 use_days=7):
    use_sales = sales.ix[-use_days:]
    sales_mean = use_sales.mean(axis=0).values
    data = np.ones((predit_days, len(use_sales.columns)))*sales_mean
    date_list = [i for i in pd.date_range(sales.ix[-1:].index[0], periods=predit_days+1)][1:]
    future = pd.DataFrame(data=data, index=date_list, columns=sales.columns)
    return future


def season_predict(sales,
                   predit_days=14,
                   use_freq=7,
                   use_period=3):
    sales_val = sales.values
    data = np.zeros((predit_days, len(sales.columns)))
    comb_val = np.vstack((sales_val, data))
    for i in range(predit_days):
        comb_val[(i-predit_days), :] = np.mean(np.array([comb_val[-(i-use_freq*t-predit_days), :] for t in range(1, use_period+1)]), axis=0)
    date_list = [i for i in pd.date_range(sales.ix[-1:].index[0], periods=predit_days+1)][1:]
    future = pd.DataFrame(data=comb_val[-predit_days:, ], index=date_list, columns=sales.columns)
    return future


if __name__ == '__main__':
    from utils import get_time_period, get_all_score
    sales = get_time_period(start="2016-03-01", end="2016-10-31")
    #sales = sales.ix[:, 0:5]
    predit_days = 14
    sales_train = sales.ix[:-predit_days]
    sales_test = sales.ix[-predit_days:]
    from timeit import default_timer as timer

    start = timer()
    res = mean_predict(sales_train, predit_days)
    end = timer()
    print "mean ## time used:", end - start, "## score:", get_all_score(res, sales_test, log2=True)

    start = timer()
    res = season_predict(sales_train, predit_days)
    end = timer()
    print "week ## time used:", end - start, "## score:", get_all_score(res, sales_test, log2=True)

    start = timer()
    res1 = season_predict(sales_train, predit_days)
    res2 = mean_predict(sales_train, predit_days)
    res = (res1+res2)/2
    end = timer()
    print "mean+season ## time used:", end - start, "## score:", get_all_score(res, sales_test, log2=True)
