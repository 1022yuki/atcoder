N = int(input())
S = list(input())
Q = int(input())

s1 = S[:N]
s2 = S[N:]

for _ in range(Q):
  t, a, b = map(int, input().split())

  if t == 1:
    if a<=N and b <= N:
      # s1の中で交換
      x = s1[a-1]
      s1[a-1] = s1[b-1]
      s1[b-1] = x
    elif a > N and b > N:
      x = s2[a-1-N]
      s2[a-1-N] = s2[b-1-N]
      s2[b-1-N] = x
    elif a > N:
      x = s2[a-1-N]
      s2[a-1-N] = s1[b-1]
      s1[b-1] = x
    else:
      x = s2[b-1-N]
      s2[b-1-N] = s1[a-1]
      s1[a-1] = x

  if t == 2:
    s3 = s1
    s1 = s2
    s2 = s3

# print(s1 + s2)
# print(S)

ans = ''
for x in s1:
  ans += x
for x in s2:
  ans += x

print(ans)