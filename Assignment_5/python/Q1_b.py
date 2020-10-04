from lib.My_library import *
import math as m

def main():
    bracket = brackting(function)
    bisection_method(function,bracket,0.0001,"Assignment_5/python/Q1_b_data/bisection_data.txt")
    falsePosition_method(function,bracket,0.000001,"Assignment_5/python/Q1_b_data/falsePosition_data.txt")
    newtonRaphson_method(function,0.0000000001,0.000001,"Assignment_5/python/Q1_b_data/newtonRaphon_data.txt")

def function(x):
    return -m.cos(x)-x  

if __name__ == "__main__":
    main()


# code output
# ---* Brackting *---
# Guss A and B such that A<B and f(A)*f(b)<0 also 0< Beta <2 for iteration 
# Enter A : -2
# Enter B : 2
# Enter Beta : 0.7
# Itration number 1 Guss =(-2.000000,2.000000)
# Brackting is done (A,B)=(-2.000000,2.000000)
# --* Bisection Method *--
# number of Itretion 17
# root of the equation is between  -0.7391357421875  and  -0.73907470703125   with epsilon  0.0001  .
# --* False Position Method *--
# number of Itretion 4
# root of the equation is between  -0.7390851332151607  and  -0.7390851332151593   with epsilon  1e-06  .
# --* Newton Raphson Method *--
# Enter your Guss : -1
# number of Itretion 4
# root of the equation is  -0.7390851332151607 with error  1e-06  .