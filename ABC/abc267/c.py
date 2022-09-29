N, M = map(int, input().split())
A = list(map(int, input().split()))

sum = [0]
for x in A:
  sum.append(sum[-1]+x)

# print(sum)

D = []
for i in range(N-M):
  dif = M*A[i+M] - (sum[i+M]-sum[i])
  D.append(dif)

# print(D)

sum_dif = [0]
for x in D:
  sum_dif.append(sum_dif[-1]+x)

# print(sum_dif)

m = max(sum_dif)
for i in range(len(sum_dif)):
  if sum_dif[i] == m:
    max_ind = i

# print(i)

ans = 0
for i in range(M):
  ans += A[max_ind+i] * (i+1)

print(ans)