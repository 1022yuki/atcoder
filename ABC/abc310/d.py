import sys
sys.setrecursionlimit(10**9)

N, T, M = map(int, input().split())

bad = []
for i in range(N):
    bad.append([False]*N)

for i in range(M):
    a, b = map(int, input().split())
    a-=1
    b-=1
    bad[a][b] = True
    bad[b][a] = True

# print(bad)

teams = []
for i in range(T):
    teams.append([])

def dfs(num, teams):
    global cnt
    # print(teams)
    if num==N:
        # print(teams)
        empty_flag = True
        for t in range(T):
            if len(teams[t])==0:
                empty_flag = False
        bad_flag = True
        for t in range(T):
            tt = teams[t]
            lg_t = len(tt)
            if lg_t<2:
                continue
            for i in range(lg_t):
                for j in range(i+1, lg_t):
                    p1 = tt[i]
                    p2 = tt[j]
                    if bad[p1][p2]:
                        bad_flag=False
                        # print(i, j, t, teams)
        if empty_flag and bad_flag:
            cnt+=1
            # print(teams)
        
    else:           
        for t in range(T):
            teams[t].append(num)
            dfs(num+1, teams)
            teams[t].pop()
            if len(teams[t])==0:
                break

cnt = 0
dfs(0, teams)
print(cnt)