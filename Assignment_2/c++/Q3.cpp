#include<iostream>
#include<fstream>

using namespace std;

void matProduct(double[3][3],double[3][3],double[3][3]);
void matProduct(double[3][3],double[3][1],double[3][1]);
void matPrint(double[3][3]);
void matPrint(double[3][1]);
//------------------------* main function *-----------------------
// this function lode the mactrix from file and do some Operation
int main()
{
    fstream fileMatM;   // an object to read file 
    fstream fileMatN;
    fileMatM.open("data_file_for_Q3/Mat-M.txt"); // loding the file to IO object.
    fileMatN.open("data_file_for_Q3/Mat-N.txt");

    double M[3][3];   // make two Array to store the matrix from file.
    double N[3][3];

    for (int i = 0; i < 3; i++)  // reading file row.
    for (int j = 0; j < 3; j++)  // reading file col.
    fileMatM >> M[i][j];            // storing the element to array.
    for (int i = 0; i < 3; i++)    
    for (int j = 0; j < 3; j++)
    fileMatN >> N[i][j];
    
    cout<<"matrix M is : "<< endl;
    matPrint(M);   // print the matrix M.
    cout<<"matrix N is : "<< endl;
    matPrint(N);   // print the matrix N. 

    double Ans[3][3];  //  a variable to store the result of MxN matrix.
    matProduct(M,N,Ans); // calculating the MXN.
    matPrint(Ans); // pinting the result of MXN. 

    double Ans1[3][1];     // a variable to stroe the result of MXA matrix.
    double A[3][1]={{2},{-1},{4}}; // defining the matrix A.
    matProduct(M,A,Ans1); // calculating the MXA.
    matPrint(Ans1);   // printing the result of MXA.
    
}

//------------------------------* 2 overloaded matPrint functions *--------------------------------
// this function will print the matrix
void matPrint(double Array[3][3])
{
    cout<<endl;
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            cout<<Array[i][j]<<"\t";
        }
        cout<<endl;
    }
}

void matPrint(double Array[3][1])
{
    cout<<endl;
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<1;j++)
        {
            cout<<Array[i][j]<<"\t";
        }
        cout<<endl;
    }
}

//-------------------------------* 2 overloaded matProduct * ----------------------------------
// this function will take 3 argument  (A , B , Ans )  where AxB= Ans. 
void matProduct(double matA[3][3],double matB[3][3],double matC[3][3])
{
    for(int i=0;i<3;i++)
    for(int j=0;j<3;j++)
    {
        matC[i][j]=0;
        for(int k=0;k<3;k++)
        matC[i][j] += matA[i][k] * matB[k][j];
    }

}
void matProduct(double matA[3][3],double matB[3][1], double matC[3][1])
{
    for(int i=0;i<3;i++)
    for(int j=0;j<1;j++)
    {
        matC[i][j]=0;
        for(int k=0;k<3;k++)
        matC[i][j] += matA[i][k] * matB[k][j];
    }

}
//-------------------* output of this code is *--------------------------
// 1       2       4
// 6       9       -11
// -7      5       0

// 5       8       -1
// 4       8       2
// 0       4       -4

// 13      40      -13
// 66      76      56
// -15     -16     17

// 16
// -41
// -19