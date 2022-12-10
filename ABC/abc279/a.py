S = list(input())

# print(S)
ans = 0
for s in S:
  if s == 'w':
    ans += 2
  else:
    ans += 1

print(ans)