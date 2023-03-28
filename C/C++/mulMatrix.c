#include<stdio.h>

int main() {
    int a[12][10], b[12][12], c[12][12], n, i, j, k;

    printf("Enter the value of N (N <= 12): ");
    scanf("%d", & n);
    printf("Enter the elements of A Matrix: \n");

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("Enter element:a[%d][%d]:",a[i][j]);
            scanf("%d", & a[i][j]);    
        }
        
    }
    //here i'm printing A matrix
     printf("A Matrix: \n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("%d\t", a[i][j]);
        }
        printf("\n");
    }

    printf("Enter the elements of Matrix-B: \n");

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", & b[i][j]);
        }
    }
    //here i'm printing B matrix
    printf("B Matrix:\n");
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("%d\t",b[i][j]);
        }
        printf("\n");
    }
//here we are multiplying the two matrix
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            c[i][j] = 0;
            for (k = 0; k < n; k++) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    printf("The product of the two matrices is: \n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("%d\t", c[i][j]);
        }
        printf("\n");
    }
    return 0;
}
