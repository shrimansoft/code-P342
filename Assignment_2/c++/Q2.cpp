#include<iostream>

using namespace std;


double * vacterSum( double a[3] ,double b[3]);
double dotProduct( double a[3] , double b[3]);
// --------------------------* main function *---------------------------
// this function run some tests.
int main()
{
    // here we define some vacters using Array.
    double v1[3] = {1,2,-2} ; 
    double v2[3] = {2,5,3};
    double v3[3] ={3,-4,-2};
    double v4[3] = {-3,6,0};


    cout<< "product of (1,2,-2) and (2,5,3)"<<endl;
    cout<< dotProduct(v1,v2)<<endl; // printing the dot Product between V_1 and V_2.
    cout<< "Vacter sum  of (1,2,-2) and (2,5,3)"<<endl;
    cout<< vacterSum(v1,v2)[0]<<" "<< vacterSum(v1,v2)[1]<<" "<<vacterSum(v1,v2)[2]<<endl;  // printing the sum between V_1 and V_2.
    cout<< "product of (3,-4,-2) and (-3,6,0)"<<endl;
    cout<< dotProduct(v3,v4)<<endl; // printing the dot Product between V_3 and V_4.
    cout<< "Vacter sum  of (3,-4,-2) and (-3,6,0)"<<endl;
    cout<< vacterSum(v3,v4)[0]<<" "<<vacterSum(v3,v4)[1]<<" "<<vacterSum(v3,v4)[2]<<endl; // printing the sum between V_3 and V_4.



}

//-----------------------* vacterSum function *-----------------------------
// this function will return the pointer of a array having the vecter sum of two
// vacter of its Argument.
double* vacterSum( double a[3],double b[3])
{
    double temp[3] = {a[0]+b[0],a[1]+b[1],a[2]+b[2]};
    return temp;
}

//-----------------------* dotProduct funciton *----------------------------
// this function will return a double value Containing the dot product of two vacters its argument
double dotProduct(double a[3], double b[3])
{
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
}

//---------------------* output of this code *-----------------------

// product of (1,2,-2) and (2,5,3)
// 6
// Vacter sum  of (1,2,-2) and (2,5,3)
// 3 7 1
// product of (3,-4,-2) and (-3,6,0)
// -33
// Vacter sum  of (3,-4,-2) and (-3,6,0)
// 0 2 -2