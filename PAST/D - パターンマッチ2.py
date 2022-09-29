# TがSにマッチしているかどうか調べる関数、帰り値はTrueかFalse
def is_match(S, T):

  # Sのi番目から始まる部分がTとマッチするか調べる
  for i in range(0, len(S)-len(T)+1):

    ok = True

    # Sのi＋j番目とTのj番目が等しいか調べる
    for j in range(0, len(T)):

      # Tのj番目がSのi+j番目とことなっていて、かつ.でもなければokをFalseに
      if S[i+j] != T[j] and T[j] != ".":
        ok = False
    
    # あるiについてokがTrueとなったとき
    if ok:
      return True
    
  # すべてのiについてokがFalseとなったとき
  return False


S = input()

# SにマッチするTを保持する配列
M = []

# 上で定義した関数にS,Tを渡し、条件を満たすTをMに追加する
# 考えられるあらゆるTを作る

# 全ての小文字アルファベット及び.を持つ文字列
C = "qwertyuiopasdfghjklzxcvbnm."

# len(T)=1
for i in C:
  T1 = i
  if is_match(S, T1):
    M.append(T1)

# 2
for i in C:
  for j in C:
    T2 = i + j
    if is_match(S, T2):
      M.append(T2)

# 3
for i in C:
  for j in C:
    for k in C:
      T3 = i + j + k
      if is_match(S, T3):
        M.append(T3)

print(len(M))