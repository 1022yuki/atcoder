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
      if N==3:
        if S[1] == "1":
          print(-1)
          return
      if N==4:
        if S[1:3] == "11":
          cnt+=1
      if S.count("11") == 1:
        cnt+=1
    # print(one)
    # print(cnt)
    print((one//2)+cnt)
    return

for i in range(T):
  solve()