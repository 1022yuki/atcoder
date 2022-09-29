L1, R1, L2, R2 = map(int, input().split())

li = [0]*100
for i in range(L1, R1):
  li[i] += 1

for i in range(L2, R2):
  li[i] += 1

# print(li)

ans = 0

for x in li:
  if x == 2:
    ans += 1

print(ans)