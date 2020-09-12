#----------* BeautifullPritnt function *---------
def Beautifulprint(matrix,name):
    print("---* "+name+" *---" )
    for row in matrix:
        print(row)
    print("")

#-------------* getMatrix function *----------------
# This function cut the Front square part of the augmented matirx.
def getMatix(augmantedMatrix):
    return list(map((lambda x : x[:len(augmantedMatrix[0])]), augmantedMatrix[0]))


#----------------* readMatrixFromFile function *--------------------
# This function read the file and also give the number of rows and Columns.
def readMatrixFromFile(fileName):
    with open(fileName, 'r') as f: # reading the file and store in M as list    
        M = [list(map(float,item.split())) for item in f.read().split('\n')]
    numberOfRow = len(M)
    numberOfCol = len(M[0])
    return (M,numberOfRow,numberOfCol)

#------------------* partial_pivot function *--------------------
# I use the Pseudocode in the Assignment with small changes
def partial_pivot(augmentedMatrix,numberOfRow,numberOfCal):
    for r,_ in enumerate(augmentedMatrix[:-1]):
        if abs(augmentedMatrix[r][r]) == 0:
            Beautifulprint(augmentedMatrix,"testpoint3")
            flag = True # use flag to avoid using break.
            for r1 in range(r+1,numberOfCal):
                if(augmentedMatrix[r1][r] > augmentedMatrix[r][r] and flag):
                    print("yes")
                    flag = False
                    temp = augmentedMatrix[r1]
                    augmentedMatrix[r1] =  augmentedMatrix[r]
                    augmentedMatrix[r] =temp
                
#------------------* Gauss_jordan function *-----------------------
# I use the Pseudocode in the Assignment with small changes 
def Gauss_Jordan(augmentedMatrix,numberOfRow,numberOfCol):
    partial_pivot(augmentedMatrix,numberOfRow,numberOfCol)
    for r,row in enumerate(augmentedMatrix):
        pivot = augmentedMatrix[r][r]
        augmentedMatrix[r] = list(map(lambda x : x / pivot,row)) # I use map rather than loop
        for r1,row1 in enumerate(augmentedMatrix):
            if r1!=r and augmentedMatrix[r1][r]!=0:
                factor =augmentedMatrix[r1][r]
                augmentedMatrix[r1] = list(map((lambda x :x[1]-(factor * x[0])),zip(augmentedMatrix[r],row1))) # I use map rather then loop
    return  list(map((lambda x : x[len(augmentedMatrix):]), augmentedMatrix))



#---------------* matProduct funtion *----------------------
# this if for chacking the inverse. This is the same function as Assignment 2 but work for any size of matrix.
def matProduct(matrixA,matrixB):
    numberOfRowA = len(matrixA)
    numberOfColA = len(matrixA[0])
    numberOfRowB = len(matrixB)
    numberOfColB = len(matrixB[0])
    if(numberOfColA==numberOfRowB):

        answerMatrix = list(list(0 for i in range(0,numberOfColB)) for i in range(0,numberOfRowA))
        for i in range(0,numberOfRowA):
            for j in range(0,numberOfColB):
                for k in range (0,numberOfColA):
                    answerMatrix[i][j] += matrixA[i][k]*matrixB[k][j]

        return answerMatrix
    else:
        return "This matrix can't multiply"

def catMatrics(A,B):
    
    if len(A) == len(B):
        return list(list( A[i][j] if j<len(A[0]) else B[i][j-len(A[0])] for j in range(0,len(A[0])+len(B[0]))) for i in range(0,len(A)))

    else:
        print("Can't Join these two metrics")


def replaceMatrix(augmentedMatrix,matrix):
    pice = cutMatrix(augmentedMatrix)
    return catMatrics(matrix,pice)


def cutMatrix(augmentedMatrix):
    return  list(map((lambda x : x[len(augmentedMatrix):]), augmentedMatrix))
