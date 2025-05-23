harsh=["happy" , "good" , "Intellegent", "Smart", "Man", "Rsiky"]

print(harsh[0])

harsh[2]="Lucky" # Unlike strings lists can be mutable

print(harsh[2])
print(harsh)


print(harsh[0:5])

# Methods used in list

# To insert something at the end of the list use append

harsh.append("Handsome")

print(harsh)


# sort 

harsh.reverse()
print(harsh)


harsh.insert(3, "Hard")
print(harsh)


harsh.pop(3)
print(harsh)

harsh.remove("Lucky")
print(harsh)