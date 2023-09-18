N = int(input())

C = []
A = []
for i in range(N):
    ci = int(input())
    a = list(map(int, input().split()))
    C.append(ci)
    A.append(a)
X = int(input())

ok = [False]*N

for i in range(N):
    for j in range(len(A[i])):
        if A[i][j] == X:
            ok[i] = True

ans = []
min_num = 40
for i in range(N):
    if ok[i]:
        num = C[i]
        if num < min_num:
            ans = []
            ans.append(i+1)
            min_num = num
        elif num == min_num:
            ans.append(i+1)

ans.sort()
print(len(ans))
print(*ans)