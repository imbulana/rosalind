n,m=map(int, input().split())
A=[[] for _ in range(n+1)]
for _ in range(m):
  u,v=map(int, input().split())
  A[u].append(v)
  A[v].append(u)

def dfs(A):
  visited=[False]*(n+1)
  cc=0
  def explore(u):
    visited[u]=True
    for v in A[u]:
      if not visited[v]:
        explore(v)
  for u in range(1,n+1):
    if not visited[u]:
      cc+=1
      explore(u) # explore one component
  return cc
print(dfs(A))
  
