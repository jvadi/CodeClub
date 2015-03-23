def isPrime(number):
    '''Returns True if number is prime, False otherwise'''
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:   
        for i in range(2, number//2+1):
            if number%i == 0:
                return False
        return True
        
#Test code    
for i in range(10):
    print(i, ":", isPrime(i))

    
