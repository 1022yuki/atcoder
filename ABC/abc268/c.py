N = int(input())
P = list(map(int, input().split()))

rotate = [0]*N

for i in range(N):
  # 人iの前に料理P[i]が置かれている
  rotate[(P[i]-i)%N] += 1
  rotate[(P[i]-i+1)%N] += 1
  rotate[(P[i]-i-1)%N] += 1

print(max(rotate))