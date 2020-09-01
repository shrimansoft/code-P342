def main():

    # Q1. Solve :
	# x + 3y + 2z = 2
	# 2x + 7y + 7z = -1
	# 2x + 5y + 2z = 7
    # augmentedMatrixQ1 is:
    # | 1 3 2  2 |
    # | 2 7 7 -1 |
    # | 2 5 2  7 |
    
    augmentedMatrixQ1 =readMatrixFromFile("Data/augmentedMetrix_Q1.txt") # Reading augmented Matrix from file. This also give the number of rows and columns
    MatrixQ1 = getMatix(augmentedMatrixQ1) # Getting only the Matrix part out of the augmented matrix

    Beautifulprint(MatrixQ1,"Q1 matrix")
    Beautifulprint(augmentedMatrixQ1[0],"Q1 augmentedMatrix")
    Beautifulprint(Gauss_Jordan(*augmentedMatrixQ1),"Solution of Q1") # calling Gauss_jordan function

    # Q2. 
    # augmentedMatrixQ2 is:
    # | 0  2 5  1 |
    # | 3 -1 2 -2 |
    # | 1 -1 3  3 |

    augmentedMatrixQ2 =readMatrixFromFile("Data/augmentedMetrix_Q2.txt") # Reading augmented Matrix from file. This also gives the number of rows and columns
    MatrixQ2 = getMatix(augmentedMatrixQ2)

    Beautifulprint(MatrixQ2,"Q2 matrix")
    Beautifulprint(augmentedMatrixQ2[0],"Q2 augmentedMatrix")
    Beautifulprint(Gauss_Jordan(*augmentedMatrixQ2),"Solution of Q2") # calling Gauss_jordan function
 

    # Q3. 
    # augmentedMatrixQ3 is: 
    # |  1 -3  7 | 1 0 0 |
    # | -1  4 -7 | 0 1 0 |
    # | -1  3 -6 | 0 0 1 |

    augmentedMatrixQ3 =readMatrixFromFile("Data/augmentedMetrix_Q3txt") # Reading augmented Matrix from file. This also give the number of row and Columns 
    MatrixQ3 = getMatix(augmentedMatrixQ3) # Getting only the matrix part out of augmented matrix
    Beautifulprint(MatrixQ3,"Q3 matrix")
    Beautifulprint(augmentedMatrixQ3[0],"Q3 augmentedMatrix")
    
    inverseMatrix = Gauss_Jordan(*augmentedMatrixQ3) # calling Gauss_jordan function for inverse
    Beautifulprint(inverseMatrix,"Q3 Inverse Matrix ")


    # Checking the inverse
    Beautifulprint(matProduct(MatrixQ3,inverseMatrix),"Result of the product of metrics and its inverse") 









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
            flag = True # use flag to avoid using break.
            for r1,_ in enumerate(augmentedMatrix[r+1:]):
                if(augmentedMatrix[r1][r] > augmentedMatrix[r][r] and flag):
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


if __name__ == "__main__":
    main()




#Output of the code:

""" 
---* Q1 matrix *---
[1.0, 3.0, 2.0]
[2.0, 7.0, 7.0]
[2.0, 5.0, 2.0]

---* Q1 augmentedMatrix *---
[1.0, 3.0, 2.0, 2.0]
[2.0, 7.0, 7.0, -1.0]
[2.0, 5.0, 2.0, 7.0]

---* Solution of Q1 *---
[3.0]
[1.0]
[-2.0]

---* Q2 matrix *---
[0.0, 2.0, 5.0]
[3.0, -1.0, 2.0]
[1.0, -1.0, 3.0]

---* Q2 augmentedMatrix *---
[0.0, 2.0, 5.0, 1.0]
[3.0, -1.0, 2.0, -2.0]
[1.0, -1.0, 3.0, 3.0]

---* Solution of Q2 *---
[-2.0]
[-2.0]
[1.0]

---* Q3 matrix *---
[1.0, -3.0, 7.0]
[-1.0, 4.0, -7.0]
[-1.0, 3.0, -6.0]

---* Q3 augmentedMatrix *---
[1.0, -3.0, 7.0, 1.0, 0.0, 0.0]
[-1.0, 4.0, -7.0, 0.0, 1.0, 0.0]
[-1.0, 3.0, -6.0, 0.0, 0.0, 1.0]

---* Q3 Inverse Matrix  *---
[-3.0, 3.0, -7.0]
[1.0, 1.0, 0.0]
[1.0, 0.0, 1.0]

---* Result of the product of metrics and its inverse *---
[1.0, 0.0, 0.0]
[0.0, 1.0, 0.0]
[0.0, 0.0, 1.0]

"""