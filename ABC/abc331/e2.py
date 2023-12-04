N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Bad = []
for i in range(N):
    Bad.append(set())

for i in range(L):
    c, d = map(int, input().split())
    Bad[c-1].add(d-1)

ans = -1

B_ind = []
for i in range(M):
    B_ind.append((B[i], i))
B_ind.sort()


for i in range(N):
    for j in range(M-1, -1, -1):
        if B_ind[j][1] not in Bad[i]:
            ans = max(ans, A[i]+B_ind[j][0])
            break

print(ans)