consequetive = None
multiplier = None
lastEntry = None

#This is not a good bit of code - lots of imbedded if statements
while True:
    entry = int(input("Enter a number, -1 to exit"))
    if entry == -1:
        break
    elif lastEntry:
        if consequetive and (multiplier * (entry - lastEntry) != 1):
            consequetive = False
        elif multiplier == None:
            multiplier = entry - lastEntry
            if (abs(multiplier) != 1):
                consequetive = False
            else:
                consequetive = True
    lastEntry = entry
    
#Test code
print(consequetive)
    

        
    
                
