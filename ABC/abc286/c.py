N, A, B = map(int, input().split())
S = input()

num = N//2
ans = 10**15

def check(St):
  cost = 0
  for i in range(num):
    if St[i] != St[N-1-i]:
      cost += 1
  return cost

# print(check(S))
cost = 0
for rot in range(N):
  cost = 0
  cost += A*rot
  r_s = S[rot:]+S[:rot]
  # print(r_s)
  cost += B*check(r_s)
  ans = min(ans, cost)
  # print(cost)

print(ans)

# print(check("refar"))