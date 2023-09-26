N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()

# 累積和
sum_B = [0]
for i in range(M):
  sum_B.append(sum_B[-1]+B[i])

# 尺取り法で解く
ans = 0

#  Aの1番大きいやつとBの1番小さいやつの和がPを超えていた時、b=0で初期化だとバグるので-1
b = -1
for a in range(N):
  while b+1<M and A[a]+B[b+1]<=P:
    b += 1
  ans += (b+1)*A[a]
  ans += sum_B[b+1]
  ans += P*(M-(b+1))

print(ans)