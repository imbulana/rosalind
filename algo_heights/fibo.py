n=int(input())
a=0
b=1
if n==0:
  print(a)
elif n==1:
  print(b)
else:
  i=2
  while i<=n:
    a,b=b,(a+b)
    i+=1
  print(b)