/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{
    int t,n;
    long m;
    scanf("%d",&t);
    while(t>0)
    {
        scanf("%d%ld",&n,&m);
        if(m%n==0)
        printf("Yes\n");
        else
        printf("No\n");
        t--;
    }

    return 0;
}
