from collections import deque

N = int(input())

count = 0

# キューを用意する
Q = deque()

# 1から9を待ち行列Qに追加
for i in range(1, 10):
  Q.append(i)
# Q = 1,2,3,4,5,6,7,8,9

# 最も位の高い数
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while len(str(Q[len(Q)-1])) <= N:
# for _ in range(0, N):
  i = Q.popleft()
  # iの1の位が1の時
  if i % 10 == 1:
    count += 2
    Q.append(10*i+i)
    Q.append(10*i+(i+1))
  # iの1の位が9の時
  elif i % 10 == 9:
    count += 2
    Q.append(10*i+(i-1))
    Q.append(10*i+i)
  # iの1の位が1,9以外
  else:
    count += 3
    Q.append(10*i+(i-1))
    Q.append(10*i+i)
    Q.append(10*i+(i+1))

print(count%998244353)