n=int(input())
A=list(map(int, input().split()))
m=int(input())
B=list(map(int, input().split()))

i=j=k=0
C=[0]*(n+m)
while i<n and j<m:
  if A[i]<B[j]:
    C[k]=A[i]
    i+=1
  else: 
    C[k]=B[j]
    j+=1
  k+=1
while i<n:
  C[k]=A[i]
  k+=1
  i+=1
while j<m:
  C[k]=B[j]
  k+=1
  j+=1

print(*C)