from lib.My_library import *


def main():

    mat = readMatrixFromFile("Data/augmentedMetrix_Q1.txt")  # reading Q1 as augmentedMatrix (A|b)
    Beautifulprint(mat[0],"Q1 augmanted Matrix (A|b) ")
    
    MatrixQ1 = getMatix(mat)  #  cutting only Matrix (A) part 
    Beautifulprint (MatrixQ1,"Q1 Matrix A ")

    Joind_LandU = LUdecompositionCol(MatrixQ1) # LUdecompositon give single Matrix Containing both L and U.
    Beautifulprint(Joind_LandU,"Single L U Matrix ")
    (L,U) = splitLU(Joind_LandU) # Splitting L and U from single Matrix to two Matrix in touple like (L,U)

    Beautifulprint(L,"L Matrix")
    Beautifulprint(U,"U Matrix")

    # solving for y where   Ly=b. so we have to make augmentedMatrix (L|b)

    augmantedMatrixLI = replaceMatrix(mat[0],L)  # here we replace A form augmentedMatrix(A|b) with L to get augmentedMatrix (L|b).
    Beautifulprint(augmantedMatrixLI,"augmentedMatrix (L|b)")


    matrixM = forwardSolver(augmantedMatrixLI) # solving (L|b) we get y

    # solving for x where Ux = y. so we have to make augmentedMatrix (U|y).

    augmantedMatrixUy = catMatrics(U,matrixM) # we join U and y
    Beautifulprint(augmantedMatrixUy,"augmentedMatrix (U|y)")

    vector_x = backwardSolver(augmantedMatrixUy) # solving (U|y) we get x
    Beautifulprint(vector_x,"solution of Q1")

    # Q2 finfing inverse 
    mat = readMatrixFromFile("Data/augmentedMetrix_Q2.txt") # reading augmentedMatrix (A|I) form file
    MatrixQ2 = getMatix(mat)  #  cutting only Matrix (A) part 
    Beautifulprint (MatrixQ2,"Q2 Matrix A ")

    Joind_LandU = LUdecompositionCol(MatrixQ2) # LUdecompositon give single Matrix Containing both L and U.
    Beautifulprint(Joind_LandU,"Single L U Matrix ")
    (L,U) = splitLU(Joind_LandU) # Splitting L and U from single Matrix to two Matrix in touple like (L,U)

    Beautifulprint(L,"L Matrix")
    Beautifulprint(U,"U Matrix")

    print("Determinant of the Matrix is : ",DetMatrix(U)) # Determinant of this matrix is not equal to zero
   
   
    # we have to solve AB = I where A = LU, there for LUB = I. let UB = M  
    # solving for M where  LM = I. so we have to make augmentedMatrix (L|I)

    augmantedMatrixLI = replaceMatrix(mat[0],L)  # here we replace A form augmentedMatrix(A|I) with L to get augmentedMatrix (L|I).
    Beautifulprint(augmantedMatrixLI,"augmentedMatrix (L|I)")


    matrixM = forwardSolver(augmantedMatrixLI) # solving (L|I) we get M

    # solving for B where UB = M . so we have to make augmentedMatrix (U|M).

    augmantedMatrixUM = catMatrics(U,matrixM) # we join U and M
    Beautifulprint(augmantedMatrixUM,"augmentedMatrix (U|y)")

    matrixB = backwardSolver(augmantedMatrixUM) # solving (U|M) we get B
    Beautifulprint(matrixB,"solution of Q2")

    # now we chack the result
    Matr = readMatrixFromFile("Data/augmentedMetrix_Q2.txt") # reading augmentedMatrix (A|I) form file
    Matrix_to_chechk = getMatix(Matr)  #  cutting only Matrix (A) part  
    Beautifulprint(Matrix_to_chechk,"rereaded the matrix")
    Beautifulprint(matProduct(Matrix_to_chechk,matrixB)," result of the product")







    

def DetMatrix(A):
    sum=0
    for i in range(0,len(A)):
        sum+= A[i][i]

    return sum

