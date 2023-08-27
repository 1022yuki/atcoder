N, D = map(int, input().split())

S = []
for i in range(N):
    s = input()
    S.append(s)

ans = 0
cnt = 0
for j in range(D):
    flag = True
    for i in range(N):
        if S[i][j] == 'x':
            flag = False
    if flag:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0

print(ans)