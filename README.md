# tianchi2017
tianchi2017: 口碑商家客流量预测.

> team keypass: hdrzwf

# TODO

* update cv method
* convert all to pinyin
* get holiday data
* build a benchmark model (toy model)

## cv requirements
* randomly select a timepoint. get data from x days before this timepoint as training data and y days after this timepoint as testing data.
* deal with null value for some shop
* calculate score based on prediction results

## holiday and weekend data
* two columns csv file. first is date and second is whether it is holiday or weekend.


## 数据描述：

https://tianchi.shuju.aliyun.com/competition/information.htm?spm=5176.100067.5678.2.7j7Plk&raceId=231591

### 扩展数据

* 增加天气数据，目前还是分类型变量，根据后续建模需求看是否要加入温度。
* ...

## 论坛问题总结：

* user pay 是只要用户使用了支付宝在商家支付了就算是，view是要点口碑进去查看该商家才算，所以view比pay要少.

## 文件夹结构：
- config.py: data file path, constant variables with full capital name
- /play_data: store random code or code that in dev



