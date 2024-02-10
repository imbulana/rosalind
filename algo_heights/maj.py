def maj(A):
  candidate, count = 0,0
  for e in A:
    if count==0:
      candidate=e
    count +=1 if e==candidate else -1

  count=0
  for e in A:
    if e==candidate:
      count+=1
  return candidate if count>n//2 else -1

k,n=map(int, input().split())

for _ in range(k):
  A=list(map(int,input().split()))
  print(maj(A))


