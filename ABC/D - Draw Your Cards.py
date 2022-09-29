import bisect

N, K = map(int, input().split())

P = list(map(int, input().split()))

ans = [-1] * N

print(ans)

# 場の状態を保存、一番上の数字と現在の枚数の二次元配列
field = []

for i in range(N):
  x = P[i]

  if len(field) == 0:
    field.append([x, 0])

  else:
    ok = len(field)
    ng = -1

    while abs(ok-ng) > 1:
      mid = (ok+ng) // 2
      if field[mid][0] >= K:
        ok = mid
      else:
        ng = mid

    if ok == len(field):
      field.append([x, 1])
    else:
      field[ok][0] = x
      field[ok][1] += 1
    
    if field[x][1] >= K:
      del field[x]
      ans[field[x][0]] == i

print(ans)
    
    

  # field[n][0] = x
  # field[n][1] += 1

  # print(n)