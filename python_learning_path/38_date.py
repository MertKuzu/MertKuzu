# import datetime

from datetime import datetime
from datetime import date
from datetime import time

simdi = datetime.now()
result= simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour

result = datetime.ctime(simdi)
result = datetime.strftime(simdi, '%Y %B')

t = '15 April 2019 hour 09:35:40'
result= datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1983,5,9,12,10,30)

result = datetime.timestamp(birthday)  #saniye
result = datetime.fromtimestamp(result)    #saniyeden tarihe
print(result)