import random

# this function is just for test  
def main():
    print("Using midPoint_method")
    print(midPoint_method(test_function,100,(0.0,2.0)))
    print(trapezoidal_method(test_function,100,(0.0,2.0)))
    print(simpson_method(test_function,100,(0.0,2.0)))
    print(monteCarlo_method(test_function,100000,(0.0,2.0)))

def test_function(x):
    return x**2


#  Integration using midpoint theorem, Algorithm is implemented as given in the notes.
def midPoint_method(function,N,interval):
    # print(interval[0],interval[1])
    sum = 0.0   
    h = float((interval[1]-interval[0])/N)
    for i in range(0,N):
        # print(i)
        # print("Value of H is ",h)
        leftPoint = interval[0] + (i * h)  
        rightPoint = interval[0] + ((i+1)*h) 
        midpoint = (leftPoint+rightPoint)/2
        # print("value of midPoint is ",midpoint)
        # print("value of function is :", function(midpoint) )
        sum += function(midpoint)*h
    return sum
# Integration technique using trapezoidal method. algorithm is implemented as given in notes.
def trapezoidal_method(function,N,interval):
    sum = 0.0
    h = float((interval[1]-interval[0])/N)

    def weight_function(x,N):           # weight function defined inside trapezoidal method function
        return (1.0 if ((x is N)or(x is 0)) else 2.0)

    for i in range(0,N+1):        
        points = interval[0] + (i*h)
        sum += function(points)* (h/2) * weight_function(i,N)
    return sum

# Integration technique implemented using Simpson method. Algorithm is implemented as given in notes.
# N should be even
def simpson_method(function,N,interval):
    sum = 0.0
    h = float((interval[1]-interval[0])/N)

    def weight_function(x,N):  #Weight function defined inside simpson method function
        return (1.0 if ((x is N)or(x is 0)) else 4.0 if (x % 2 is 1) else 2.0)

    for i in range(0,N+1):
        # print(weight_function(i,N))
        points = interval[0] + (i*h)
        sum += (h/3) * weight_function(i,N) * function(points)
    return sum


# Integration technique using Monte Carlo method. Algorithm is implemented as given in notes.
def monteCarlo_method(function,N,interval):

    h = float((interval[1]-interval[0])/N)
    sum = 0.0
    for i in range(0,N):
        X = random.uniform(*interval) # Random values taking in the given interval
        sum += h * function(X)

    return sum 












if __name__ == "__main__":
    main()

