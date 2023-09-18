N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A+B
C.sort()

# print(C)

ans1 = [None]*N
ans2 = [None]*M

from collections import defaultdict
dic = defaultdict(int)

for i in range(N+M):
  dic[C[i]] = i+1

for i in range(N):
  ans1[i] = dic[A[i]]

for i in range(M):
  ans2[i] = dic[B[i]]

print(*ans1)
print(*ans2)