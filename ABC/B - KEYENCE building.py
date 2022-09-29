N = int(input())

S = list(map(int, input().split()))

count = 0

for s in S:

  flag = False

  for a in range(1, max(S)):
    for b in range(1, max(S)):
      if 4*a*b+3*a+3*b == s:
        flag = True
  if not flag:
    count += 1

print(count)