N, K = map(int, input().split())
S = list(input())

cnt_1 = S.count("1")

if (cnt_1-K)%2 == 0:
  print("Yes")
else:
  print("No")