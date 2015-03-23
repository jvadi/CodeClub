def naiveSort(number1, number2, number3):
    '''Returns 3 numbers in order from highest to lowest'''
    highest = max(number1, number2, number3)
    lowest = min(number1,number2, number3)
    middle = max(min(number1, number2),
                 min(number2, number3),
                 min(number1, number3))
    return highest, middle, lowest

#Test code
print(naiveSort(1,2,3))
print(naiveSort(1,3,2))
print(naiveSort(3,2,1))
print(naiveSort(3,1,2))
print(naiveSort(2,3,1))
print(naiveSort(2,1,3))
