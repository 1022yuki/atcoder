N = int(input())

S = []
for i in range(N):
    s = list(input())
    S.append(s)

from collections import defaultdict
dic = defaultdict(int)


s_a = set()
ans = 0
for i in range(N):
    s = S[i]
    set_i = set()
    str1 = q = ''.join(s)
    set_i.add(str1)
    # s_a.add(str1)
    s.reverse()
    str2 = ''.join(s)
    set_i.add(str2)
    # s_a.add(str2)

    if not set_i.issubset(s_a):
        ans += 1

    s_a.add(str1)
    s_a.add(str2)

    

# print(dic)
print(ans)