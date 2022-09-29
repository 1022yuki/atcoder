A, B = map(int, input().split())

if A <= B:
  ans = B - A + 1
else:
  ans = 0

print(ans) 