N = int(input())

# X[d]: d日目から実行可能になるタスクのポイントを集めた配列
X = []
for i in range(0, N):
  X.append([])

# print(X)

for i in range(0, N):
  a, b = list(map(int, input().split()))
  X[a-1].append(b)

# print(X)

# cnt[b]: 実行可能なタスクの中でポイントがbであるものの個数
cnt = [0]*101

ans = 0

# print(cnt)

for d in range(0, N):
  # d日目から実行可能なタスクをcntに追加する
  for b in X[d]:
    cnt[b] += 1

  # cnt[b]>0 である最大のbを探して加算する
  for b in range(100, 0, -1):
    if cnt[b] > 0:
      ans += b
      cnt[b] -= 1
      break
    
  print(ans)