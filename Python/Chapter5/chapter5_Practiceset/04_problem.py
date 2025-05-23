s=set()

s.add(20)
s.add(20.0)
s.add("20")

print(len(s))


# Actually it seems 20 is integer and 20.0 is float point 
# number its true but value of 20.00 is 20  and sets cannot repeat values
# if we add 20.83 or some integer after a point then itsvalues get different
