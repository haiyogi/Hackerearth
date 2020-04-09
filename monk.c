#include <stdio.h>
int main()
{
	long n,a[100000],b[100000],c[100000];
	scanf("%ld",&n);
	for(long i=0;i<n;i++)
	 scanf("%ld",&a[i]);
	 for(long i=0;i<n;i++)
	 scanf("%ld",&b[i]);
	 for(long i=0;i<n;i++)
	 {
	     c[i]=a[i]+b[i];
	     printf("%ld ",c[i]);
	 }
}
	
