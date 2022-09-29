S, T, X = map(int, input().split())

if S < T and S <= X < T:
  print('Yes')
elif S > T and S <= X < T+24 or S <= X+24 < T+24:
  print('Yes')
else:
  print('No')