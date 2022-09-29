N, M, K = map(int, input().split())
A = list(map(int, input().split()))

N = int(input())
P = list(map(int, input().split()))

for i in range(N):
  if i%2 == 0:
    if P[i]%2 == 0:
      for j in range(i+1, N):
        if P[j]%2 == 1:
          # i番目とj番目を交換
          
  if i%2 == 1:
    if P[i]%2 == 1:
      for j in range(i+1, N):
          # i番目とj番目を交換