from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

dic = defaultdict(int)

for i in range(N):
  dic[A[i]] += 1

for i in range(K):
  if dic[i]==0:
    print(i)
    exit()

print(K)