S = list(input())

ans = 0

for i in range(0, len(S)):
  for j in range(i, len(S)):
    s = S[i:j+1]
    # print(s)
    state = True
    for x in s:
      if x != 'A' and x != 'C' and x != 'G' and x != 'T':
        state = False
    
    if state:
      ans = max(ans, len(s))

print(ans)