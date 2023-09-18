from collections import defaultdict

step = int(input())

if step==1:
    M = int(input())
    dish_dic = defaultdict(int)
    for i in range(M):
      d, s, p = map(int, input().split())
      dish_dic[d].append([s, p])

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
                    dish_dic[d][1]-=n
                    for i in range(n):
                        print('received order '+str(t)+' '+str(d))

    except EOFError:
        pass