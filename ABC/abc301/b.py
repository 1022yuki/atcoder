N = int(input())
A = list(map(int, input().split()))

ans = [A[0]]

for i in range(N-1):
  fir = A[i]
  sec = A[i+1]
  if sec>fir:
    for i in range(fir+1, sec+1):
      ans.append(i)
  else:
    for i in range(fir, sec, -1):
      ans.append(i)
  # ans.pop()

print(ans)