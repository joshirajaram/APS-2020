#include <stdio.h>
#include <stdlib.h>
#include<string.h>
int main()
{
    char val[]="0011100110011";
    char ptr[]="10";
    int i,j,k,count=0;
    int L1=strlen(val);
    int L2=strlen(ptr);
    for(i=0;i<L1-L2;i++)
    {
        j=0;k=i;
        while((val[k]==ptr[j])&&(j<L2))
        {
            k++;
            j++;
        }
        if(j==L2)
            count++;
    }
    printf("\nNo of times %s occurs is %d",ptr,count);
    return 0;
}
