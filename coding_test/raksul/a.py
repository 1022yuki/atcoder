from collections import defaultdict

can_enter_dict = defaultdict(int)

step = int(input())
n = int(input())

# 開始時点で有効な社員番号
for i in range(n):
    inp = int(input())
    can_enter_dict[inp] = 1

while True:
    # 入力を受け取る
    inp =  list(map(str, input().split()))

    if inp[0] == 'enter':
        date = inp[1]
        time = inp[2]
        id = int(inp[3])
        if can_enter_dict[id] == 1:
            print('can')
        else:
            print('cannot')
    
    if inp[0] == 'issue':
        id = int(inp[1])
        can_enter_dict[id] = 1
    
    if inp[0] == 'disable':
        id = int(inp[1])
        can_enter_dict[id] = 0