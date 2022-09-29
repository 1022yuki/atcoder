import sys
sys.setrecursionlimit(1000000)

N, X = map(int, input().split())
A = list(map(int, input().split()))

know = [False] * N

def rec(i):
  if not know[i-1]:
    know[i-1] = True
    rec(A[i-1])

rec(X)
  
count = 0
for i in range(N):
  if know[i]:
    count += 1

# print(know)
print(count)