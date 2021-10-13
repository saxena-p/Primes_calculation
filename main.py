# Use this file to run the program
import PrimeSieve as ps

# To calculate all the prime numbers upto a number largeNum:
largeNum = 2000000
primelist = ps.primesUptoN(largeNum)
print("There are ", len(primelist), "prime numbers upto ", largeNum)
print("The largest prime number less than ", largeNum, "is ", primelist[-1])


# To check if the number N is prime
N = primelist[-1] # Just choose a prime number from the previous step
value = ps.isPrime(N)
if value:
    print(N, "is a prime number.")
else:
    print(N, "is not a prime number.")

N += 2
value = ps.isPrime(N)
if value:
    print(N, "is a prime number.")
else:
    print(N, "is not a prime number.")


# To calculate the Nth prime number, there are two functions:
N = 10001
prime = ps.nthPrime(N)
print("The ", N, "th prime number is ", prime)

prime = ps.nthPrime2(N)
print("The ", N, "th prime number is ", prime)
