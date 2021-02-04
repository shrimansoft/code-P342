from matplotlib import pyplot as plt

import lib.My_library as my
import math as m

# given function in question    
def givenFunction(x,y,z): 
    g = 9.8
    return -g

# calling boundaryValue function from my lib . 
data = my.boundaryValueProblem(givenFunction,(0,2),(5,45),100,25,0.0002,0.1)
plt.scatter(*list(zip(*data))[:2])
plt.show()

print("Launch velocity is :",data[0][2],"m/s")

#----------Out put-------------

#('Launch velocity is :', 33.059166666666634, 'm/s')