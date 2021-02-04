import lib.My_library as my
import math as m

def givenFunction(thita):
    L = 1
    g = 9.8
    thitaM = m.pi/4
    return 4*(m.sqrt(L/g))*(1/(2*(m.sqrt(m.sin(thitaM/2)**2 - m.sin(thita/2)**2))))


T = my.simpson_method(givenFunction,10,(0,m.pi/4.001))

print("Time Period of oscilation is " , T, "s")

#----------Out put -------------

# ('Time Period of oscilation is ', 3.7140730452388553, 's')