s = list(input())
a, b = list(map(int, input().split()))

c = s[a-1]
s[a-1] = s[b-1]
s[b-1] = c

sol = ""

for i in range(len(s)):
  sol += s[i]

print(sol)