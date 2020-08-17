#include <iostream>            //  for cout
#include <cmath>              // for NAN

using namespace std;

double factorial(int);                    // Declaration of the function factorial.

int main()
{

    cout << " Factorail of 10 is : ";              // Some sample testing of function factorial.
    cout << factorial(10) << endl;
    cout << " Factorail of 15 is : ";
    cout << factorial(15) << endl;
    cout << " Factorail of 5 is  : ";
    cout << factorial(5) << endl;
    cout << " Factorail of -5 is : ";
    cout << factorial(-5) << endl;

}
// -------------*  factorial function *-------------------------------
double factorial(int num)
{
    if ( num < 0.0 )            // This will check whether a number is negative,if it is nagative then it  will return nan.
    return NAN;


    double count = 1;
    for(int i=1;i<= num;i++)     //This is simple for loop for factorial
    {
        count *= i; 
    
    }
    return count;   
}