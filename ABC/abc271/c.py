N = int(input())
a = list(map(int, input().split()))
a.sort()
A = [0]+a

from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] 
def runLengthEncode(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

# print(runLengthEncode(A))
run_A = runLengthEncode(A)

end = N
i = 1
manga = 1
ans = 0

while(i<=end):
  # if A[i] == manga-1:
  #   print('aaaaaaa')
  #   i += 1
  #   end += 1
  if i==end:
    if run_A[i][0] == manga:
      ans += 1
      i += 1
    else:
      i += 1
  else:
    ans += 1
    if run_A[i][0] == manga:
      if run_A[i][1] >= 2:
        run_A.append((run_A[i][0], run_A[i][1]-1))
      i += 1
      manga += 1
      # ans += 1
    else:
      end -= 2
      manga += 1
      # ans += 1

print(ans)