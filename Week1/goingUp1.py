consequetive = True
lastEntry = None

while True:
    entry = int(input("Enter a number, -1 to exit"))
    if entry == -1:
        break
    elif lastEntry and consequetive:
        if entry - lastEntry != 1:
            consequetive = False
    lastEntry = entry
print(consequetive)
        

        
    
                
