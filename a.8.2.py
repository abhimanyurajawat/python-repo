#Script to check the given quadratic eqn. has real and distinct roots, real and equal roots or imaginary roots.
print("enter the values of both roots")
n=float(input())
m=float(input())
if(n!= m):
    print("real and distinct roots")
elif(n==m):
    print("real and equal roots")
else:
    print("imaginary roots")
    
