N = int(input())

# 終了日でソートするため、[終了日, 開始日]の順に格納する
BA = []
for i in range(0, N):
  a, b = list(map(int, input().split()))
  BA.append([b, a])

BA.sort()

print(BA)

ans = 0
last = 0
for b, a in BA:
  if a > last:
    ans += 1
    last = b

print(ans)