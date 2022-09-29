# 文字列Tが文字列Sにマッチするかどうかを判定する関数
# マッチするときはTrueを、そないときはFalseを返す
def is_match(T, S):
  
  # 文字列Sのi文字目から始まる部分が文字列Tとマッチするあどうか調べる
  for i in range(0, len(S)-len(T)+1):
    
    ok = True

    for j in range(0, len(T)):
      if T[j] != S[i+j] and T[j] != '.':
        ok = False

    if ok:
      return True

  return False

S = input()

# 使える文字の一覧
C = "abcdefghijklmnopqrstuvwxyz."

# 文字列Sとマッチする文字列を保持する配列
M = []

# 長さ1の文字列について調べ、マッチしているものをMにいれる
for T in C:
  if is_match(T, S):
    M.append(T)

# 長さ2の文字列について調べ、マッチしているものをMにいれる
for c1 in C:
  for c2 in C:
    T = c1 + c2
    if is_match(T, S):
      M.append(T)

# 長さ2の文字列について調べ、マッチしているものをMにいれる
for c1 in C:
  for c2 in C:
    for c3 in C:
      T = c1 + c2 + c3
      if is_match(T, S):
        M.append(T)

print(len(M))