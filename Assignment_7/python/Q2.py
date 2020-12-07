from lib.My_library import *


def main():
    # Generating data 
    data1 = RK4_method2(function1,(0,2,1),-0.05,100)[::-1] +  RK4_method2(function1,(0,2,1),0.05,100) 
    data2 = functionPloter(function2,0,-0.05,100)[::-1] +  functionPloter(function2,0,0.05,100)  

    # Ploting data
    plt.plot(*zip(*data2),label="plot of analytical solution")
    plt.plot(*zip(*data1)[:2],label="plot by RK4")
    plt.legend()
    plt.show() # https://github.com/shrimansoft/code-P342/blob/master/Assignment_7/python/plots/Q2_plot.png

    # Writing data in a text file
    with open("Assignment_7/python/Q2_data.txt","w") as writer:
        writer.write(str(data1))


# This is the function given in the Q2 where y'(x)=z
def function1(x,y,z):
    return 1-z-x
# This is the analytical solution where c_1 = 1 and c_2 = 1 
def function2(x):
    return 2*x - (x*x)/2 + m.exp(-x) + 1


if __name__ == "__main__":


    main()


# Output 
# This code produce Plot and data. Plots are in Plot folder and data is stored in Q2_data.txt file.