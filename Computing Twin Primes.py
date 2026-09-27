#Computing Twin primes

#taking input from user
limit = input("Enter the number of pairs of twin primes which you want to find: ")

#accounting for user error in input
try: 
    int(limit)
except:
    print("Syntax error. Please try again with an integer")

#defining the list of twin primes as it can't be intiated in the while loop
TwinPrimes = []

#I start out with 2 as a prime as 1 divides everything and the algorithm dose't catch that
n=3
primes= [2]
#This is to remember the length of the primes list after every iteration of the loop
n0 = 0

while len(TwinPrimes) < int(limit): #while loop stops when we have enough pairs of twin primes

    n0 = len(primes)
    counter=0 #this is the divisiblity counter. Keeps track of number of prime factors.
    for i in primes:#Only check divisiblity by primes to be efficient
        if n%i==0:
            counter+=1
    if counter==0: #if the counter is 0, then there are no prime factors other than itself. So, we have a prime number
        primes.append(n) 
    n+=1 #taking the count forward to test the next number
    
    if len(primes) > n0: # check the twin prime condition again only if a new prime was added
        if primes[n0]-primes[n0-1] == 2:
            TwinPrimes.append((primes[n0-1],primes[n0]))


print("This is the list of the first "  + limit + " Twin Primes:")
print(TwinPrimes)

