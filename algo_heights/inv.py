n=int(input())
A=list(map(int, input().split()))

inv=0
def ms(A):
  if len(A)>1:
    m=len(A)//2
    L=A[:m]
    R=A[m:]
    ms(L)
    ms(R)

    i=j=k=0
    while i<len(L) and j<len(R):
      if L[i]<=R[j]:
        A[k]=L[i]
        i+=1
      else:
        A[k]=R[j]
        j+=1
        global inv
        inv+=m-i # choosing from R means every elt in L after and incl. L[i] is greater than R[j]
      k+=1
    while i<len(L):
      A[k]=L[i]
      i+=1
      k+=1
    while j<len(R):
      A[k]=R[j]
      j+=1
      k+=1

ms(A)
print(inv)