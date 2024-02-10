n,m=map(int, input().split())
E=[0]*(n+1)
for _ in range(m):
  u,v=map(int, input().split())
  E[u]+=1
  E[v]+=1
print(*E[1:])