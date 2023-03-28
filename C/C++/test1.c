#include <stdio.h>

void main(){
int a[10][10],b[10][10],c[10][10];
int i,n,j;

printf("enter the number value:\n");
scanf("%d",&n);
printf("Enter number:%d\n",n);
printf("Enter element of A matrix:2");
for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", & a[i][j]);
            printf("First matrix:%d\n",a[i][j]);
        }
        printf("\n");
    }
    
}
 