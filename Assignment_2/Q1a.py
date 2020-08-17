

def main():
    points = [1,2,3,4,5,6]
    print( averageDistance(points))



def averageDistance(numArray):
    sum =0.0
    for i in range(0,6):
        for j in range(0,6):
            sum += abs(numArray[i] - numArray[j])
    return (sum/36)























if __name__ == "__main__":
    main()