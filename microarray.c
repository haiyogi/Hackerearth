#include<stdio.h>
int main()
{
    int t;
    long n,i,small=0,k,a[100000];
    scanf("%d",&t);
    while(t>0)
    {
     scanf("%ld%ld",&n,&k);
     for(i=0;i<n;i++)
     scanf("%ld",&a[i]);
     small=a[0];
     for(i=1;i<n;i++)
     {
         if(small>a[i])
         small=a[i];
     }
	 if(small<k)
        printf("%ld\n",(k-small));
	 else
	 printf("%d\n",0);
        t--;
    }
    return 0;
}