# week13_01.py
# 202444071
# 전태현

import datetime
from datetime import datetime as dt

# module.class.method()
d1 = datetime.datetime.now()
print(type(d1), d1)

# class.method()
d2 = dt.now()
print(type(d2), d2)

print(d2.year)
print(d2.month)
print(d2.day)
print(d2.hour)
print(d2.minute)
print(d2.second)
print(d2.microsecond)

print('-' *20)

print(d2.weekday())
print(d2.date(), type(d2.date()))
print(d2.time(), type(d2.time()))
