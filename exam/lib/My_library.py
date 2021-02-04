from matplotlib import pyplot as plt
import math as m 


# This function is exact in Implementation of bracketing as given in notes
def brackting(equation):
    print("---* Brackting *---")
    while True:
        guss = [0,0]
        print("Guss A and B such that A<B and f(A)*f(b)<0 also 0< Beta <2 for iteration ")
        guss[0] = float(input("Enter A : "))
        guss[1] = float(input("Enter B : "))
        beta = float(input("Enter Beta : "))
        if(guss[0]<guss[1] and beta<2 and beta>0):
            for i in range(1,14):
                print('Itration number %g Guss =(%f,%f)'%(i,guss[0],guss[1]))
                if(equation(guss[0])*equation(guss[1]) < 0 ):
                    print("Brackting is done (A,B)=(%f,%f)"%(guss[0],guss[1]))
                    return guss
                else:
                    if(equation(guss[0]) < equation(guss[1])) :
                        guss[0]-= beta * (guss[1]-guss[0])
                    else:
                        guss[1]+= beta * (guss[1]-guss[0])
            print("Iteration is going over 14 times guss again.")
        else:
            print("Conditions are not satisfied try again")



# this is function use synthetic division method. and call a helpler 
# function that use Laguerre's Algorithm.
def LaguerreRootOfPolynomial_method(polynomialAsList,h_forDeriv,epsilon,filename):
    roots =[]
    with open(filename,'w') as writer:
        for i in range(1,len(polynomialAsList)):
            writer.write("solving for "+str(i+1)+"st/ed/rd/th root\n")
            aRoot = aRootOfPolynomianl(polynomialAsList,h_forDeriv,epsilon,writer)
            roots.append(aRoot)
            temp=[polynomialAsList[0]]
            for i in polynomialAsList[1:]:
                temp.append(i+temp[-1]*aRoot)
            polynomialAsList = temp[:-1]
    print("Roots of the polynomial are ",roots," with error ",epsilon)

# This is hapler function of LaguerreRootOfPolynomial_method
def aRootOfPolynomianl(polynomialAsList,h_forDeriv,epsilon,writer):
    print("---* Root of Polynomials method *--")
    guss = float(input("Enter your Guss : "))
    if (polynomialsFromList(polynomialAsList)(guss) == 0):
        guss += 0.00001
    for i in range(1,200):
        firstDerivAtGussPoint = functionDeriv1(polynomialsFromList(polynomialAsList),guss,h_forDeriv)
        secondDerivAtGussPoint = functionDeriv2(polynomialsFromList(polynomialAsList),guss,h_forDeriv)
        valueAtGussPoint = polynomialsFromList(polynomialAsList)(guss)
        G = firstDerivAtGussPoint/valueAtGussPoint
        H = (G**2) - (secondDerivAtGussPoint/valueAtGussPoint)
        n = len(polynomialAsList)-1
        term = (n-1)*(n*H-(G**2))
        dinominater = ((G)+(m.sqrt(term))) if abs((G)+(m.sqrt(term)))>abs((G)-(m.sqrt(term))) else ((G)-(m.sqrt(term)))
        a = n/dinominater
        newGuss = guss - a
        writer.write(str(i)+" "+str(newGuss)+"\n")
        print(newGuss)
        if(abs(newGuss - guss)<epsilon):
            print("number of Itretion %d"%(i))
            print("root of the equation is ",newGuss, "with error ",epsilon," ." )
            return newGuss
        else:
            guss = newGuss
        



# This function generate a Polynomial function from given coeifficants as list.
def polynomialsFromList(list):
    def polynomial(value):
        result =0
        for i,c in enumerate(reversed(list)):
            # print(c,value,i)
            # print(c*(value**i))
            result += c*(value**i)
        return result
    return polynomial



# This function is the Exact implementation of Newton Raphson method as given in notes
def newtonRaphson_method(equation,h_forDeriv,epsilon,filename):
    print("--* Newton Raphson Method *--")
    guss = float(input("Enter your Guss : "))
    with open(filename,'w') as writer:
        for i in range(1,200):
            gussPointValue = equation(guss)
            gussPointDValue = functionDeriv1(equation,guss,h_forDeriv)
            newGuss = guss - (gussPointValue/gussPointDValue)
            writer.write(str(i)+" "+str(newGuss)+"\n")
            if (abs(guss-newGuss) < epsilon):
                print("number of Itretion %d"%(i))
                print("root of the equation is ",newGuss, "with error ",epsilon," ." )
                return newGuss 
            else:
                guss = newGuss
    print("Iteration is going over 200. The range is may be not less then epsilon")
    print("Last guss of this method is ",guss )
    return newGuss



