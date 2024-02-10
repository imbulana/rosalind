def ins(A, n):
  swaps=0
  for i in range(1,n):
    j=i
    while j>0 and A[j]<A[j-1]:
      A[j], A[j-1] = A[j-1], A[j]
      j-=1
      swaps+=1
  return A, swaps

n=int(input())
A=list(map(int, input().split()))

print(ins(A,n)[1])