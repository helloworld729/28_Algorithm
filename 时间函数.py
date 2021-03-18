from datetime import datetime

# 输出星期几
myData = datetime(2021, 2, 6)
weekday = datetime.weekday(myData)
daystr  = datetime.strftime(myData, "%A")
print(weekday)
print(daystr)

# 5
# Saturday
# Sat(格式为a%)

days = datetime.strftime(myData, "%c")
print(days)

# 但是要修改时区才对

