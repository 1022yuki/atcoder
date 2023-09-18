N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

from collections import defaultdict
dict = defaultdict(list)

culind = [-1]*N

for i in range(N):
    culind[i] = len(dict[C[i]])
    dict[C[i]].append(i)

# print(dict)

ans = ['']*N

for m in range(1, M+1):
    tmp = dict[m]
    tmp.append(tmp[0])
    del tmp[0]
    # print(tmp)
    dict[m] = tmp

# print(dict)

for i in range(N):
    ans[dict[C[i]][culind[i]]] = S[i]

print(''.join(ans))