import math

N = int(input())

# N番目のゾロ目の桁数
x = math.ceil(N/9)

# N番目のゾロ目の数字
y = N % 9

if y == 0:
  y = 9

ans = ''

for i in range(0, x):
  ans += str(y)

print(int(ans))