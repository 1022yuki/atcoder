N = int(input())
P = list(map(int, input().split()))

count = 1

def rec(i):
  global count
  # print(count)
  pare = P[i-2]
  if pare == 1:
    return count
  else:
    count += 1
    rec(pare)

rec(N)

print(count)