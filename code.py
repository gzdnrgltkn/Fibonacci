num = int(input()) 

def fibonacci(n):

 a=0
 b=1
 if n==1:
  return a
 elif n==2:
  return b
 else:
  print(a) #this is n==1, prints 0
  print(b) #this is n==2, prints 1
  for i in range(2,n): #this starts at n==3 , prints 1 which is 0 plus 1 and the algorithym goes on. 
   c=a+b
   print(c)
   a=b
   b=c
   
fibonacci(num)
