# breaking loop leaving all the conditions 

for i in range(100):
    if (i==35):
        break # This will break the loop  if the condition is true  
    print(i)
    
# skiping the iterations anf cotinuing further

for i in range(100):
    if (i==35):
        continue # This will not break the loop  if the condition is true but this will not
                #  print 35 and cotinue the loop 
    print(i)

