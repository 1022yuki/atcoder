from collections import deque

K = int(input())

num10 = 9

# ルンルンナンバーを格納するリスト
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# キューを用意する
Q = deque()

for i in range(1, 10):
  Q.append(i)

# キューから取り出しながら探索する
while(len(Q)) > 0:
  if num10 == K:
    break
  i = Q.popleft()
  iti = i % 10
  if num10 <= K and iti != 0:
    run = i*10+iti-1
    Q.append(run)
    num10 += 1
    list.append(run)
    # print(list)

  if num10 <= K:
    run = i*10+iti
    Q.append(run)
    num10 += 1
    list.append(run)
    # print(list)

  if num10 <= K and iti != 9:
    run = i*10+iti+1
    Q.append(run)
    num10 += 1
    list.append(run)
    # print(list)

# if K <= 10:
#   num = K
# else:
#   num = num10

print(list[K-1])