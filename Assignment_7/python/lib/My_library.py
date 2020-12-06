from matplotlib import pyplot as plt
import math as m 



# this function1 is just for test  
def main():
    data =RK4_method(test_function2,(2,2.71828),0.5,100)
    print(zip(*data))
    plt.plot(*zip(*data))
    plt.show()

def test_function1(x,y):
    return (y*m.log(y))/x
def test_function2(x,y):
    return 6-((2*y)/x)

def eulerS_method(function1,initValue,h,N):
    points=[initValue]
    for i in range(N):
        newPoint =(points[i][0]+h,points[i][1] + h*function1(*points[i]))
        points.append(newPoint)

    return points

def predictor_corrector_method(function1,initValue,h,N):
    points=[initValue]
    for i in range(N):
        k1 = h*function1(*points[i])
        newPointP =(points[i][0]+h,points[i][1] + k1)
        k2 = h*function1(*newPointP)
        newPointC =(points[i][0]+h,points[i][1] + (k1+k2)/2)
        points.append(newPointC)
    return points

def RK4_method(function1,initValue,h,N):
    points=[initValue]
    for i in range(N):
        (Y,X) = points[i]
        k1 = h*function1(X,Y)
        k2 = h*function1(X+(h/2),Y+(k1/2))
        k3 = h*function1(X+(h/2),Y+(k2/2))
        k4 = h*function1(X+h,Y+k3))
        newPoint =(X+h,Y + (k1+(2*k2)+(2*k3)+k4)/6)
        points.append(newPoint)
    return points




def RK4_method(function2,initValue,h,N):
    points=[initValue]
    for i in range(N):
        (Y2,Y1,X) = points[i]


        k1 = h*function2(X,Y)
        k2 = h*function2(X+(h/2),Y+(k1/2))
        k3 = h*function2(X+(h/2),Y+(k2/2))
        k4 = h*function2(X+h,Y+k3))
        newPoint =(X+h,Y + (k1+(2*k2)+(2*k3)+k4)/6)
        points.append(newPoint)
    return points

if __name__ == "__main__":
    main()

