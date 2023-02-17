//피보나치 수열

#include <stdio.h>

int array[41];

int fibonacci(int n){

    if (n == 0) {
        return 0;
    }
    else if (n == 1) {
        return 1;
    }
    for (int i = 2; i <= n; i++)
    {
        array[i] = array[i-1] + array[i-2];
    }
    return array[n];
}


int main(){
    int T;
    scanf("%d",&T);
    int N_array[T];
    for (int i = 0; i < T; i++)
    {
        scanf("\n%d",&N_array[i]);
    }
    array[0] = 0;
    array[1] = 1;
    
    //N_array = (int*)malloc(sizeof(int)*T);

    for (int j = 0; j < T; j++)
    {
        if (N_array[j] == 0)
        {
            printf("%d %d\n",1,0);
        }else if (N_array[j] == 1){
            printf("%d %d\n",0,1);
        }else printf("%d %d\n",fibonacci(N_array[j]-1),fibonacci(N_array[j]));
    }
    return 0;
}
 /*#include <stdio.h>

int num0,num1 = 0;

int fibonacci(int n) {
    if (n == 0) {
        num0++;
        return 0;
    } else if (n == 1) {
        num1++;
        return 1;
    } else return fibonacci(n-1) + fibonacci(n-2);
}

int main(){
    int T;
    scanf("%d",&T);
    int N_array[T];
    for (int i = 0; i < T; i++)
    {
        scanf("\n%d",&N_array[i]);
    }
    
    //N_array = (int*)malloc(sizeof(int)*T);

    for (int j = 0; j < T; j++)
    {
        num0 = 0;
        num1 = 0;
        fibonacci(N_array[j]);
        printf("%d %d\n",num0,num1);
    }
    return 0;
}*/
