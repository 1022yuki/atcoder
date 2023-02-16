N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
X = list(map(int, input().split()))


# Aの累積和
sum = [0]
for i in range(N):
  sum.append(sum[-1]+A[i])
# print(sum)

done = [False]*(N)

ans = 0

for m in range(M-1, -1, -1):
  if done[X[m]-1]:
    # print("skip")
    continue
  comod_ind = X[m]-1
  comod = A[comod_ind]
  # done[m] = True
  money = 10**13
  for i in range(X[m]):
    # print(comod_ind, comod_ind-i)
    A_sum = sum[comod_ind+1]-sum[comod_ind-i]
    # print(A_sum)
    # print(C[comod_ind-i])
    mon_con = A_sum + C[comod_ind-i]*(i+1)
    # print(mon_con)
    # print()
    money = min(money, mon_con)
    if money == mon_con:
      min_ind = comod_ind-i

  # print(money)
  # print(min_ind)
  done = [False]*min_ind+[True]*(N-min_ind)
  # print(done)
  ans += money


print(ans)