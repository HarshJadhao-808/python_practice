# sets are also enclosed by { } 

# For an empty set 

a=set() #Its an empty set

b={} # This will make an empty dictionary


print(type(a))

print(type(b))


#  Elements in set cannot be repeated


# Properties of sets 

# 1) Sets cannot be duplicated
# 2) Sets cannot be indexed
# 3) There is no way to change element in the set


# Operations in sets

c={ 3, 53, 34 , 2312, 12 }

d={3,53, 345 , 52345 ,321134 ,12}

# print(c)

# print(c.pop()) # Removes and prints a random value from the set

# print(c)

e=c.union(d)

print(e)

f=c.intersection(d)

print(f)


  