from collections import deque

n,m=map(int, input().split())
A=[[] for _ in range(n+1)]
for _ in range(m):
  u,v=map(int, input().split())
  A[u].append(v)

# get shortest dist to all nodes from s, return -1 if no path
def bfsd(A, s=1):
  frontier=deque()
  dist=[-1]*(n+1)

  frontier.append(s)
  dist[s]=0
  while frontier:
    u=frontier.popleft()
    for v in A[u]:
      if dist[v]==-1:
        dist[v]=dist[u]+1
        frontier.append(v)
  return dist[1:]

# get shortest path to all nodes from s, return ([], -1) if no path
# does not keep track of distance but can be obtained via length of path-1
def bfsp(A, s=1):
  frontier=deque()
  prev=[0]*(n+1)

  prev[s]=-1
  frontier.append(s)
  while frontier:
    u=frontier.popleft()
    for v in A[u]:
      if prev[v]==0:
        prev[v]=u
        frontier.append(v)

  def getpath(t):
    if prev[t]==0: # t is not reachable
      return []

    path=[]
    v=t
    while v!=s:
      path.append(v)
      v=prev[v]
    path.append(s)
    path.reverse()
    return path

  for i in range(1, n+1):
    P=getpath(i)
    print(getpath(i), 'dist=', len(P)-1)

print(*bfsd(A))
