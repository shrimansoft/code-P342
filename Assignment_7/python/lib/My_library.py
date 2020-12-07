from matplotlib import pyplot as plt
import math as m 



# this function1 is just for test  
def main():

    # data1 =RK4_method(test_function1,(2,2.71828),0.5,100)
    # data = RK4_method2(test_function2,(0,2,1),-0.05,100)[::-1] +  RK4_method2(test_function2,(0,2,1),0.05,100) 
    # data3 = functionPloter(test_function3,0,-0.05,100)[::-1] +  functionPloter(test_function3,0,0.05,100)  

    # print(zip(*data))
    # plt.plot(*zip(*data3))
    # plt.plot(*zip(*data)[:2])
    # plt.show()

    data = boundaryValueProblem(test_function4,(0,1),(1,2*(2.71828-1)),100,5.0,0.02,0.0001)
    plt.plot(*zip(*data)[:2])
    plt.show()



#-------------------------* bunch of test function *--------------------------------------------
def test_function4(x,y,z):
    return z+1 
def test_function3(x):
    return 2*x - (x*x)/2 + m.exp(-x) +1

def test_function1(x,y):
    return (y*m.log(y))/x

def test_function2(x,y,z):
    return 1-z-x


#---------------------* function Ploter *--------------------------------------------
# this function generate the data from given function to plot graph
def functionPloter(function,initValue,h,N):
    data = [] 
    for i in range(N):
        data.append((initValue+(h*i),function(initValue+(h*i))))
    return data


#--------------------* boundary Value Problem *-----------------------------------------
# This function will take a boundary Value Problem and Using the algorithm given in notes find the best plot.
def boundaryValueProblem(function,firstBoundaryCondition,secondBoundaryCondition,N,guess,guessVariation,tolerance):

    h = (secondBoundaryCondition[0]-firstBoundaryCondition[0])/(N+0.0)
    print(h)
    GLow = 0 
    GHigh = 0
    fb0 = secondBoundaryCondition[1]
    fb1=RK4_method2(function,firstBoundaryCondition+(guess,),h,N)[-1][1]

    if (fb1 > fb0):
        GHigh = guess
        while(fb1 > fb0):
            # print(fb1)
            # print(fb0)
            # print("testPoint2")
            guess = guess - guessVariation
            fb1=RK4_method2(function,firstBoundaryCondition+(guess,),h,N)[-1][1]
        GLow = guess
    else:
        GLow = guess
        while(fb1 < fb0):
            # print("testPoint3")
            guess = guess + guessVariation
            fb1=RK4_method2(function,firstBoundaryCondition+(guess,),h,N)[-1][1]
        GHigh = guess
    # print("testPoint1")
    fb1 = RK4_method2(function,firstBoundaryCondition+(GLow,),h,N)[-1][1] 
    fb2 = RK4_method2(function,firstBoundaryCondition+(GHigh,),h,N)[-1][1] 

    Gnew = GLow + ((GHigh - GLow)/(fb2-fb1))*(fb0-fb1)
    fb3 = RK4_method2(function,firstBoundaryCondition+(Gnew,),h,N)[-1][1]  
    print("GLow:",GLow)
    print("GHigh:",GHigh)
    print("Gnew:",Gnew)
    print("fb3:",fb3)
    print("fb0",fb0)
    # print("testPoint4")
    while(abs(fb3 - fb0) >  tolerance and   abs(fb3) < 100 ):
        if fb3 > fb0 :
            GHigh = Gnew
        else:
            GLow = Gnew

        fb1 = RK4_method2(function,firstBoundaryCondition+(GLow,),h,N)[-1][1] 
        fb2 = RK4_method2(function,firstBoundaryCondition+(GHigh,),h,N)[-1][1] 
        Gnew = GLow + ((GHigh - GLow)/(fb2-fb1))*(fb0-fb1)
        fb3 = RK4_method2(function,firstBoundaryCondition+(Gnew,),h,N)[-1][1]  
        print("GLow:",GLow)
        print("GHigh:",GHigh)
        print("Gnew:",Gnew)
        print("fb3:",fb3)
        print("fb0",fb0)
        # print("testPoint4")
    data = RK4_method2(function,firstBoundaryCondition+(Gnew,),h,N) 

    return data 
        
    

# ----------------* euler's mathod *-----------------------------
# implamented as given in notes
def eulerS_method(function1,initValue,h,N):
    points=[initValue]

    for i in range(N):
        newPoint =(points[i][0]+h,points[i][1] + h*function1(*points[i]))
        points.append(newPoint)

    return points



# ------------------* Predictor Corrector Method *----------------------
# implamented as given in the notes
def predictor_corrector_method(function1,initValue,h,N):
    points=[initValue]
    for i in range(N):
        k1 = h*function1(*points[i])
        newPointP =(points[i][0]+h,points[i][1] + k1)
        k2 = h*function1(*newPointP)
        newPointC =(points[i][0]+h,points[i][1] + (k1+k2)/2)
        points.append(newPointC)
    return points
#-------------------* RK4 Method *-------------------------
# implament as given in the notes
def RK4_method(function1,initValue,h,N):
    points=[initValue]
    for i in range(N):
        (Y,X) = points[i]
        k1 = h*function1(X,Y)
        k2 = h*function1(X+(h/2),Y+(k1/2))
        k3 = h*function1(X+(h/2),Y+(k2/2))
        k4 = h*function1(X+h,Y+k3)
        newPoint =(X+h,Y + (k1+(2*k2)+(2*k3)+k4)/6)
        points.append(newPoint)
    return points
#-----------------* Rk4 for second order Method *------------------------
# this is not given in the notes. This is just a little modificaion of The Method given in the Notes
# here we are using k and l. where k are for the currection in value of f(x) and l are currection in values of f'(x). 
def RK4_method2(function2,initValue,h,N):
    points=[initValue]
    for i in range(N):
        (X,Y,Z) = points[i]

        l1 = h*function2(X,Y,Z)
        k1 = h*Z
        l2 = h*function2(X+(h/2),Y+(k1/2),Z+(l1/2))
        k2 = h*(Z+(l1/2))
        l3 = h*function2(X+(h/2),Y+(k2/2),Z+(l2/2))
        k3 = h*(Z+(l2/2))
        l4 = h*function2(X+h,Y+k3,Z+l3)
        k4 = h*(Z+(l3/2))
        newPoint =(X+h,Y + (k1+(2*k2)+(2*k3)+k4)/6, Z+ (l1+(2*l2)+(2*l3)+l4)/6 )
        points.append(newPoint)
    return points

if __name__ == "__main__":
    main()

