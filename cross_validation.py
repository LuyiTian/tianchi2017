"""A Cross validation framework."""

from __future__ import division

from miscellany import data_path
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

import pandas as pd
import numpy as np


class validator(object):
    """Cross validation class.

        Usage:

        from corss_validation import validator

        cv = validator()
        for train_date, test_date in cv.split():
            model = model_under_test(train_date)
            cv.submit(model.fit(test_date))
        print cv.result
    """

    def __init__(self, fold=10, test_size=0.1, verbose=True):
        """Set the fold number."""
        self.fold = fold
        self.verbose = verbose

        # Load true sales
        sales = pd.read_csv(data_path('sales_by_day.csv'))
        # Fill NaN with zero
        sales.fillna(0, inplace=True)
        # Set index to shop_id
        sales = sales.set_index('shop_id')
        # Get the set of date
        dates = sales.columns
        # Retain part of data for test
        train_set, test_set, _, _ = train_test_split(
            sales.columns, sales.columns, test_size=test_size, random_state=0)
        self.sales = sales
        self.train_set = train_set
        self.test_set = test_set

    def split(self):
        """Split train set into K folders."""
        kf = KFold(n_splits=self.fold, shuffle=True)
        self.step = 0
        self.score = []
        for train, test in kf.split(self.train_set):
            self.step += 1
            self.testing = self.train_set[test]
            yield self.train_set[train], self.train_set[test]

    def __get_score(self, predicted, actual):
        """Calculate the score."""
        for shop in range(self.sales.shape[0]):
            if predicted[shop] == 0 and actual[shop] == 0:
                return 0
            else:
                return abs((predicted[shop] - actual[shop]) /
                           (predicted[shop] + actual[shop]))

    def submit(self, result):
        """Collect test result. Results should be a dictionry which has keys 
        refer to date and values refers to sales of different shops.

        For example, a valid result looks like this:

        {
            '2016-01-01' : [10, 10, 10, 10, ..., 10],
            '2016-01-05' : [20, 20, 20, 20, ..., 20],
        }
        """

        # Check input
        for date in self.testing:
            if date not in result.keys():
                raise Exception('Missing date %s' % date)
            if len(result[date]) != self.sales.shape[0]:
                raise Exception('Missing %d shop on date %s' %
                                (self.sales.shape[0] - len(result[date]), date))

        score = 0
        for date, predicted in result.iteritems():
            actual = self.sales[str(date)].tolist()
            score += self.__get_score(predicted, actual)

        score /= len(self.testing) * self.sales.shape[0]
        self.score.append(score)
        if self.verbose:
            print('Fold %s : %s' % (str(self.step), score))

    def result(self):
        """Get the average score of cross validation."""
        return sum(self.score) / len(self.score)

    def final_test(self):
        self.score = []
        self.step = 'final test'
        self.testing = self.test_set
        return self.test_set
