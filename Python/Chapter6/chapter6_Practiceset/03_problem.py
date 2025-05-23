p1=("Make a lot of money")
p2=("subscribe this")
p3=("buy now")
p4=("click this")


message=input("Enter a message:")

if (p1 in message or p2 in message or p3 in message or p4 in message):
    print("This comment is a spam")

else:
    print("This comment is not a spam")
