N, M = map(int, input().split())

s_a = set()
for i1 in range(1, N+1):
    for j1 in range(i1+1, N+1):
        s_a.add((i1, j1))

# print(s_a)

s_b = set()

a = []
for i in range(M):
    inp = list(map(int, input().split()))
    a.append(inp)

for i in range(M):
    # print(a[i])
    for j in range(N-1):
        # print(a[i][j], a[i][j+1])
        c1 = a[i][j]
        c2 = a[i][j+1]
        if c1 > c2:
            c1, c2 = c2, c1
        s_b.add((c1, c2))

print(len(s_a.difference(s_b)))