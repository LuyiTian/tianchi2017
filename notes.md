## 代码说明

* miscellany.py 一些辅助性的代码片段
* cross_validation.py cross_validation框架

在使用cross_validation之前，请在config中加入一个DATA_PATH路径，这个路径下应该包括所user_pay.txt等数据文件。

然后运行miscellany.py中的aggregate_sales_by_shop_day函数，生成按商家和日期的支付聚合数据。

然后就可以使用cross validation了。

示例如下，首先引入类

```
from corss_validation import validator
```

然后新建一个对象，fold是轮数，test_size是留出的最终测试集比例

```
cv = validator(fold=10, test_size=0.1, verbose=True)
```

然后开始循环生成训练和验证集，其中train_date和test_date都是日期列表，类似于［'2016-01-02', '2016-02-02'］这种，然后模型用训练集中指定的日期来训练，训练完了之后用测试集数据来测试，cv.submit接受的参数是一个以日期为键的字典，类似这个样子：

```
{
    ‘2016-01-02’ : [10, 10, 10, ..., 10],
    '2016-02-02' : [20, 20, 20, ..., 20],
}
```

其中值必须是一个2000个元素的列表，其中第i个元素代表shop id为i的商店在这一天的支付数量。

```
for train_date, test_date in cv.split():
    model = model_under_test(train_date)
    cv.submit(model.fit(test_date))
```

最后可以输出平均得分，根据比赛的记分规则，这个值越低越好

```
print cv.result
```

调完了参数之后可以使用最终测试集了：

```
test_date = cv.final_test()
cv.submit(model.fit(test_date))
print cv.result
```