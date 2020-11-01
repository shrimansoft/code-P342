from lib.My_library import * 
import math as m


def main():
    with open("Assignment_6/python/Q3_data/data.txt",'w') as writer:
        interval = [0.0,1.0]
        analytical_value = 0.746824132812 
        print("\t midpoint \t trapezoidal \t simpson \t ")
        # Integrating the given function using all three techniques.
        # I choose the value of N to get maximum error of 0.001
        midpoint_integral = midPoint_method(function,100,interval)
        simpson_integral = simpson_method(function,100,interval)
        trapezoidal_integral = trapezoidal_method(function,20,interval)
        # Writing the data in a text file
        writer.write(str(midpoint_integral)+" "+str(trapezoidal_integral)+" "+str(simpson_integral)+"\n")
        print("value: \t" + str(midpoint_integral)+"\t"+str(trapezoidal_integral)+"\t"+str(simpson_integral))
        

        # Calculating the error in each method
        midpoint_error =  abs(midpoint_integral-analytical_value)
        trapezoidal_error = abs(trapezoidal_integral-analytical_value)
        simpson_error = abs(simpson_integral-analytical_value)
        print("error: \t" + str(midpoint_error)+"\t"+str(trapezoidal_error)+"\t"+str(simpson_error))

def function(x):
    return m.exp(-(x**2)) 

if __name__ == "__main__":
    main()

# Output 
#          midpoint        trapezoidal     simpson         
# value:  0.746827198492  0.74667083694   0.746824132894
# error:  3.06568031971e-06       0.000153295872127       8.21761547698e-11