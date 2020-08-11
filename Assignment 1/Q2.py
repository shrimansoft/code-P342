

#----------------------* main function *----------------------------------  
def main():
    print( " Factorail of 10 is : " )           #Some sample testing of function Factorial. 
    print( Factorial(10) )
    print( " Factorail of 15 is : " )
    print( Factorial(15) )
    print( " Factorail of 5 is  : " )
    print( Factorial(5) )
    print( " Factorail of -5 is : " )
    print( Factorial(-5) )



#------------------------* Factorial function *----------------------------
def Factorial(num):
    if (num < 0):                            # It will check whether number is negative or not.If it is the negative then it will return nan.
        return float("nan")
    coutn =1
    for i in range(1,num+1):
        coutn*=i
    return coutn

#-------------------------* If this program is running as a __main__ then it execute the main function *----------------
if __name__=="__main__":
    main()