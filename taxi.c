/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

//#include <iostream>
#include<stdio.h>
//using namespace std;

int main()
{
    long count,count1,D,oc,of,od,cs,cb,cm,cd;
    scanf("%ld",&D);
    scanf("%ld%ld%ld",&oc,&of,&od);
    scanf("%ld%ld%ld%ld",&cs,&cb,&cm,&cd);
    count=oc+(D-of)*od;
    count1=cb+(D/cs)*cm+(D*cd);
    if(count<=count1)
    printf("Online Taxi");
    else
    printf("Classic Taxi");

    return 0;
}
