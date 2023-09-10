N, D, P = map(int, input().split())
F = list(map(int, input().split()))

F.sort(reverse=True)
# print(F)

if N%D==0:
  max_num = N//D
else:
  max_num = (N//D)+1
# print(max_num)

# Fの累積和
sum_F = [0]
for i in range(len(F)):
  sum_F.append(sum_F[-1]+F[i])
# print(sum_F)

ans = 10**15
for i in range(max_num+1):
  # D*i枚の1日チケットを使う
  cnt = P*i
  if i*D<=N:
    cnt += sum_F[-1]-sum_F[i*D]
  # cnt += sum_F[-1]-sum_F[i*D-1]
  ans = min(ans, cnt)

print(ans)