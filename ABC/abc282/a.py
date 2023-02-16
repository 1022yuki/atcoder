K = int(input())

num = ord('A')

# print(num)

ans = ""

for i in range(K):
  ans += chr(num)
  num+=1

print(ans)