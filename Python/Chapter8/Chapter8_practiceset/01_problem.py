def greatest (a,b,c):
    if (a>b and a>c):
        return a
    if(b>a and b>c):
        return b
    if(c>a and c>b):
        return c
    
num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
num3=int(input("Enter third number :"))

answer=greatest(num1,num2,num3)

print(answer,"is the greatest number")