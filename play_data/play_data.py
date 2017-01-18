import numpy as np
from collections import Counter
import pylab as pl
def get_day_pay_freq(pay_file):
    cnt = Counter()
    for line in open(pay_file):
        items = line.split(',')
        cnt[(int(items[1]), items[2].split()[0])] += 1
    return cnt.values()


if __name__ == '__main__':
    freq = get_day_pay_freq("/Users/luyi/data/tianchi2017/dataset/user_pay.txt")
    pl.hist([np.log(i) for i in freq],  bins=100)
    pl.title("distribution of daily customer flow (log).")
    pl.show()
