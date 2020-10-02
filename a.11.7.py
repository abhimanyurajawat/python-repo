#script to count digits in a given no.
print("enter the value of n")
n=int(input())
count=0
while(n!=0):
    n=n//10    
    count+=1
print(count)
      
