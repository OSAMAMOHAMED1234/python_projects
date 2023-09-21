from datetime import datetime

def time_delta(t1, t2):
  time_format = '%a %d %b %Y %H:%M:%S %z'
  t1 = datetime.strptime(t1, time_format)
  t2 = datetime.strptime(t2, time_format)
  return str(int(abs((t1-t2).total_seconds())))

t1 = 'Sat 02 May 2015 19:54:36 +0530'
t2 = 'Fri 01 May 2015 13:54:36 -0000'
print(time_delta(t1, t2))