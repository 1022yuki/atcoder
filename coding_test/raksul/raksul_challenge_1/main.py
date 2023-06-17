from collections import defaultdict
import datetime

can_enter_dict = defaultdict(int)
already_enter_dict = defaultdict(int)

step = int(input())

if step == 1:
    n = int(input())
    # 開始時点で有効な社員番号
    for i in range(n):
        inp = input()
        can_enter_dict[inp] = 1

    try:
        while True:
            # 入力を受け取る
            inp =  list(map(str, input().split()))

            if inp[0] == 'enter':
                date = inp[1]
                time = inp[2]
                id = inp[3]
                if can_enter_dict[id] == 1:
                    print('can')
                else:
                    print('cannot')
            
            if inp[0] == 'issue':
                id = inp[1]
                can_enter_dict[id] = 1
            
            if inp[0] == 'disable':
                id = inp[1]
                can_enter_dict[id] = 0

    except EOFError:
        pass

if step == 2:
    last_time = -1
    try:
        while True:
            # 入力を受け取る
            inp =  list(map(str, input().split()))

            if inp[0] == 'enter':
                date_time = datetime.datetime.strptime(inp[1]+' '+inp[2], '%Y/%m/%d %H:%M:%S')
                id = inp[3]
                last_time = date_time
                if can_enter_dict[id] == 0:
                    print('unissued id')
                elif can_enter_dict[id] == -1:
                    print('disabled id')
                elif date_time<can_enter_dict[id][0] or can_enter_dict[id][1]<date_time:
                    print('not applicable now')
                else:
                    already_enter_dict[id] = 1
                    print('can')
                    
            if inp[0] == 'issue':
                id = inp[1]
                date_time_1 = datetime.datetime.strptime(inp[2]+' '+inp[3], '%Y/%m/%d %H:%M:%S')
                date_time_2 = datetime.datetime.strptime(inp[4]+' '+inp[5], '%Y/%m/%d %H:%M:%S')
                if last_time==-1 or last_time <= date_time_2:
                    if date_time_1 <= date_time_2:
                        can_enter_dict[id] = [date_time_1, date_time_2]
                        print('successfully issued')
                    else:
                        print('invalid info')
                else:
                    print('invalid info')
            
            if inp[0] == 'update':
                id = inp[1]
                date_time_1 = datetime.datetime.strptime(inp[2]+' '+inp[3], '%Y/%m/%d %H:%M:%S')
                date_time_2 = datetime.datetime.strptime(inp[4]+' '+inp[5], '%Y/%m/%d %H:%M:%S')
                if last_time==-1 or last_time <= date_time_2:
                    if date_time_1 <= date_time_2:
                        if already_enter_dict[id] == 1:
                            print('already used')
                        else:
                            can_enter_dict[id] = [date_time_1, date_time_2]
                            print('successfully updated')
                    else:
                        print('invalid info')
                else:
                    print('invalid info')


            if inp[0] == 'disable':
                id = inp[1]
                if already_enter_dict[id] == 1:
                    print('already used')
                else:
                    can_enter_dict[id] = -1
                    print('successfully disabled')

    except EOFError:
        pass