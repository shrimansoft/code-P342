from lib.My_library import * 


def main():
    with open("Assignment_6/python/Q2_data/data.txt",'w') as writer:
        interval = [1.0,3.0]
        print("N \t midpoint \t trapezoidal \t simpson ")
        # Integrating the given function using all the three techniques and different values of N
        for N in [5,10,25,30,50]:
            midpoint_integral = midPoint_method(function,N,interval)
            simpson_integral = simpson_method(function,N,interval)
            trapezoidal_integral = trapezoidal_method(function,N,interval)
            # Writing the data in a text file
            writer.write(str(N)+" "+str(midpoint_integral)+" "+str(trapezoidal_integral)+" "+str(simpson_integral)+"\n")
            print(str(N)+"\t"+str(midpoint_integral)+"\t"+str(trapezoidal_integral)+"\t"+str(simpson_integral))



def function(x):
    return x/(1+x)

if __name__ == "__main__":
    main()

# Output 
# N        midpoint        trapezoidal     simpson 
# 5       1.30809211428   1.30436507937   1.20846560847
# 10      1.30716463959   1.30622859682   1.30684976931
# 25      1.30690280196   1.30675283942   1.2869193931
# 30      1.30688753323   1.30678338464   1.30685278097
# 50      1.30686531835   1.30682782069   1.30685281445