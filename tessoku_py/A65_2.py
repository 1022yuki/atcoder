import sys
sys.setrecursionlimit(10**7)

N = int(input())
A = [-1, -1]+list(map(int, input().split()))

# print(A)

buka = []
for i in range(N+1):
  buka.append([])

for i in range(2, N+1):
  jousi = A[i]
  buka[jousi].append(i)

# print(buka)

buka_num = [-1]*(N+1)

# done = [False]*(N+1)

def dfs(i):
  if buka_num[i] != -1:
    return buka_num[i]
  sum = 0
  for j in buka[i]:
    sum += dfs(j)
  buka_num[i] = sum
  return buka_num[i]+1

dfs(1)
print(*buka_num[1:])