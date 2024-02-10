def solve(A):
  H={}
  for i,e in enumerate(A):
    if -e in H:
      return H[-e]+1, i+1 # 1-indexed
    H[e]=i
  return (-1,)

k,n=map(int, input().split())
for _ in range(k):
  A=list(map(int, input().split()))
  print(*solve(A))
