M, D = map(int, input().split())
y, m, d = map(int, input().split())

# 次の日を求める
ans_y = y
ans_m = m
ans_d = d

if d==D:
  ans_d = 1
  if m==M:
    ans_m = 1
    ans_y += 1
  else:
    ans_m += 1
else:
  ans_d += 1

print(ans_y, ans_m, ans_d)