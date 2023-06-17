import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

visited = [False]*N

def dfs(n):
    inp = list(map(str, input().split()))
    if inp[0] == '-1' or inp[0] == 'OK':
        exit()
    edges = inp[1:]

    if visited[n-1]:
        return
    visited[n] = True
    for str_i in edges[n]:
        if not visited[int(str_i)-1]:
            print(str_i, flush=True)
            dfs(int(str_i))
            print()

dfs(1)

# while True:
#     inp = map(str, input().split())
#     if inp[0] == '-1' or inp[0] == 'OK':
#         break

#     if inp[0] == 1:
#         next = inp[1]
#     else:
#         ne = inp[1:]
#         if N in ne:
#             next = N
#         else:
#             for i in range(len(ne)):
#                 if not visited[ne[i]]:
#                     next = ne[i]
#                     break
                
    
#     visited[next] = True
#     print(next, flush=True)