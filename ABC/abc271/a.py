N = int(input())

ans = format(N, 'x')

ans2 = ans.upper()

# print(ans2)

if len(ans2) == 1:
  ans2 = '0' + ans2

print(ans2)