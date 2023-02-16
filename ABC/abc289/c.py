# 10進数→2進数へ変換
def to_bin(n: int) -> int:
  ans = ''
  # nの最大値に応じて変更
  # 2**max_keta以内に収まるように
  max_keta = 10
  for i in range(max_keta, -1, -1):
    wari = n // (1<<i)
    ans += str(wari%2)
  return int(ans)

def has_bit(n, i):
  return n&(1<<i)>0

N, M = map(int, input().split())

C = []
A = []
for i in range(M):
  c = int(input())
  a = list(map(int, input().split()))
  C.append(c)
  A.append(a)

ans = 0

sel = 1<<M
# 集合の選び方
for n1 in range(sel):
  sum = 0
  flag = True
  for i in range(M):
    # n1に対してi個目の集合が含まれているか
    if has_bit(n1, i):
      # print(n1, i)
      for j in range(C[i]):
        # print('aaaaaa')
        # print(A[i][j])
        # print('aaaaaa')
        sum |= 1<<(A[i][j]-1)
  # print(sum)
  for k in range(N):
    if not has_bit(sum, k):
      flag = False
  if flag:
    ans += 1

print(ans)