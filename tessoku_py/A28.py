N = int(input())

num = 0
for i in range(N):
  inp = list(input().split())
  t, a = inp[0], int(inp[1])
  if t == '+':
    num += a
    num %= 10000
  if t == '-':
    num -= a
    num %= 10000
  if t == '*':
    num *= a
    num %= 10000
  print(num)