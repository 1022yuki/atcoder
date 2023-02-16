from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

mod = 100
dic = defaultdict(int)

for i in range(N):
  dic[A[i]%mod] += 1

# print(dic)

ans = 0
for i in range(1, 50):
  ans += dic[i]*dic[100-i]
ans += dic[50]*(dic[50]-1)//2
ans += dic[0]*(dic[0]-1)//2

print(ans)