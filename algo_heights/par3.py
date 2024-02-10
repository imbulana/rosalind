n=int(input())
A=list(map(int, input().split()))

def par3(A, p=0):
  A[0], A[p]=A[p], A[0]
  l=0
  r=n-1
  v=A[p]
  while l<r:
    if A[r]>v:
      r-=1
    elif A[l]<=v:
      l+=1
    else:
      A[l], A[r]=A[r], A[l]

  k=0
  while k<l:
    if A[k]!=v:
      k+=1
    elif A[l]==v:
      l-=1
    else:
      A[k], A[l]=A[l], A[k]
  return A

print(*par3(A))
