S = input()

T = ''

for _ in range(0, 10**4):
  T += 'oxxoxxoxxoxxoxxoxxoxxoxxoxxoxx'


def is_match(S, T):
  for i in range(0, len(S)+3):
    ok = True

    for j in range(0, len(S)):

      if T[i+j] != S[j]:
        ok = False

    if ok:
      return True
  
  return False

ans = is_match(S, T)

if ans:
  print('Yes')
else:
  print('No')