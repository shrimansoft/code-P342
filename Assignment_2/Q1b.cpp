#include<iostream> // cin ,cout
#include<cmath> // abs()

using namespace std;

double averageDistance(double[36][2]);
void setPoints(double[36][2]);
void printPoints(double [36][2]);

//-------------------------* main function *-------------------------
int main()
{
    double points[36][2];   // Declaring a array to stored grid
    setPoints(points);      // Setting the values to the grid   
    printPoints(points);    // Pringing grid to stdout 


    //averageDistance(double [36][2]) function take the pointer of the array as its argument 
    //and return the average distance between the points.
    cout<<" Average distance between points is : "<< averageDistance(points) <<endl; 

}
//-------------------------* averageDistance function  *-------------------------
double averageDistance(double points[36][2])
{
    double count=0; // double variable to store the sum of distance.
    for(int i=0;i<36;i++)  
    for(int j=0;j<36;j++)
    {
        count+= (abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]));

    }
    return count/(36*36);
}
//-------------------------* setPoints function *-------------------------
void setPoints(double points[36][2])
{
    for(int i=0;i<36;i++)
    {
        points[i][0]=(i%6)+1;
        points[i][1]=(i/6)+1;
    }
}
//-------------------------* printPoints function *-------------------------
void printPoints(double points[36][2])
{
    cout<<endl;
    for(int i=0;i<6;i++)
    {
        for(int j=0;j<6;j++)
        {
            cout<<"{"<<points[(i*6)+j][0]<<","<<points[(i*6)+j][1]<<"}";
        }
        cout<<endl;
    }
}

//-------------------------* Code output *-------------------------
// $ ./Q1b.cpp                              
// {1,1}{2,1}{3,1}{4,1}{5,1}{6,1}
// {1,2}{2,2}{3,2}{4,2}{5,2}{6,2}
// {1,3}{2,3}{3,3}{4,3}{5,3}{6,3}
// {1,4}{2,4}{3,4}{4,4}{5,4}{6,4}
// {1,5}{2,5}{3,5}{4,5}{5,5}{6,5}
// {1,6}{2,6}{3,6}{4,6}{5,6}{6,6}
// Average distance between points is : 3.88889