T = int(input())

def solve():
  N = int(input())
  S = input()
  one = S.count("1")
  if one%2==1:
    print(-1)
    return
  else:
    cnt = 0
    if one==2:
      if S.count("11") == 1:
        if N==2 or N==3:
          print(-1)
          return
        cnt+=2
    print((one//2)+cnt)
    return

for i in range(T):
  solve()