#----------------------* main function *--------------------------------------
def main():
    with open("data_file_for_Q3/Mat-M.txt", 'r') as f: # reading the file and store in M as list    
        M = [map(float,item.split()) for item in f.read().split('\n')]
    with open("data_file_for_Q3/Mat-N.txt",'r') as f: # reading the file and store in N as list
        N = [map(float,item.split()) for item in f.read().split('\n')]

    print(M) # printing the list M 
    print(N) # print the list N

    print(matProduct(M,N)) # here we call the function matProduct() which do cros product of matrix. we also print the result
    A = [[2],[-1],[4]] # defining the matrix A
    print(matProductV(M,A)) # here we call the function matProductV() which do matrix and vacter product.we also print the result.
#------------------------------* matProductV function * ----------------------------
# this function will do matrix and Vactor product
def matProductV(matA,matB):
    matC = [[0],[0],[0]]
    for i in range(0,3):
        for j in range(0,1):
            for k in range (0,3):
                matC[i][j] += matA[i][k]*matB[k][j]
    return matC

#---------------------------------* matProduct function *----------------------------
# this function will do matrix-matrix product.  
def matProduct(matA,matB):
    matC = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0,3):
        for j in range(0,3):
            for k in range (0,3):
                matC[i][j] += matA[i][k]*matB[k][j]
    return matC



if __name__ == "__main__":
    main()

#--------------------------* output of this code *-------------------------------
# [[1.0, 2.0, 4.0], [6.0, 9.0, -11.0], [-7.0, 5.0, 0.0]]
# [[5.0, 8.0, -1.0], [4.0, 8.0, 2.0], [0.0, 4.0, -4.0], []]
# [[13.0, 40.0, -13.0], [66.0, 76.0, 56.0], [-15.0, -16.0, 17.0]]
# [[16.0], [-41.0], [-19.0]]