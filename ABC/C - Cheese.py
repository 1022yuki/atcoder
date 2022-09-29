N, W = map(int, input().split())

cheese = []
for i in range(N):
  a, b = map(int, input().split())
  cheese.append([a, b])

cheese.sort()

# print(cheese)

deli = 0
amount = 0

for i in range(N-1, -1, -1):
  a, b = cheese[i]
  if b+amount >= W:
    deli += a * (W-amount)
    break
  else:
    amount += b
    deli += a * b

print(deli)