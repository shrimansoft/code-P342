#include <iostream>  // cin , cout 
#include <cmath> // abs(),

using namespace std;

double averageDistance(double* );

//-------------------------* main function to run tests *-------------------------
int main()
{
    double points1[6] = {1,2,3,4,5,6};    // double[] varible to store the points with unit distance 
    cout<<"Average distance of points [ 1 , 2, 3 , 4, 5 ,6 ] is :" << averageDistance(points1)<<endl;

    double points2[6] = {3,4,5,6,7,8};   // double[] variable store points with unit distance (displaced by 2 unit)
    cout<<"Average distance of points [ 3 , 4, 5 ,6 , 7, 8 ] is :" << averageDistance(points2)<<endl;
}

//-------------------------* averageDistance funtion to find the averageDistance between 6 points *-------------------------
double  averageDistance(double a[])
{
    double sum=0;           //  Variable to store the sum during loop
    for(int i=0;i<6;i++)    //  fixing one of the points out of six
    for(int j=0;j<6;j++)    //  Running over the rest of the points including fixed point
    {
        sum+= abs(a[j]-a[i]);    // Adding the absolute distance between the points.
    }
    return (sum/36);         // returing the average distance of points.
}

//------------------------* Output of the code *--------------------------------------------
//Average distance of points [ 1 , 2, 3 , 4, 5 ,6 ] is :1.94444
//Average distance of points [ 3 , 4, 5 ,6 , 7, 8 ] is :1.94444