# 10進数→2進数へ変換
def to_bin(n: int) -> int:
  ans = ''
  # nの最大値に応じて変更
  # 2**max_keta以内に収まるように
  max_keta = 50
  for i in range(max_keta, -1, -1):
    wari = n // (1<<i)
    ans += str(wari%2)
  return ans

S = input()
N = int(input())

bin_N_str = to_bin(N)

ans_bin = ''

for i in range():