def main():
    points = []
    setPoints(points)
    print(points)

    print(" Average distance between points is : ", averageDistance(points),"\n")


def setPoints(points):
    for i in range(1,7):
        for j in range(1,7):
            point = [i,j]
            points.append(point)


def averageDistance(points):
    count = 0.0
    for point_set in points:
        for point_take in points:
            count+= (abs(point_set[0]-point_take[0])+abs(point_set[1]-point_take[1]))
    return count/(36*36)


if __name__ == "__main__":
    main()