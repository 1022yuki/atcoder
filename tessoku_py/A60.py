from collections import deque

N = int(input())
A = [0]+list(map(int, input().split()))

st = deque()
ans = [None]*N

for i in range(1, N+1):
  if i>=2:
    st.append((i-1, A[i-1]))
    while len(st)>0:
      kabuka = st[-1][1]
      if kabuka <= A[i]:
        st.pop()
      else:
        break

  if len(st)>0:
    ans[i-1] = st[-1][0]
  else:
    ans[i-1] = -1


print(*ans)