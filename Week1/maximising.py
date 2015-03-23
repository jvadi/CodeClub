maximum = 0
entry = 0

while entry != -1:
    entry = int(input("Enter a number, -1 to exit"))
    if entry > maximum:
        maximum = entry

print(maximum)
                      