def LUdecompositionRow(A):
    size = len(A)
    partial_pivot(A,size,size)
    for i in range(0,size):
        for j in range(0,size):
            if(i>j):
                A[i][j]=sumFacter(A,i,j)/A[j][j]
            else:
                A[i][j]=sumFacter(A,i,j)
    return A
    

def LUdecompositionCol(A):
    size = len(A)
    partial_pivot(A,size,size)
    Beautifulprint(A,"test")
    for j in range(0,size):
        for i in range(0,size):
            
            if(i>j):
                A[i][j]=sumFacter(A,i,j)/A[j][j]
            else:
                A[i][j]=sumFacter(A,i,j)
    return A


def sumFacter(A,i,j):
    sum = 0.0
    for k in range(0,min(i,j)):
        sum += A[i][k]*A[k][j]
    return A[i][j] - sum


def splitLU(A):
    def tstU(A,i,j):
        if i<j:
            return 0.0
        else:
            return A[j][i]
    def tstL(A,i,j):
        if i==j:
            return 1.0
        elif i>j:
            return 0.0
        else:
            return A[j][i]
    
    U =list(list(tstU(A,i,j) for i in range(0,len(A[0]))) for j in range(0,len(A[0])))
    L =list(list(tstL(A,i,j) for i in range(0,len(A[0]))) for j in range(0,len(A[0])))

    return (L,U)


def forwardSolver(augmentedMatrix):
    numberOfCol = len(augmentedMatrix[0])
    numberOfRow = len(augmentedMatrix)
    def sum(A,i,j):
        sum = 0
        for k in range(0,i):
            sum += A[i][k]*A[k][j]
        return sum

    for i in range(0,numberOfRow):
        for j in range(numberOfRow,numberOfCol):
            augmentedMatrix[i][j] = (augmentedMatrix[i][j]-sum(augmentedMatrix,i,j))/augmentedMatrix[i][i]
    return cutMatrix(augmentedMatrix)
        
def backwardSolver(augmentedMatrix):
    numberOfCol = len(augmentedMatrix[0])
    numberOfRow = len(augmentedMatrix)
    def sum(A,i,j):
        sum = 0
        for k in range(len(A)-1,i,-1):
            sum += A[i][k]*A[k][j]
        return sum

    for i in reversed(range(0,numberOfRow)):
        for j in range(numberOfRow,numberOfCol):
            augmentedMatrix[i][j] = (augmentedMatrix[i][j]-sum(augmentedMatrix,i,j))/augmentedMatrix[i][i]
    return  list(map(list,list(map(reversed, cutMatrix (augmentedMatrix)))))
        
if __name__ == "__main__":
    main()


# output of the code 
# ---* Q1 augmanted Matrix (A|b)  *---
# [1.0, 0.0, 1.0, 2.0, 6.0]
# [0.0, 1.0, -2.0, 0.0, -3.0]
# [1.0, 2.0, -1.0, 0.0, -2.0]
# [2.0, 1.0, 3.0, -2.0, 0.0]

# ---* Q1 Matrix A  *---
# [1.0, 0.0, 1.0, 2.0]
# [0.0, 1.0, -2.0, 0.0]
# [1.0, 2.0, -1.0, 0.0]
# [2.0, 1.0, 3.0, -2.0]

# ---* test *---
# [1.0, 0.0, 1.0, 2.0]
# [0.0, 1.0, -2.0, 0.0]
# [1.0, 2.0, -1.0, 0.0]
# [2.0, 1.0, 3.0, -2.0]

# ---* Single L U Matrix  *---
# [1.0, 0.0, 1.0, 2.0]
# [0.0, 1.0, -2.0, 0.0]
# [1.0, 2.0, 2.0, -2.0]
# [2.0, 1.0, 1.5, -3.0]

# ---* L Matrix *---
# [1.0, 0.0, 0.0, 0.0]
# [0.0, 1.0, 0.0, 0.0]
# [1.0, 2.0, 1.0, 0.0]
# [2.0, 1.0, 1.5, 1.0]

# ---* U Matrix *---
# [1.0, 0.0, 1.0, 2.0]
# [0.0, 1.0, -2.0, 0.0]
# [0.0, 0.0, 2.0, -2.0]
# [0.0, 0.0, 0.0, -3.0]

