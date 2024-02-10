import heapq

n,m=map(int, input().split())
A=[[] for _ in range(n+1)]
for _ in range(m):
  u,v,w=map(int, input().split())
  A[u].append((v,w))

# min heap priority queue wrapper
class PriorityQueue:
  def __init__(self):
    self.elements=[]
  def push(self, key, value):
    heapq.heappush(self.elements, (key, value))
  def pop(self):
    return heapq.heappop(self.elements)[1]
  def empty(self):
    return not self.elements

# uniform cost search, get shortest distance to all nodes from s
def ucsd(A, s=1):
  frontier=PriorityQueue()
  dist=[-1]*(n+1)

  dist[s]=0
  frontier.push(0, s)
  while not frontier.empty():
    u=frontier.pop()
    for v,w in A[u]:
      d=dist[u]+w
      if dist[v]==-1 or d<dist[v]: # not visited or shorter distance
        dist[v]=d
        frontier.push(d, v)
  return dist[1:]

# get shortest path to all nodes from s
def uscp(A, s=1):
  frontier=PriorityQueue()
  dist=[-1]*(n+1)
  prev=[0]*(n+1)

  dist[s]=0
  prev[s]=-1
  frontier.push(0, s)
  while not frontier.empty():
    u=frontier.pop()
    for v,w in A[u]:
      d=dist[u]+w
      if prev[v]==0 or d<dist[v]:
        dist[v]=d
        prev[v]=u
        frontier.push(d, v)

  def getpath(t=n):
    if prev[t]==0: # no path to t from s
      return []
    path=[]
    u=t
    while u!=s:
      path.append(u)
      u=prev[u]
    path.append(s)
    path.reverse()
    return path
  
  for i in range(1, n+1):
    print(getpath(i), 'dist=', dist[i])

print(*ucsd(A))