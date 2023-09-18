from datetime import datetime
import re

dist_meter = 0
low_speed_time_meter = 0
fare_meter =0

def check_time(time: str):
    match = re.search(r"(\d{2}):(\d{2}):\d{2}\.\d{3}",time)
    hour = int(match.group(1))
    min = int(match.group(2))
    if 0<=hour%24 and hour%24<=5:
        return "1"
    elif 6<=hour%24 and hour%24<=9 and min<30:
        return "2"
    elif 20<=hour%24 and hour%24<=23:
        return "2"
    else:
        return "0"

def time_diff(time1, time2):
    # 分以下を取り出す
    # 時間の部分は24を超えるとエラーになる
    # 時間の部分は差だけ使う
    h1 = int(re.sub(":.*", "", time1))
    h2 = int(re.sub(":.*", "", time2))
    time1 = time1[3:]
    time2 = time2[3:]
    time1 = datetime.strptime(time1, '%M:%S.%f')
    time2 = datetime.strptime(time2, '%M:%S.%f')
    return (time2-time1).total_seconds()+(h2-h1)*3600


# 1行目の入力を受け取る
inp =  list(map(str, input().split()))
time = inp[0]
if check_time(time)=="0":
    fare_meter +=400
if check_time(time)=="1":
    fare_meter +=600
if check_time(time)=="2":
    fare_meter +=520

time_pre = time

try:
    while True:
        # print('運賃')
        # print(fare_meter)
        # 2行目以降の入力を受け取る
        inp =  list(map(str, input().split()))
        time = inp[0]
        dist = float(inp[1])

        # 低速走行時間メーターの更新
        # print(time_pre, time)
        # print(dist_meter)
        dif_time = time_diff(time_pre, time)
        ave_v = dist/dif_time
        # print(ave_v)
        low_speed_time_pre = low_speed_time_meter//45
        if ave_v<=10:
            low_speed_time_meter += dif_time
            low_speed_time_suf = low_speed_time_meter//45
            # 45秒の区間を跨いだとき、その時の時刻に応じて運賃メーターを更新
            if low_speed_time_suf!=low_speed_time_pre:
                # print('aaaaaaaaaaaaaaaaaaa')
                if check_time(time)=="0":
                    # 通常
                    fare_meter +=40
                if check_time(time)=="1":
                    # 深夜
                    fare_meter +=60
                if check_time(time)=="2":
                    # 通勤
                    fare_meter +=52             


        # 距離メーターの更新
        dist_meter_pre = dist_meter
        dist_meter += dist
        dist_meter_suf = dist_meter

        if dist_meter_pre<1000 and 1000<=dist_meter_suf:
            # print('bbbbbbbbbbbbb')
            if check_time(time)=="0":
                # 通常
                fare_meter +=40
            if check_time(time)=="1":
                # 深夜
                fare_meter +=60
            if check_time(time)=="2":
                # 通勤
                fare_meter +=52     
        if dist_meter_pre>1000 and (dist_meter_pre-1000)//400!=(dist_meter_suf-1000)//400:
            # print('cccccccccccc')
            if check_time(time)=="0":
                # 通常
                fare_meter +=40
            if check_time(time)=="1":
                # 深夜
                fare_meter +=60
            if check_time(time)=="2":
                # 通勤
                fare_meter +=52
        if dist_meter_pre>10200 and (dist_meter_pre-10200)//350!=(dist_meter_suf-10200)//350:
            # print('ddddddddddddddddd')
            if check_time(time)=="0":
                # 通常
                fare_meter +=40
            if check_time(time)=="1":
                # 深夜
                fare_meter += 60
            if check_time(time)=="2":
                # 通勤
                fare_meter +=52

        # 前回の時刻を更新
        time_pre = time

        print(fare_meter)

except EOFError:
    print(fare_meter)
    pass