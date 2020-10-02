#Script to accept one complex no. from user and display the greater number between real and imaginary part.
print("enter the values of real and imaginary part")
Re=int(input())
Img=int(input())
c=complex(Re + Img)

if(Re> Img):
    print(Re)
else:
    print(Img)
