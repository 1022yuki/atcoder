import re
s = list(input())

ans = []
for i in range(len(s)):
  if s[i]=="1":
    ans.append("0")
  else:
    ans.append("1")

print("".join(ans))