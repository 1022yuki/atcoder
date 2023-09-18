N, H, X = map(int, input().split())
P = list(map(int, input().split()))

num = X-H
for i in range(N):
    if num<=P[i]:
        print(i+1)
        exit()