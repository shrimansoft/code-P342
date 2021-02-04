from matplotlib import pyplot as plt
import lib.My_library as my


def givenEquation(x):
    return (x-5)*((2.71828)**x)+5


def defOf_b(k,h,c,x):
    return (h*c)/(k*x)


h = 6.626E-34
k = 1.381E-23
c = 3E8

# this function ask for guss.take between 4 and 6 
x = my.newtonRaphson_method(givenEquation,0.0000000001,0.0000001,"./Q1_data.txt")

b = defOf_b(k,h,c,x)

print("value of b is: ",b)


#-------------- output is ------------
# --* Newton Raphson Method *--
# Enter your Guss : 5
# number of Itretion 4
# ('root of the equation is ', 4.965114111021147, 'with error ', 1e-07, ' .')
# ('value of b is: ', 0.002899010401225615)