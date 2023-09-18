N, M = map(int, input().split())

P = []
C = []
F = []
for i in range(N):
    inp = list(map(int, input().split()))
    p = inp[0]
    c = inp[1]
    f = set(inp[2:])
    P.append(p)
    C.append(c)
    F.append(f)

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if P[i]>=P[j]:
            if F[j]>=F[i]:
                if P[i]>P[j] or F[j]>F[i]:
                    print('Yes')
                    # print(i, j)
                    exit()

print('No')