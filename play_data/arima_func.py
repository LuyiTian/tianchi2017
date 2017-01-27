# arima things
import statsmodels.api as sm
import numpy as np
import pandas as pd


def __gen_para():
    """
    generate parameters for SARIMAX model
    """
    for p in range(1, 15):
        for q in range(1, 15):
            for P in range(1, 15):
                for Q in range(1, 15):
                    yield p, q, P, Q


def SARIMAX_predict_one(sales_ashop,
                        predit_days,
                        verbose=True):
    """
    @param sales_ashop sales data for a shop
    """
    num_tried = 0
    for p, q, P, Q in __gen_para():
        try:
            mod = sm.tsa.statespace.SARIMAX(sales_ashop, trend=[1, 1], order=(p, 1, q), seasonal_order=(P, 1, Q, 7))
            results = mod.fit()
            break
        except:
            num_tried += 1
    if verbose:
        print "SARIMAX finished with parameters:", p, q, P, Q
        print results.summary()
    date_list = [i for i in pd.date_range(sales_ashop.ix[-1:].index[0], periods=predit_days+1)][1:]
    future = pd.DataFrame(index=date_list, columns=sales_ashop.columns)
    sales_ashop = pd.concat([sales_ashop, future])
    pred_da = results.predict(start=date_list[0], end=date_list[-1], dynamic=True)
    return pred_da


def SARIMAX_predict(sales,
                    predit_days=14,
                    verbose=True):
    """
    doc
    """
    result = pd.concat([SARIMAX_predict_one(sales[[ith]], predit_days, verbose) for ith in range(len(sales.columns))], axis=1)
    result.columns = sales.columns
    return result


if __name__ == '__main__':
    from utils import get_time_period, get_all_score
    sales = get_time_period(start="2016-03-01", end="2016-10-31")
    sales = sales.ix[:, 0:5]
    predit_days = 14
    sales_train = sales.ix[:-predit_days]
    sales_test = sales.ix[-predit_days:]
    res = SARIMAX_predict(sales_train, predit_days)
    print get_all_score(res, sales_test)

