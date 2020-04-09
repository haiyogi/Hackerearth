#include <stdio.h>
 
int main(){
	long unsigned int n,count=0;
		while(scanf("%lu",&n)!=EOF){
		while(n!=0){
			n=n&(n-1);
			count++;
		}
		printf("%ld\n", count);
		count=0;
	}
}
	
