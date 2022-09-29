N = int(input())

LR = []
for i in range(0, N):
  LR.append(list(map(int, input().split())))

# print(LR)

LR.sort()

# print(LR)

Sec = []

for lr in LR:
  if len(Sec)==0:
    Sec.append(lr)
  else:
    if lr[0] > Sec[-1][1]:
      #2つの区間に分かれる場合
      Sec.append(lr)
    else:
      #1つの区間にまとまる場合
      if lr[1] > Sec[-1][1]:
        #範囲が広がる場合
        Sec[-1] = [Sec[-1][0], lr[1]]

        #内側に含まれるときは何もしない


# print("aaaaa")
# print(Sec)

for x in Sec:
  print(str(x[0]) + " " + str(x[1]))

  print(*x)