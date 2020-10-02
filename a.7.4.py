#Script to print greater between two no.s and print the no. only once if both the no.s are same.
print("enter any two no.s")
p= int(input())
q= int(input())
#Method 1
#print(p)if(p>q)else print(q)
#Method 2
if(p>q):
    print(p)
elif(p==q):
    print(q)
else:
    print(q)
    
        
        
