def sum(n):
    if(n==1):
        return 1
    return n + sum(n-1)
n=int(input("Enter a number here :"))
answer = sum(n)

print("Sum of",n,"numbers is",answer)


    # if(n==1):
        # return 1

        # This is a base condition that is used to end recursion at some point 