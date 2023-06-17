import math
from collections import defaultdict

N = int(input())
C = list(map(int, input().split()))

mod = 10**5+3
ans = 0

# 全部同じなら階乗が答え
if C.count(C[0])==N:
    print(math.factorial(N)%mod)
    exit()

# 全部異なる時は2^N-1が答え
dict = defaultdict(int)
flag = True 
for i in range(N):
    if dict[C[i]]==1:
        flag = False
        break
    else:
        dict[C[i]]+=1
if flag:
    print((2**(N-1))%mod)
    exit()

# 以下、全探索

# 配列aの[l, r)の部分のnext_permutation
def next_permutation(a: list, l: int = 0, r: int = None) -> bool:
    # a[l,r)の次の組み合わせ
    if r is None:
        r = len(a)
    for i in range(r - 2, l - 1, -1):
        if a[i] < a[i + 1]:
            for j in range(r - 1, i, -1):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
                    p, q = i + 1, r - 1
                    while p < q:
                        a[p], a[q] = a[q], a[p]
                        p += 1
                        q -= 1
                    return True
    return False

a = list(range(N))
while True:
    cnt_out = 0
    flag = True
    for i in range(N):
        cnt_in = 0 
        for j in range(i+1, N):
            if C[a[i]]<C[a[j]]:
                cnt_in += 1
                if cnt_in == 2:
                    break
        if cnt_in == 2:
            flag = False
            break
    if flag:
        ans += 1
                
    if not next_permutation(a, 0, N):
        break

print(ans%mod)