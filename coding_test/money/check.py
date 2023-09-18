import datetime
import re

a = input()
print(a)

def check_time(time: str):
    match = re.search(r"(\d{2}):(\d{2}):\d{2}\.\d{3}",time)
    hour = int(match.group(1))
    min = int(match.group(2))
    if 0<=hour%24 and hour%24<=5:
        return 1
    elif 6<=hour%24 and hour%24<=9 and min<30:
        return 2
    elif 20<=hour%24 and hour%24<=23:
        return 2
    else:
        return 0

print(check_time(a))