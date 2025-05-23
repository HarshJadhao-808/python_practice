marks1=int(input("Enter marks 1 :"))
marks2=int(input("Enter marks 2 :"))
marks3=int(input("Enter marks 3 :"))
marks4=int(input("Enter marks 4 :"))


# Check for total percentage

total_percentage=((marks1+marks2+marks3+marks4)/400)*100


if(total_percentage>=40):
    print("you are passed with", total_percentage)

else:
    print("sorry you are failed with ", total_percentage)    