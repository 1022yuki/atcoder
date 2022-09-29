N = int(input())
S = input()

ans = ''

for i in S:
  if ord(i)+N <= 90:
    ans += chr(ord(i)+N)
  else:
    ans += chr(ord(i)+N-26)

print(ans)