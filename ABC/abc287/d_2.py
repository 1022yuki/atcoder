S = list(input())
T = list(input())

ls = len(S)
lt = len(T)

lim_f = lt
for i in range(lt):
  # マッチしない場合
  if S[i]!="?" and T[i]!="?" and S[i]!=T[i]:
    lim_f = i
    break
# 先頭i文字目までマッチ
first = [True]*(lim_f+1)+[False]*(lt-lim_f)

lim_l = lt
for i in range(lt):
  # マッチしない場合
  if S[ls-1-i]!="?" and T[lt-1-i]!="?" and S[ls-1-i]!=T[lt-1-i]:
    lim_l = i
    break
# 末尾i文字目までマッチ
last = [True]*(lim_l+1)+[False]*(lt-lim_l)

# print(first)
# print(last)

for i in range(lt+1):
  # 先頭i文字まで+末尾lt-i文字までがマッチしていればyes
  if first[i] and last[lt-i]:
    print("Yes")
  else:
    print("No")