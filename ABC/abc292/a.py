S = list(input())

dif = ord("a")-ord("A")
ans = []
# print(dif)
for i in range(len(S)):
  n = ord(S[i])-dif
  ans.append(chr(n))

print("".join(ans))