 

holiday = data.frame(date=seq(as.Date("2015-07-01"), as.Date("2016-10-31"), by="days"))

holiday$is_holiday = 0

#国庆
holiday[holiday$date > "2015-09-26" & holiday$date < "2015-10-8", "is_holiday"] = 1
#元旦
holiday[holiday$date > "2015-12-31" & holiday$date < "2016-01-04", "is_holiday"] = 1
#春节
holiday[holiday$date > "2016-02-03" & holiday$date < "2016-02-16", "is_holiday"] = 1
#清明
holiday[holiday$date > "2016-04-03" & holiday$date < "2016-04-07", "is_holiday"] = 1
#端午
holiday[holiday$date > "2016-06-08" & holiday$date < "2016-06-12", "is_holiday"] = 1
#中秋
holiday[holiday$date > "2016-09-14" & holiday$date < "2016-09-18", "is_holiday"] = 1
#国庆
holiday[holiday$date > "2016-09-30" & holiday$date < "2016-10-08", "is_holiday"] = 1


write.csv(holiday, file="holidays.csv", row.names = FALSE,quote = FALSE)
