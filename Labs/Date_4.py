from datetime import datetime, time

date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()

timedelta = date2 - date1
a = timedelta.days * 24 * 3600 + timedelta.seconds

print(a)