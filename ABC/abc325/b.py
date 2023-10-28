N = int(input())

W = []
X = []
for i in range(N):
  w, x = map(int, input().split())
  W.append(w)
  X.append(x)

Nums = []
for n in range(24):
  num = 0
  for i in range(N):
    w, x = W[i], X[i]
    startTime = n+x
    startTime %= 24
    if 9<=startTime and startTime<=17:
      num += w
      # print(w, x)
  Nums.append(num)

# print(Nums)
print(max(Nums))