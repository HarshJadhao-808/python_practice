# dictionary


Marks={
    "Harsh":100,
    "Shalmon":24,
    "Shakyaveer":23,
}


print(Marks ["Harsh"])


# It is mutable
# It is unordered
# It is indexed
# Cannot contain duplicate keys


print(Marks.items()) #Prints all items inside a container 

print(Marks.keys()) # Prints only keys

print(Marks.values()) # prints only corresponding values of keys

# print(Marks.get("Harsh2")) # This shows none

# print(Marks["Harsh2"]) # This shows error

# print(Marks.pop["Shalmon"])

Marks.setdefault( "Not in the list")

print(Marks ["Jason"])

print(Marks)