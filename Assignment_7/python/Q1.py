import math as m 
from matplotlib import pyplot as plt
from lib.My_library import *


def main():
    data1 = eulerS_method(function1,(2,2.71828),0.5,100)
    data2 = eulerS_method(function2,(3,1),0.5,100)
    data3 = eulerS_method(function1,(2,2.71828),0.02,2500)
    data4 = eulerS_method(function2,(3,1),0.02,2500)

    with open("Assignment_7/python/Q1_data.txt","w") as writer:
        writer.write(str(data1))
        writer.write(str(data2))
        writer.write(str(data3))
        writer.write(str(data4))

    plt.plot(*zip(*data1),label="h=0.5")
    plt.plot(*zip(*data3),label="h=0.2")
    plt.legend(loc=2)
    plt.show()  # https://github.com/shrimansoft/code-P342/blob/master/Assignment_7/python/plots/Q1.1_plot.png
    plt.plot(*zip(*data2),label="h=0.5")
    plt.plot(*zip(*data4),label="h=0.2")
    plt.legend(loc=2) # https://github.com/shrimansoft/code-P342/blob/master/Assignment_7/python/plots/Q1.2_plot.png
    plt.show()



def function1(x,y):
    return (y*m.log(y))/x

def function2(x,y):
    return 6-((2*y)/x)

if __name__ == "__main__":
    main()