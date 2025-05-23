marks=int(input("Enter your marks :"))


if(marks<=100 and marks>=0 and marks>=90):
    print("Congratulations you are passed with",marks,"and you have got grade Ex")

elif(marks<=100 and marks>=0 and  marks>=80 and marks<90):
    print("Congratulations you are passed with",marks,"and you have got grade A")

elif(marks<=100 and marks>=0 and  marks>=70 and marks<80):
    print("Congratulations you are passed with",marks,"and you have got grade B")

elif(marks<=100 and marks>=0 and marks<60 and marks>=50):
    print("Congratulations you are passed with",marks,"and you have got grade C")

elif(marks<=100 and marks>=0 and marks<50 ):
    print("Sorry you are fsilrd with",marks,"and you have got grade F")

else:
    print("please enter valid marks")