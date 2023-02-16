S = list(input())

from collections import defaultdict, deque

st = deque()

dic = defaultdict(int)

for i in range(len(S)):
  # print(dic)
  # 英小文字の時
  if S[i] != "(" and S[i] != ")":
    if dic[S[i]] == 1:
      print('No')
      exit()
    st.append(S[i])
    dic[S[i]] = 1

  # (の時
  if S[i] == "(":
    st.append("(")

  # )の時
  if S[i] == ")":
    # print(st)
    while True:
      moji = st.pop()
      if moji == "(":
        break
      dic[moji] = 0

# print(deque)
print('Yes')