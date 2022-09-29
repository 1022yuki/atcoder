N, M, X, T, D = map(int, input().split())

sin = 0

if X <= M <= N:
  print(T)
else:
  print(T-D*(X-M))