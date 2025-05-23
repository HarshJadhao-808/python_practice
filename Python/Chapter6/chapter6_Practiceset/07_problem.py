post=("Harsh is a intellgent man , Harsh is very curious and enthusiastic for learning")


if("harsh".lower() in post.lower()):
    print("Yes this post is talking about Harsh")
else:
    print("No this post is not talking about Harsh")



    # .lower()  :- can be used to convert into lowercase here we did so that even if 
    #              user input is in different caps both will be converted into small caps and then 
    #              evaluated which will work as we want