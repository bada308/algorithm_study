//이친수

#include <stdio.h>

int main(){
    int N;

    scanf("%d",&N);

    long int arr[N+1];
    arr[1] = 1;
    arr[2] = 1;

    for (int i = 3; i <= N; i++)
    {
        arr[i] = arr[i-1] + arr[i-2];
    }

    printf("%ld",arr[N]);

    return 0;
}

//처음 두자리는 10으로 고정
//10을 제외한 f(n) =>> 3번째 자리가 0일 때, 경우의 수가 f(n-1)/ 3번째 자리가 1일 때, 경우의 수가 f(n-2)이다. 즉, f(n) = f(n-1) + f(n-2), 피보나치 수열과 똑같다.