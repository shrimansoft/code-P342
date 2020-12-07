from lib.My_library import *   

def main():
    data = boundaryValueProblem(function,(0,1),(1,2*(2.71828-1)),100,5.0,0.02,0.0001)
    plt.plot(*zip(*data)[:2],label = "plot with given boundary conditions")
    plt.legend(loc=2)
    plt.show() # https://github.com/shrimansoft/code-P342/blob/master/Assignment_7/python/plots/Q3_plot.png
    with open("Assignment_7/python/Q3_data.txt","w") as writer:
        writer.write(str(data))



def function(x,y,z):
    return z+1 





if __name__ == "__main__":
    main()