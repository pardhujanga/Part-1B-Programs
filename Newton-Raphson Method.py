#A program to calculate the nth roots of n to extremly high precision using Newton-Raphson Method

input = input("Enter an integer 'n' between 1 and 100 to find it's nth root: ") #asking the user for an input
try: # to account for user error and let them know to type an integer
    type(input) == int
    n = int(input)
except:
    print("Sorry but this can only compute the nth root of an integer.So please try again with an integer")

def f(x): #defining the function whose zero we want to find. The zero is the nth root we need
    return n - x**n
def df(x):#defining the derivative as python can't calculate derivatives. (What a shame!)
    return -n*x**(n-1)

def nth(x):
    p = 1 #this will hold the final result we get. Also, this is the initial guess.
      #As nth roots are very close to 1 as n increases, 1 is a good guess

    iterations = int((x/1.5) + 5) # we vary the number of iterations for efficiency at various inputs.
                              # The 1.5 factor was chosen by trial and error such that 100 works.
                              #the 5 is to avoid the iterations being too low for small numbers.
    for i in range(iterations): #implementing Newton-Raphson
        p -= f(p)/df(p)

    return p

answer = nth(n)
final_error = n - nth(n)**n # this is the error we have after the run is over
print(f"The value of {n}th root of {n} obtained is {nth(n)}") #letting the user know the result
print(f"The error between {n} and the result to the power of {n} is {final_error}")

