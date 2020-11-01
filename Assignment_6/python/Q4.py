from lib.My_library import * 


def main():
    with open("Assignment_6/python/Q4_data/data.txt",'w') as writer:
        interval = [0.0,1.0]
        writer.write("N \t monteCarlo \n") 
        print("N \t monteCarlo ")
        # Integrating using Monte Carlo method for different values of N
        for N in [10,100,1000,10000,100000,1000000,10000000]:
            monteCarlo_integral = monteCarlo_method(function,N,interval)
            # Writing the output in a text file
            writer.write(str(N)+"\t"+str(monteCarlo_integral)+"\n")
            print(str(N)+"\t"+str(monteCarlo_integral))


def function(x):
    return 4/(1+(x**2)) 

if __name__ == "__main__":
    main()

# output 
# N        monteCarlo 
# 10      3.41026101839
# 100     3.14287219211
# 1000    3.15765475576
# 10000   3.14031147025
# 100000  3.13918907625
# 1000000 3.14099554076
# 10000000        3.1413849302

