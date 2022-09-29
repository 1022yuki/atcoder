A, B, C = map(int, input().split())

ans = B//A

if ans > C:
  ans = C

print(ans)