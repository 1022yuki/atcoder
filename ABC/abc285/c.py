S = input()

# 26進数
ls = len(S)

ans = 0
for i in range(ls):
  # print(ord(S[i])-ord('A'))
  ans += (26**i)*(ord(S[ls-i-1])-ord('A')+1)

print(ans)