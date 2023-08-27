from collections import defaultdict

N = int(input())
S = []
for i in range(N):
    s = input()
    S.append(s)

dic = defaultdict(int)
ans=0
for i in range(N):
    s = S[i]
    s = min(s, s[::-1])
    # print(s)
    if dic[s]==0:
        ans += 1
        dic[s] = 1
print(ans)