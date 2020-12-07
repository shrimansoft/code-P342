from lib.My_library import *   

def main():
    # generating data 
    data = boundaryValueProblem(function,(0,1),(1,2*(2.71828-1)),100,5.0,0.02,0.0001)

    # Ploting data 
    plt.plot(*zip(*data)[:2],label = "plot with given boundary conditions")
    plt.legend(loc=2)
    plt.show() # https://github.com/shrimansoft/code-P342/blob/master/Assignment_7/python/plots/Q3_plot.png

    # Writing data in test file
    with open("Assignment_7/python/Q3_data.txt","w") as writer:
        writer.write(str(data))


# this is the equation given in Q3 where y'(x) = z
def function(x,y,z):
    return z+1 





if __name__ == "__main__":
    main()


# This code produce Plot and data. Plots are in Plot folder and data is stored in Q3_data.txt file.
# the console output is just for tracking the iteration. output is:
# 0.01
# ('GLow:', 1.0000000000000187)
# ('GHigh:', 5.0)
# ('Gnew:', 1.0016659407328548)
# ('fb3:', 3.436560000000003)
# ('fb0', 3.43656)