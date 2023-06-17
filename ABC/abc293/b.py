N = int(input())
A = list(map(int, input().split()))

called = [False]*N
# called[0] = True

for i in range(N):
  if called[i]:
    continue
  called[A[i]-1] = True

ans = []
for i in range(N):
  if not called[i]:
    ans.append(i+1)

# print(called)
# print(ans)
print(len(ans))
print(*ans)