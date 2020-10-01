
#--------------------* main function to run some test *------------------------
def main():
    points1 = [1,2,3,4,5,6]  # A list variable to store list of points.
    print("Average distance between points [1,2,3,4,5,6] is " ,averageDistance(points1))
    points2 = [3,4,5,6,7,8]  # another list of points.
    print("Average distance between points [3,4,5,6,7,8] is " ,averageDistance(points2))
    


#-------------------* arvearge distance function *---------------------------
# this function take a array of 6 points and return average distance.
def averageDistance(numArray):
    sum =0.0    # variable to store sum of distance between points.
    for i in range(0,6): # fixing one point.    
        for j in range(0,6): # runing over the points. 
            sum += abs(numArray[i] - numArray[j]) # adding abs value of difference between points.
    return (sum/36) # returning the average by dividing 36.


# -----------------------* Output of this code *-----------------------------
#('Average distance between points [1,2,3,4,5,6] is ', 1.9444444444444444)
#('Average distance between points [3,4,5,6,7,8] is ', 1.9444444444444444)




















if __name__ == "__main__":
    main()