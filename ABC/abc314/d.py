N = int(input())
S = list(input())
Q = int(input())

qs = []
last = -1
for q in range(Q):
    t, x, c = map(str, input().split())
    t = int(t)
    x = int(x)
    x -= 1
    qs.append((t, x, c))
    if t==2 or t==3:
        last = q

# print(last)

for q in range(Q):
    t, x, c = qs[q]
    if t==1:
        S[x] = c
    if q == last:
        if t==2:
            tmp = ''.join(S)
            tmp = tmp.lower()
            # print('low')
            # print(tmp)
            S = list(tmp)
        if t==3:
            tmp = ''.join(S)
            tmp = tmp.upper()
            # print('up')
            # print(tmp)
            S = list(tmp)

print(''.join(S))