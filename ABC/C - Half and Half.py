A, B, C, X, Y = map(int, input().split())

# ABピザを買う枚数で全探索
# ABピザの枚数が決まれば残りの枚数が決まる
ABM = max(X, Y) * 2

ans = 10**10

for i in range(ABM+1):

  # ABピザがi枚のとき、Aピザは(X-[i/2])枚、Bピザは(X-[i/2])枚追加する必要がある
  if X-int(i/2)>0:
    add_A = X-int(i/2)
  else:
    add_A = 0

  if Y-int(i/2)>0:
    add_B = Y-int(i/2)
  else:
    add_B = 0
  
  price = add_A*A + add_B*B + i*C

  ans = min(ans, price)

print(ans)