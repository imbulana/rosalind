n,m=map(int, input().split())
E=[[] for _ in range(n+1)]
for _ in range(m):
  u,v=map(int, input().split())
  E[u].append(v)
  E[v].append(u)

for i in range(1, n+1):
  dsum=0
  for v in len(E[i]):
    dsum+=len(E[v])
  print(dsum)