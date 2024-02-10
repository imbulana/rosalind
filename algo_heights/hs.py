n=int(input())
A=list(map(int, input().split()))

def heapify(A, i, n):
  g=i
  l=2*i+1
  r=2*i+2
  if r<n and A[r]>A[g]:
    g=r
  if l<n and A[l]>A[g]:
    g=l
  if g!=i:
    A[g], A[i]=A[i], A[g]
    heapify(A, g, n)

def convert(A, n):
  for i in range(n//2-1, -1, -1):
    heapify(A, i, n)

def hs(A):
  convert(A, n)
  for i in range(n-1, 0, -1):
    A[0], A[i]=A[i], A[0]
    heapify(A, 0, i)

hs(A)
print(*A)

  
  