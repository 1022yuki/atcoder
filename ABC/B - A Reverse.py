L, R = map(int, input().split())
S = list(input())

first = S[0:L-1]
last = S[R:len(S)]

rev = S[L-1:R]

rev.reverse()

# print(first)
# print(rev)
# print(last)

ans = first + rev + last

strA = "".join(ans)

print(strA)