N, D, P = map(int, input().split())
F = list(map(int, input().split()))

F.sort(reverse=True)
# print(F)

sum_F = [0]
for i in range(N):
  sum_F.append(sum_F[-1]+F[i])

# print(sum_F)

ans = 10**15
# 1日周遊パスを何枚使うか(0~N枚)全探索
for n in range(N+1):
  # 周遊パスをn枚買う料金
  if n%D==0:
    path = (n//D)*P
  else:
    path = ((n//D)+1)*P
  # 周遊パスを使わない区間の料金
  fair = sum_F[-1]-sum_F[n]
  all = path+fair
  ans = min(ans, all)

print(ans)