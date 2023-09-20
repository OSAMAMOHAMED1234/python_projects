import re
res = re.search(r'([A-Za-z0-9])\1', input())
print(res)
print(-1) if res is None else print(res.groups()[0])
# m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
# m.group(), m.groups(), m.groupdict()