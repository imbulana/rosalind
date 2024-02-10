def bins(A, n, k):
  L=0
  R=n-1
  while L<=R:
    M=(L+R)>>1
    v=A[M]
    if k<v:
      R=M-1
    elif k>v:
      L=M+1
    else:
      return M+1 # 1-indexed array
  return -1

n=int(input())
m=int(input())
A=list(map(int, input().split()))

for key in list(map(int, input().split())):
  print(bins(A,n,key))




