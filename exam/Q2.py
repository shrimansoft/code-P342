import lib.My_library as my
import math as m

# this is the given formula
def givenFunction(thita):
    L = 1
    g = 9.8
    thitaM = m.pi/4
    return 4*(m.sqrt(L/g))*(1/m.sqrt(1-((m.sin(thitaM/2)**2)*(m.sin(thita)**2))))


# applying the simpson integration technique 
T = my.simpson_method(givenFunction,10,(0,m.pi/2))

print("Time Period of oscilation is "+ str(T)+"s")

#----------Out put -------------

# Time Period of oscilation is 2.08732001748s