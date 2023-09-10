M = int(input())
D = list(map(int, input().split()))

sum_d = sum(D)
mid = (sum_d+1) // 2

cnt = 0
for i in range(M):
  if cnt+D[i] >= mid:
    month = i+1
    day = mid - cnt
    break
  cnt += D[i]

print(month, day)