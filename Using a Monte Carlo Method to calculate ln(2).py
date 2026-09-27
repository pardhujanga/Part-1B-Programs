import random
import math
import matplotlib.pyplot as plt

iter = int(input("Enter the number of iterations you want to use to approimate. Use atleast 10000 iterations for consistent results upto 2 decimal places. "))

try: 
    int(iter)
except:
    print("Syntax error. Please try again with an integer")

N = int(iter)

#Array of iterations
iterations = []
#Array of results
results = []

points_in = 0 #We are counting the number of points below 1/x
for i in range(N):
    x = 1 + random.random() #As random.random() returns a number between 0 and 1
    y = random.random()

    cond = y - 1/x # condition to see if the random point is inside 1/x
    outcome = 1 if cond < 0 else 0
    points_in += outcome
    fraction_in = points_in/(i+1) # counts the points in the area under 1/x between 1 and 2. This is ln(2).

    #storing the results
    results.append(fraction_in)
    #Storing the iteration
    iterations.append(i+1)

#the last printed number is the closest approx of ln(2)
print("The value of ln(2) obtained is " + str(fraction_in))
print("The error in the obtained value is " + str(math.log(2) - fraction_in))

 # Plot the results using pyplot
fig = plt.figure()
plt.plot (iterations , results , label ="numerical ln(2)")
plt.plot ([0 , iterations [-1]] , [ math .log(2) , math . log(2) ], label =" ln(2)")

plt.grid(True)
plt.legend()
plt.ylabel("Result [-]")
plt.xlabel("Iteration [-]")
# plt.savefig("ln(2)Convergence.pdf")
plt.show()
