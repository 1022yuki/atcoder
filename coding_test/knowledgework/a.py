from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

dic = defaultdict(int)

for i in range(N):
    if dic[A[i]] == 0:
        dic[A[i]] = 1
    else:
        print(i+1)
        exit()

print(-1)