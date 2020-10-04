from lib.My_library import *
import math as m

def main():
    bracket = brackting(function)
    bisection_method(function,bracket,0.0001,"Assignment_5/python/Q1_a_data/bisection_data.txt")
    falsePosition_method(function,bracket,0.000001,"Assignment_5/python/Q1_a_data/falsePosition_data.txt")
    newtonRaphson_method(function,0.0000000001,0.000001,"Assignment_5/python/Q1_a_data/newtonRaphon_data.txt")

def function(x):
    return m.log(x)-m.sin(x)   


if __name__ == "__main__":
    main()

# code output
# ---* Brackting *---
# Guss A and B such that A<B and f(A)*f(b)<0 also 0< Beta <2 for iteration 
# Enter A : 1.5
# Enter B : 2.5
# Enter Beta : 0.7
# Itration number 1 Guss =(1.500000,2.500000)
# Brackting is done (A,B)=(1.500000,2.500000)
# --* Bisection Method *--
# number of Itretion 15
# root of the equation is between  2.21905517578125  and  2.2191162109375   with epsilon  0.0001  .
# --* False Position Method *--
# Iteration is going over 200. The range is may be not less then epsilon
# root of the equation is between  2.219107148913746  and  2.2191162109375   with epsilon  1e-06  .
# --* Newton Raphson Method *--
# Enter your Guss : 1.5
# number of Itretion 5
# root of the equation is  2.219107148913747 with error  1e-06  .