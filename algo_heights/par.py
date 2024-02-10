def par(A, pivot=0):
  L=[]
  G=[]
  p=A[pivot]
  for i,e in enumerate(A):
    if i==pivot: continue
    if e<=p:
      L.append(e)
    else: G.append(e)
  return L+[p]+G

def par_inplace(A, n, pivot=0):
  if pivot!=n-1:
    A[pivot], A[n-1]=A[n-1], A[pivot]
  for i in range(n):
    if A[i]>A[n-1]:
      break
  for j in range(i,n):
    if A[j]<A[n-1]:
      A[i], A[j]=A[j], A[i]
      i+=1
  A[i], A[n-1]=A[n-1], A[i]
  return A

def par_2pt(A, l, r, p=0):
  A[p], A[0]=A[0], A[p]
  p=A[0]
  while l<r:
    if A[r]>p:
      r-=1
    elif A[l]<=p:
      l+=1
    else:
      A[r], A[l]=A[l], A[r]
  A[0], A[l]=A[l], A[0]

n=int(input())
A=list(map(int, input().split()))
print(*par(A))
print(*par_inplace(A,n))
print(*par_2pt(A,0,n-1))