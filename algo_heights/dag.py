def acyclic(A, n):
  color=[0]*(n+1)
  def explore(u):
    color[u]=1
    for v in A[u]:
      if color[v]==1:
        return False
      if not color[v]:
        if not explore(v):
          return False
    color[u]=2
    return True
  for u in range(1, n):
    if not color[u]:
      if not explore(u):
        return -1
  return 1

k=int(input())
for _ in range(k):
  _=input()
  n,m=map(int, input().split())
  A=[[] for _ in range(n+1)]
  for _ in range(m):
    u,v=map(int, input().split())
    A[u].append(v)
  print(acyclic(A, n))