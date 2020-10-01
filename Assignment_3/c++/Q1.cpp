#include<iostream>
#include<fstream>

using namespace std;

void matPrint(int numberOfRow,int numberOfCol,double Array[][numberOfCol])
{
    cout<<endl;
    for(int i=0;i<numberOfRow;i++)
    {
        for(int j=0;j<numberOfCol;j++)
        {
            cout<<Array[i][j]<<"\t";
        }
        cout<<endl;
    }
}

int main()
{
    fstream fileMatM;   // an object to read file 
    fileMatM.open("data_file_for_Q3/Mat-M.txt"); // loding the file to IO object.
    int numberOfRow, numberOfCol;
    fileMatM >> numberOfRow >> numberOfCol;

    double M[numberOfRow][numberOfCol];   // make two Array to store the matrix from file.

    for (int i = 0; i < numberOfRow; i++)  // reading file row.
    for (int j = 0; j < numberOfCol; j++)  // reading file col.
    fileMatM >> M[i][j];            // storing the element to array.

    matPrint(numberOfRow,numberOfCol,M);


}
