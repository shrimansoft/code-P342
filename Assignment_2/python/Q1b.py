#-------------------* main function *------------------------------
# this function to run tests
def main():
    points = [] # a empty list to store the gitd 
    setPoints(points) # there we call setPoints() which make the 6x6 gird of unit distance.
    print(points) # print the gird using normal print function but points are Readable. 
    print(" Average distance between points is : ", averageDistance(points),"\n") #here we call the averageDistance function and print its output.

#-----------------------* setPoints function *-------------------------------
# this function make 6x6 gide of unit distance.
def setPoints(points):
    for i in range(1,7):
        for j in range(1,7):
            point = [i,j]
            points.append(point)

#-------------------------* averageDistance function *---------------------------   
# this function calculate the average distance between the points of 6x6 grid.
def averageDistance(points):
    count = 0.0 # a variable to store the sum of the distance.
    for point_set in points: # fixing one point
        for point_take in points: # runing over all the points including the fixed point.
            count+= (abs(point_set[0]-point_take[0])+abs(point_set[1]-point_take[1])) # adding the abs distance between the points to count.
    return count/(36*36) # returning the average distance between points along the grid.


# this to run the main function.
if __name__ == "__main__":
    main()

#--------------------------------* output of this code *------------------------
# [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6]]
# (' Average distance between points is : ', 3.888888888888889, '\n')