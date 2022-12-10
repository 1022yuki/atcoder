from collections import deque
S = input()

st = deque()

for i in range(len(S)):
  if S[i] == '(':
    st.append(i+1)
  if S[i] == ')':
    la = i+1
    fi = st.pop()
    print(fi, la)