# In this library I choose the variable name meaningful
# as given in algorithm to make the code readable.

import math as m


# This function is to test this lib
def mainForTest():
    print("test")
    # bracketedPoints = brackting(equation) 
    # print(bracketedPoints)
    # bisection_method(equation,bracketedPoints,0.0001)
    # falsePosition_method(equation,bracketedPoints,0.000001)
    # newtonRaphson_method(equation,0.0000000001,0.0000001)
    # aRootOfPolynomianls([1,-4,4],0.00001,0.000001)
    # LaguerreRootOfPolynomial_method([1,-3,-7,27,-18],0.00001,0.000001)




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







# just for test
def equation(x):
    return m.sin(x)

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












if __name__ == "__main__":
    mainForTest()