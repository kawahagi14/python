# coding: utf-8

import datetime

day = datetime.date(1971,6,23)
day.weekday()

kyou = datetime.date.today()
print(kyou)
print(day.today())

date_a = datetime.date(2008,1,1)
date_b = datetime.date(2009,1,1)
days_2008 = date_b - date_a
print(days_2008)

birthday = datetime.date(1971,6,23)
life = kyou - birthday
print(life.days)