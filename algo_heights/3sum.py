from collections import defaultdict

k,n=map(int, input().split())

def solve(A):  
  # res =[] 
  H={e:i for i,e in enumerate(A)}
  A.sort()

  for i in range(n):
    if A[i]>0: # skip +ve nums (since all nums after are also +ve, thus cannot sum to 0)
      break
    if i>0 and A[i]==A[i-1]: # don't look at the same num consecutively
      continue

    l=i+1
    r=n-1
    while l<r:
      S=A[i]+A[l]+A[r]
      if S>0:
        r-=1
      elif S<0:
        l+=1
      else:
        return (H[A[i]]+1, H[A[l]]+1, H[A[r]]+1) # 1-based indexing
        # if we are looking for all solutions
        # res.append((H[A[i]]+1, H[A[j]]+1, H[A[k]]+1))
        # l+=1
        # while l<r and A[l]==A[l-1]:
        #   l+=1
  return (-1,)
  # return res