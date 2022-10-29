N = int(input())
A = list(map(int, input().split()))

gu = []
ki = []
for x in A:
  if x % 2 == 0:
    gu.append(x)
  else:
    ki.append(x)

gu.sort()
ki.sort()

len_gu = len(gu)
len_ki = len(ki)

if len_gu <= 1 and len_ki <= 1:
  print(-1)
  exit()
elif len_gu <= 1:
  print(ki[-1]+ki[-2])
  exit()
elif len_ki <= 1:
  print(gu[-1]+gu[-2])
  exit()

ans1 = gu[-1]+gu[-2]
ans2 = ki[-1]+ki[-2]

if ans1 >= ans2:
  print(ans1)
else:
  print(ans2)