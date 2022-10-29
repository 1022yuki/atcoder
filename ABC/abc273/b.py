X, K = map(int, input().split())

def sg(n, dig):
  # print(n)
  if dig != 0:
    n /= 10
  
  iti = n % 10
  if iti <= 4:
    n -= iti
  else:
    n -= iti
    n += 10
  return n

for i in range(0, K):
  X = sg(X, i)

print(int(X*(10**(K-1))))