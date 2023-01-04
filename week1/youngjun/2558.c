#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    int A;
    char B[4]; // 널문자 조심
    scanf("%d %s",&A,B);

    printf("%d\n",A * (B[2] - '0'));
    printf("%d\n",A * (B[1] - '0'));
    printf("%d\n",A * (B[0] - '0'));
    printf("%d\n",A * atoi(B));
    
}