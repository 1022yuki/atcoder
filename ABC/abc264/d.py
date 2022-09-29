s = list(input())

ans = 0

for i in range(7):
  if s[i] == 'a':
    del s[i]
    s.insert(0, 'a')
    ans += i

# print(s)
# print(ans)

for i in range(7):
  if s[i] == 't':
    del s[i]
    s.insert(1, 't')
    ans += abs(i-1)

# print(s)

for i in range(7):
  if s[i] == 'c':
    del s[i]
    s.insert(2, 'c')
    ans += abs(i-2)

for i in range(7):
  if s[i] == 'o':
    del s[i]
    s.insert(3, 'o')
    ans += abs(i-3)

for i in range(7):
  if s[i] == 'd':
    del s[i]
    s.insert(4, 'd')
    ans += abs(i-4)

for i in range(7):
  if s[i] == 'e':
    del s[i]
    s.insert(5, 'e')
    ans += abs(i-5)

for i in range(7):
  if s[i] == 'r':
    del s[i]
    s.insert(6, 'r')
    ans += abs(i-6)

print(ans)