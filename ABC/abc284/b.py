T = int(input())

def solve(N, A):
  cnt = 0
  for i in range(N):
    if A[i]%2==1:
      cnt+=1
  return cnt

for i in range(T):
  n = int(input())
  A = list(map(int, input().split()))
  print(solve(n, A))