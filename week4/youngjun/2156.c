//포도주 시식

#include <stdio.h>
#define Max(a,b) (((a) > (b)) ? (a) : (b))

int gr(int N, int arr[]){
    int dp[N+1];

    dp[1] = arr[0];
    dp[2] = dp[1] + arr[1];

    if (N<=2)
    {
        return dp[N];
    }
    else {
        for (int i = 0; i <= N; i++)
        {
            dp[i] = dp[i-3] + arr[i-2] + arr[i-1];
            dp[i] = Max(dp[i],dp[i-2]+arr[i-1]);
            dp[i] = Max(dp[i],dp[i-1]);
        }
    }

    return dp[N];
}

int main(){
    int N;
    scanf("%d",&N);

    int dt[N];
    for (int i = 0; i < N; i++)
    {
        scanf("\n%d",&dt[i]);
    }

    printf("%d",gr(N,dt));
    
    return 0;
}