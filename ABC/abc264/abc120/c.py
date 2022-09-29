S = input()
N = len(S)

cnt_red = 0
cnt_blue = 0
for i in range(N):
  if S[i] == '0':
    cnt_red += 1
  else:
    cnt_blue += 1

ans = min(cnt_red, cnt_blue) * 2

print(ans)