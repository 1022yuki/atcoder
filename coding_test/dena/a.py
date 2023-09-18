from collections import deque
from collections import defaultdict

step = int(input())

if step==1:
    M = int(input())
    dish_dic = defaultdict(int)
    for i in range(M):
      d, s, p = map(int, input().split())
      dish_dic[d]=([s, p])

    try:
        while True:
            # 入力を受け取る
            inp =  list(map(str, input().split()))
            if inp[0] == 'order':
                t = int(inp[1])
                d = int(inp[2])
                n = int(inp[3])
                if dish_dic[d][0]<n:
                    print('sold out '+str(t))
                else:
                    dish_dic[d][0]-=n
                    for i in range(n):
                        print('received order '+str(t)+' '+str(d))

    except EOFError:
        pass

if step==2:
    M, K = map(int, input().split())
    dish_dic = defaultdict(int)
    for i in range(M):
      d, s, p = map(int, input().split())
      dish_dic[d]=([s, p])

    # 現在調理中の料理
    cooking = []

    # 待ち料理リスト
    queue_wait = deque()
    
    try:
        while True:
            # 入力を受け取る
            inp =  list(map(str, input().split()))
            if inp[0] == 'received':
                # 席番号
                t = int(inp[2])
                # 料理番号
                d = int(inp[3])

                if len(cooking)<K:
                    cooking.append(d)
                    print(str(d))
                else:
                    queue_wait.append(d)
                    print('wait')


            if inp[0] == 'complete':
                # 料理番号
                d = int(inp[1])

                if not d in cooking:
                    print('unexpected input')
                else:
                    if len(queue_wait)==0:
                        cooking.remove(d)
                        print('ok')
                    else:
                        cooking.remove(d)
                        st_cook = queue_wait.popleft()
                        cooking.append(st_cook)
                        print('ok '+str(st_cook))
    
    except EOFError:
        pass

if step==3:
    M = int(input())
    dish_dic = defaultdict(int)
    for i in range(M):
      d, s, p = map(int, input().split())
      dish_dic[d]=([s, p])
    
    dish_table_dic = defaultdict(int)
    
    try:
        while True:
            # 入力を受け取る
            inp =  list(map(str, input().split()))
            if inp[0] == 'received':
                # 席番号
                t = int(inp[2])
                # 料理番号
                d = int(inp[3])

                if dish_table_dic[d]==0:
                    dish_table_dic[d] = deque()
                dish_table_dic[d].append(t)

            if inp[0] == 'complete':
                # 料理番号
                d = int(inp[1])

                table = dish_table_dic[d].popleft()
                print('ready '+str(table)+' ' +str(d))

    except EOFError:
        pass

if step==4:
    M = int(input())
    dish_dic = defaultdict(int)
    for i in range(M):
      d, s, p = map(int, input().split())
      dish_dic[d]=([s, p])
    
    table_amount_dic = defaultdict(int)
    table_num_waiting_dic = defaultdict(int)
    
    try:
        while True:
            # 入力を受け取る
            inp =  list(map(str, input().split()))
            if inp[0] == 'received':
                # 席番号
                t = int(inp[2])
                # 料理番号
                d = int(inp[3])

                table_num_waiting_dic[t]+=1

            if inp[0] == 'ready':
                # 席番号
                t = int(inp[1])
                # 料理番号
                d = int(inp[2])

                table_num_waiting_dic[t]-=1
                table_amount_dic[t]+=dish_dic[d][1]


            if inp[0] == 'check':
                # 席番号
                t = int(inp[1])

                if table_num_waiting_dic[t]==0:
                    print(table_amount_dic[t])
                    table_amount_dic[t]=0
                else:
                    print('please wait')

    except EOFError:
        pass