N = int(input())

for x in range(61):
  for y in range(61):
    if (2**x)*(3**y)==N:
      print('Yes')
      exit()

print('No')