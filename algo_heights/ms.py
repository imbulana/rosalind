def msr(A):
  if len(A)>1:
    C=len(A)//2
    L=msr(A[:C])
    R=msr(A[C:])

    i=j=k=0
    while i<len(L) and j<len(R):
      if L[k]<R[j]:
        A[k]=L[i]
        i+=1
      else:
        A[k]=R[j]
        j+=1
      k+=1
    while i<len(L):
      A[k]=A[i]
      i+=1
      k+=1
    while j<len(R):
      A[k]=A[j]
      j+=1
      k+=1
  return A

n=int(input())
A=list(map(int, input().split()))

print(*msr(A))