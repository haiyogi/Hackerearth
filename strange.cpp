#include<iostream>
//#include<algorithm>
using namespace std;
int main()
{
 int t;
 cin>>t;
 while(t--)
 {
 	int sum=0;
	long long n,x,max,k,u=0;
	 cin>>n;
	 cin>>k;
	 long long a[n],b[n];
	 for(int i=0;i<n;i++)
	 {
		 cin>>a[i];
	 }
	 for(int i=0;i<n;i++)
	 {
		 cin>>b[i];
	 }
	 max=b[0];
	 for(int i=0;i<n;i++)
	 {
	 	if(b[i]>max)
	    max=b[i];
	 }
	 max++;
	 for(int i=0;i<n;i++)
	 {
		  if(a[i]<max)
		 {
		 	x=0;
           x=max-a[i];
		   u+=(x*k);
		 }
	 }
   cout<<u<<endl;
 }
 
 
}