#Secand Derivative of function
def functionDeriv2(equation,point,h):
    slop = (equation(point+h)+equation(point-h)-2*equation(point))/(h**2)
    return slop 

#First Derivative of function
def functionDeriv1(equation,point,h):
    slop = (equation(point+h)-equation(point))/(h)
    return slop 


# false Position method to find the root
def falsePosition_method(equation,bracktedGuss,epsilon,filename):
    print("--* False Position Method *--")
    with open(filename,'w') as writer:
        for i in range(1,200):
            writer.write(str(i)+" "+str(bracktedGuss[0])+" "+str(bracktedGuss[1])+"\n")
            if(bracktedGuss[1]-bracktedGuss[0]<epsilon):
                print("number of Itretion %d"%(i))
                print("root of the equation is between ",bracktedGuss[0]," and ",bracktedGuss[1],"  with epsilon ",epsilon," ." )
                return bracktedGuss
            else:
                c = (bracktedGuss[1]*equation(bracktedGuss[0])-bracktedGuss[0]*equation(bracktedGuss[1]))/(equation(bracktedGuss[0])-equation(bracktedGuss[1]))
                if(equation(c)*equation(bracktedGuss[0])<0):
                    bracktedGuss[1]= c
                else:
                    bracktedGuss[0]= c
    print("Iteration is going over 200. The range is may be not less then epsilon")
    print("root of the equation is between ",bracktedGuss[0]," and ",bracktedGuss[1],"  with epsilon ",epsilon," ." )
    return bracktedGuss



# This function is the Exact implementation of bisection method is as given in notes.
def bisection_method(equation,bracktedGuss,epsilon,filename):
    print("--* Bisection Method *--")
    with open(filename, 'w') as writer:
        for i in range(1,200):
            writer.write(str(i)+" "+str(bracktedGuss[0])+" "+str(bracktedGuss[1])+"\n")
            if(bracktedGuss[1]-bracktedGuss[0]<epsilon):
                print("number of Itretion %d"%(i))
                print("root of the equation is between ",bracktedGuss[0]," and ",bracktedGuss[1],"  with epsilon ",epsilon," ." )
                return bracktedGuss
            else:
                c = (bracktedGuss[0]+bracktedGuss[1])/2
                if(equation(c)*equation(bracktedGuss[0])<0):
                    bracktedGuss[1]= c
                else:
                    bracktedGuss[0]= c
    print("Iteration is going over 200. The range is may be not less then epsilon")
    print("root of the equation is between ",bracktedGuss[0]," and ",bracktedGuss[1],"  with epsilon ",epsilon," ." )
    return bracktedGuss



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

#---------------------* function Ploter *--------------------------------------------
# this function generate the data from given function to plot graph
def functionPloter(function,initValue,h,N):
    data = [] 
    for i in range(N):
        data.append((initValue+(h*i),function(initValue+(h*i))))
    return data


