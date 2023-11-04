X, Y = map(int, input().split())

if X<=Y:
  # のぼり
  if Y-X<=2:
    print('Yes')
  else:
    print('No')
else:
  # おりる
  if X-Y<=3:
    print('Yes')
  else:
    print('No')