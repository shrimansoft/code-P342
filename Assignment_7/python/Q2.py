from lib.My_library import *


def main():
    data1 = RK4_method2(function1,(0,2,1),-0.05,100)[::-1] +  RK4_method2(function1,(0,2,1),0.05,100) 
    data2 = functionPloter(function2,0,-0.05,100)[::-1] +  functionPloter(function2,0,0.05,100)  

    plt.plot(*zip(*data2),label="plot of analytical solution")
    plt.plot(*zip(*data1)[:2],label="plot by RK4")
    plt.legend()
    plt.show() # https://github.com/shrimansoft/code-P342/blob/master/Assignment_7/python/plots/Q2_plot.png
    with open("Assignment_7/python/Q2_data.txt","w") as writer:
        writer.write(str(data1))



def function1(x,y,z):
    return 1-z-x

def function2(x):
    return 2*x - (x*x)/2 + m.exp(-x) + 1


if __name__ == "__main__":


    main()