#--------------------* boundary Value Problem *-----------------------------------------
# This function will take a boundary Value Problem and Using the algorithm given in notes find the best plot.
def boundaryValueProblem(function,firstBoundaryCondition,secondBoundaryCondition,N,guess,guessVariation,tolerance):
    GLow = 0 
    GHigh = 0
    h = (secondBoundaryCondition[0]-firstBoundaryCondition[0])/(N+0.0)
    # print(h)
    fb0 = secondBoundaryCondition[1]
    fb1=RK4_method2(function,firstBoundaryCondition+(guess,),h,N)[-1][1]

    if (fb1 > fb0):
        GHigh = guess
        while(fb1 > fb0):
            # print(fb1)
            # print(fb0)
            #print("testPoint2")
            guess = guess - guessVariation
            fb1=RK4_method2(function,firstBoundaryCondition+(guess,),h,N)[-1][1]
        GLow = guess
    else:
        GLow = guess
        while(fb1 < fb0):
            #print("testPoint3")
            guess = guess + guessVariation
            fb1=RK4_method2(function,firstBoundaryCondition+(guess,),h,N)[-1][1]
        GHigh = guess
    # print("testPoint1")
    fb1 = RK4_method2(function,firstBoundaryCondition+(GLow,),h,N)[-1][1] 
    fb2 = RK4_method2(function,firstBoundaryCondition+(GHigh,),h,N)[-1][1] 

    Gnew = GLow + ((GHigh - GLow)/(fb2-fb1))*(fb0-fb1)
    fb3 = RK4_method2(function,firstBoundaryCondition+(Gnew,),h,N)[-1][1]  
    # print("GLow:",GLow)
    # print("GHigh:",GHigh)
    # print("Gnew:",Gnew)
    # print("fb3:",fb3)
    # print("fb0",fb0)
    # print("testPoint4")
    while(abs(fb3 - fb0) >  tolerance and   abs(fb3) < 100 ):
        if fb3 > fb0 :
            GHigh = Gnew
        else:
            GLow = Gnew

        fb1 = RK4_method2(function,firstBoundaryCondition+(GLow,),h,N)[-1][1] 
        fb2 = RK4_method2(function,firstBoundaryCondition+(GHigh,),h,N)[-1][1] 
        Gnew = GLow + ((GHigh - GLow)/(fb2-fb1))*(fb0-fb1)
        fb3 = RK4_method2(function,firstBoundaryCondition+(Gnew,),h,N)[-1][1]  
        # print("GLow:",GLow)
        # print("GHigh:",GHigh)
        # print("Gnew:",Gnew)
        # print("fb3:",fb3)
        # print("fb0",fb0)
        # print("testPoint4")
    data = RK4_method2(function,firstBoundaryCondition+(Gnew,),h,N) 

    return data 
        
    

# ----------------* euler's mathod *-----------------------------
# implamented as given in notes
def eulerS_method(function1,initValue,h,N):
    points=[initValue]

    for i in range(N):
        newPoint =(points[i][0]+h,points[i][1] + h*function1(*points[i]))
        points.append(newPoint)

    return points



# ------------------* Predictor Corrector Method *----------------------
# implamented as given in the notes
def predictor_corrector_method(function1,initValue,h,N):
    points=[initValue]
    for i in range(N):
        k1 = h*function1(*points[i])
        newPointP =(points[i][0]+h,points[i][1] + k1)
        k2 = h*function1(*newPointP)
        newPointC =(points[i][0]+h,points[i][1] + (k1+k2)/2)
        points.append(newPointC)
    return points
#-------------------* RK4 Method *-------------------------
# implament as given in the notes
def RK4_method(function1,initValue,h,N):
    points=[initValue]
    for i in range(N):
        (Y,X) = points[i]
        k1 = h*function1(X,Y)
        k2 = h*function1(X+(h/2),Y+(k1/2))
        k3 = h*function1(X+(h/2),Y+(k2/2))
        k4 = h*function1(X+h,Y+k3)
        newPoint =(X+h,Y + (k1+(2*k2)+(2*k3)+k4)/6)
        points.append(newPoint)
    return points
#-----------------* Rk4 for second order Method *------------------------
# this is not given in the notes. This is just a little modificaion of The Method given in the Notes
# here we are using k and l. where k are for the currection in value of f(x) and l are currection in values of f'(x). 
def RK4_method2(function2,initValue,h,N):
    points=[initValue]
    for i in range(N):
        (X,Y,Z) = points[i]

        l1 = h*function2(X,Y,Z)
        k1 = h*Z
        l2 = h*function2(X+(h/2),Y+(k1/2),Z+(l1/2))
        k2 = h*(Z+(l1/2))
        l3 = h*function2(X+(h/2),Y+(k2/2),Z+(l2/2))
        k3 = h*(Z+(l2/2))
        l4 = h*function2(X+h,Y+k3,Z+l3)
        k4 = h*(Z+(l3/2))
        newPoint =(X+h,Y + (k1+(2*k2)+(2*k3)+k4)/6, Z+ (l1+(2*l2)+(2*l3)+l4)/6 )
        points.append(newPoint)
    return points




if __name__ == "__main__":
    main()

