#include <iostream>

using namespace std;

int main()
{
    double count = 0;
    for(int i=1;((double) 1/i) > 0.001;i++)
    {
        // cout << i ; 
        count +=((double)1/i)  ; 
        // cout << endl;
    }
    cout << count << endl;

}