N, C = map(str, input().split())
N = int(N)
S = list(input())

cnt_r = S.count("R")
cnt_b = S.count("B")
cnt_w = S.count("W")

if C == "W":
  if (cnt_r-cnt_b)%3 == 0:
    print("Yes")
  else:
    print("No")

if C == "R":
  if (cnt_r-cnt_b)%3 == 1:
    print("Yes")
  else:
    print("No")

if C == "B":
  if (cnt_r-cnt_b)%3 == 2:
    print("Yes")
  else:
    print("No")