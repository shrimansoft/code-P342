#include<iostream>

using namespace std;


double * vacterSum( double a[3] ,double b[3]);
double dotProduct( double a[3] , double b[3]);

int main()
{
    double v1[3] = {1,2,-2} ;
    double v2[3] = {2,5,3};
    double v3[3] ={3,-4,-2};
    double v4[3] = {-3,6,0};


    cout<< "product of (1,2,-2) and (2,5,3)";
    cout<< dotProduct(v1,v2);
    cout<< "Vacter sum  of (1,2,-2) and (2,5,3)";
    cout<< vacterSum(v1,v2);
    cout<< "product of (3,-4,-2) and (-3,6,0)";
    cout<< dotProduct(v3,v4);
    cout<< "Vacter sum  of (3,-4,-2) and (-3,6,0)";
    cout<< vacterSum(v3,v4);


}


double* vacterSum( double a[3],double b[3])
{
    double temp[3] = {a[0]+b[0],a[1]+b[1],a[2]+b[2]};
    return temp;
}

double dotProduct(double a[3], double b[3])
{
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
}