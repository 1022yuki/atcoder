A, B, C, D, E, F, X = list(map(int, (input().split())))

if X%(A+C) < A:
  taka = (X//(A+C))*A*B + (X%(A+C))*B
  # aoki = (X//(D+F))*D*E + (X%(D+F))*E
else:
  taka = (X//(A+C))*A*B + A*B
  # aoki = (X//(D+F))*D*E + D*E

if X%(D+F) < D:
  # taka = (X//(A+C))*A*B + (X%(A+C))*B
  aoki = (X//(D+F))*D*E + (X%(D+F))*E
else:
  # taka = (X//(A+C))*A*B + A*B
  aoki = (X//(D+F))*D*E + D*E


if taka > aoki:
  print('Takahashi')
elif taka < aoki:
  print('Aoki')
else:
  print('Draw')