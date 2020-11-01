
def main():
    print("Using midPoint_method")
    print(midPoint_method(test_function,100,(0.0,2.0)))

def test_function(x):
    return x**2

def midPoint_method(function,N,interval):
    # print(interval[0],interval[1])
    sum = 0
    for i in xrange(0,N):
        # print(i)
        h = float((interval[1]-interval[0])/N)
        # print("Value of H is ",h)
        leftPoint = interval[0] + (i * h)  
        rightPoint = interval[0] + ((i+1)*h) 
        midpoint = (leftPoint+rightPoint)/2
        # print("value of midPoint is ",midpoint)
        # print("value of funtion is :", function(midpoint) )
        sum += function(midpoint)*h
    return sum

def trapezoidal_method(funtion,N,interval):




if __name__ == "__main__":
    main()
