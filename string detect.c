#include <stdio.h>
#include<math.h>
void main()
{
    char a[100],b[100];
    gets(a);
    gets(b);
    int x=strlen(a);
    int y=strlen(b);
    int z=0;
    for(int i=0;i<x;i++)
    {
        for(int j=0;j<y;j++)
        {
            if(b[j]==a[i])
            {
                z++;
                break;
            }
        }
    }
    if(z<=y)
        printf("YES");
    else
        printf("NO");
}
