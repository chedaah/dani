import numpy 

def is_prime(n):
    for i in range(n):
        if n % i == 0:
            return False
    return True