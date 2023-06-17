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

N, M = map(int, input().split())

S = []
for i in range(N):
    s = input()
    S.append(s)

def check_dif(s1: str, s2: str):
    cnt = 0
    for m in range(M):
        if s1[m]!=s2[m]:
            cnt += 1
    if cnt==1:
        return True
    else:
        return False
  
a = list(range(N))
while True:
    # print(a)
    flag = True
    for i in range(N-1):
        s1 = S[a[i]]
        s2 = S[a[i+1]]
        # print(s1, s2)
        # print(check_dif(s1, s2))
        if not check_dif(s1, s2):
            flag = False
    # print(flag)
    if flag:
        print("Yes")
        exit()
    if not next_permutation(a, 0, N):
        break

print('No')