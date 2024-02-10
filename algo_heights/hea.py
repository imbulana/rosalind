n=int(input())
A=list(map(int, input().split())) 

def heapify(i):
	g=i
	l=2*i
	r=2*i+1
	if r<=n and A[r-1]>A[g-1]:
		g=r
	if l<=n and A[l-1]>A[g-1]:
		g=l
	if g!=i:
		A[g-1], A[i-1]=A[i-1], A[g-1]
		heapify(g)

for i in range(n//2, 0, -1):
	heapify(i)

print(*A)