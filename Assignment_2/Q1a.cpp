#include <iostream>  // cin , cout 
#include <cmath> // abs(),

using namespace std;

double averageDistance(double* );


int main()
{
    double points[6] = {1,2,3,4,5,6};
    cout<<"Average distance of points [ 1 , 2, 3 , 4, 5 ,6 ] is :" << averageDistance(points)<<endl;
}


double  averageDistance(double a[])
{
    double sum = 0;
    for(int i=0;i<6;i++)
    for(int j=0;j<6;j++)
    {
        sum+= abs(a[j]-a[i]);
    }
    return (sum/36);
}