# ---* augmentedMatrix (L|b) *---
# [1.0, 0.0, 0.0, 0.0, 6.0]
# [0.0, 1.0, 0.0, 0.0, -3.0]
# [1.0, 2.0, 1.0, 0.0, -2.0]
# [2.0, 1.0, 1.5, 1.0, 0.0]

# ---* augmentedMatrix (U|y) *---
# [1.0, 0.0, 1.0, 2.0, 6.0]
# [0.0, 1.0, -2.0, 0.0, -3.0]
# [0.0, 0.0, 2.0, -2.0, -2.0]
# [0.0, 0.0, 0.0, -3.0, -6.0]

# ---* solution of Q1 *---
# [1.0]
# [-1.0]
# [1.0]
# [2.0]

# ---* Q2 Matrix A  *---
# [0.0, 2.0, 8.0, 6.0]
# [0.0, 0.0, 1.0, 2.0]
# [0.0, 1.0, 0.0, 1.0]
# [3.0, 7.0, 1.0, 0.0]

# ---* testpoint3 *---
# [0.0, 2.0, 8.0, 6.0]
# [0.0, 0.0, 1.0, 2.0]
# [0.0, 1.0, 0.0, 1.0]
# [3.0, 7.0, 1.0, 0.0]

# yes
# ---* testpoint3 *---
# [3.0, 7.0, 1.0, 0.0]
# [0.0, 0.0, 1.0, 2.0]
# [0.0, 1.0, 0.0, 1.0]
# [0.0, 2.0, 8.0, 6.0]

# yes
# ---* test *---
# [3.0, 7.0, 1.0, 0.0]
# [0.0, 1.0, 0.0, 1.0]
# [0.0, 0.0, 1.0, 2.0]
# [0.0, 2.0, 8.0, 6.0]

# ---* Single L U Matrix  *---
# [3.0, 7.0, 1.0, 0.0]
# [0.0, 1.0, 0.0, 1.0]
# [0.0, 0.0, 1.0, 2.0]
# [0.0, 2.0, 8.0, -12.0]

# ---* L Matrix *---
# [1.0, 0.0, 0.0, 0.0]
# [0.0, 1.0, 0.0, 0.0]
# [0.0, 0.0, 1.0, 0.0]
# [0.0, 2.0, 8.0, 1.0]

# ---* U Matrix *---
# [3.0, 7.0, 1.0, 0.0]
# [0.0, 1.0, 0.0, 1.0]
# [0.0, 0.0, 1.0, 2.0]
# [0.0, 0.0, 0.0, -12.0]

# Determinant of the Matrix is :  -7.0
# ---* augmentedMatrix (L|I) *---
# [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
# [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]
# [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0]
# [0.0, 2.0, 8.0, 1.0, 0.0, 0.0, 0.0, 1.0]

# ---* augmentedMatrix (U|y) *---
# [3.0, 7.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0]
# [0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0]
# [0.0, 0.0, 1.0, 2.0, 0.0, 0.0, 1.0, 0.0]
# [0.0, 0.0, 0.0, -12.0, 0.0, -2.0, -8.0, 1.0]

# ---* solution of Q2 *---
# [-0.24999999999999997, 1.6666666666666663, -1.8333333333333337, 0.3333333333333333]
# [0.08333333333333333, -0.6666666666666666, 0.8333333333333334, 0.0]
# [0.16666666666666666, -0.33333333333333326, -0.3333333333333333, 0.0]
# [-0.08333333333333333, 0.6666666666666666, 0.16666666666666666, -0.0]

# ---* rereaded the matrix *---
# [0.0, 2.0, 8.0, 6.0]
# [0.0, 0.0, 1.0, 2.0]
# [0.0, 1.0, 0.0, 1.0]
# [3.0, 7.0, 1.0, 0.0]

# ---*  result of the product *---
# [1.0, 8.881784197001252e-16, 2.220446049250313e-16, 0.0]
# [0.0, 1.0, 0.0, 0.0]
# [0.0, 0.0, 1.0, 0.0]
# [2.7755575615628914e-17, -2.220446049250313e-16, -2.7755575615628914e-16, 1.0