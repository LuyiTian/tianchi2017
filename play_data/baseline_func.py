## baseline functions

import pandas as pd
import numpy as np
from utils import get_time_period, get_all_score
from random import randint


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


def generate_ran_train_test(dataset_num=10000, perc=0.8, use_days=28, pred_days=14):
    sales = get_time_period(start="2016-03-01", end="2016-10-31", fillna="pad")
    data = sales.values
    X = np.zeros((dataset_num, use_days))
    Y = np.zeros((dataset_num, pred_days))
    r_r = (use_days+1, data.shape[0]-pred_days-1)
    c_r = (0, data.shape[1]-1)
    for i in range(dataset_num):
        r = randint(r_r[0], r_r[1])
        c = randint(c_r[0], c_r[1])
        X[i] = data[(r-use_days):r, c]
        Y[i] = data[r:(r+pred_days), c]
    if perc == 1.:
        return X, Y, None, None
    elif perc <= 0.5:
        print "perc should be larger than 0.5"
    else:
        train_label = np.random.choice(Y.shape[0], int(Y.shape[0]*perc))
        test_label = np.array([i for i in range(Y.shape[0]) if i not in train_label])

        train_X = X[train_label, :]
        train_Y = Y[train_label, :]
        test_X = X[test_label, :]
        test_Y = Y[test_label, :]
        return train_X, train_Y, test_X, test_Y


if __name__ == '__main__':
    """
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
    """
    sales = get_time_period(start="2016-10-14", end="2016-10-31", fillna="median")
    res = mean_predict(sales, use_days=14)
    print res
    f_out = open("mean_predict.csv", "w")
    for i in range(2000):
        f_out.write("{},".format(i+1)+",".join([str(int(2**it)) for it in res.values[:, i]])+"\n")
