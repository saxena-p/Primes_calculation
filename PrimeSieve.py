import math

def primesUptoN(n):
    """ Returns a list of prime numbers upto the integer n. 
    An implementation of the sieve of Eratosthenes algorithm"""
    maxindex = (n-1)//2 + 1
    # First we create a boolean array of True.
    # We will modify this array such that prime = True and composite = False
    labels = [True for i in range(maxindex)]
    labels[0] = False

    # Now loop over 3 to n/2. Since i = (n-1)/2, we choose the index range accordingly
    idx = 1
    while (idx < (maxindex/2 - 1)//2 +1):
        # For each index, look at the prime number at that index.
        # Mark all the multiples of that prime number as False.
        prime = 2*idx + 1
        idx2 = idx+prime
        while idx2< maxindex:
            labels[idx2] = False
            idx2 += prime
        
        # Now we increment the idx until the point we hit another true
        while (labels[idx+1]==False):
            idx +=1
        idx+=1
    
    primeList = [2]
    for index, value in enumerate(labels):
        if (value):
            primeList.append(2*index+1)

    return primeList

def isPrime(numberToCheck):
    "Checks whether a given number N is prime. Returns True or False"
    # We use three main principles here
    # 1. All prime numbers greater than 2 are odd.
    # 2. All primes greater than 3 can be written as 6k+1 or 6k-1
    # 3. Any number can have only one prime factor greater than sqrt(N)

    if numberToCheck <=1: # 1 is not prime. We don't want negative numbers
        return False
    elif numberToCheck%1 != 0: # We only want to test integers
        return False
    elif numberToCheck < 4: # 2 and 3 are prime numbers
        return True
    elif numberToCheck %2 ==0: # remove all the even numbers
        return False
    elif numberToCheck < 9: # 5, 7 are primes.
        return True
    elif numberToCheck % 3 == 0: # numbers divisible by 3
        return False
    else:
        divisor = 5
        while (divisor <= math.floor(math.sqrt(numberToCheck))):
            if numberToCheck% divisor == 0:
                return False
            if numberToCheck% (divisor+2) == 0:
                return False
            divisor +=6
        return True

    return True

def nthPrime(N):
    "Returns the Nth prime number. The first prime number is 2."
    # One implementation is by checking numbers sequentially if they are prime or not.

    if N==1:
        return 2
    elif N==2:
        return 3
    
    count = 2
    numtocheck = 3
    while count < N: # we stop when count = N
        numtocheck += 2
        if isPrime(numtocheck):
            count += 1
            # At this point count'th prime is numtocheck
    
    return numtocheck

def nthPrime2(N):
    ''' This is another implementation for finding the nth prime.
    Probably a little faster than the previous one.
    We use a result that for n>6, there is an upper bound on the prime number p_n.
    p_n < n log(n) + n log(log(n))'''
    upper_bound = N* math.log(N) + N* math.log( math.log(N))
    primelist = primesUptoN (math.ceil(upper_bound))
    return primelist[N-1]