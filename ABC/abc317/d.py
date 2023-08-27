N = int(input())

X = []
Y = []
Z = []
for i in range(N):
    x, y, z = map(int, input().split())
    X.append(x)
    Y.append(y)
    Z.append(z)

t = 0
a = 0
for i in range(N):
    x, y, z = X[i], Y[i], Z[i]
    if x>y:
        t += z
    else:
        a += z

if t>a:
    print(0)
    exit()

# print(t, a)
need = ((a-t)//2)+1
# print(need)

cand = []
for i in range(N):
    t, a, z = X[i], Y[i], Z[i]
    if t<a:
        ch = ((a-t)//2)+1
        cand.append([ch, z])

# print(cand)
len_cand = len(cand)
inf = 10**12

dp = []
for i in range(len_cand+1):
    dp.append([inf]*(10**5+1))
dp[0][0] = 0

for i in range(len_cand):
    ch, z = cand[i]
    for j in range(10**5+1):
        if dp[i][j]!=inf:
            # 使わない
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            # 使う
            if j+z<=10**5:
                dp[i+1][j+z] = min(dp[i+1][j+z], dp[i][j]+ch)

# print(dp)
ans_li = dp[len_cand][need:]
ans = min(ans_li)
print(ans)