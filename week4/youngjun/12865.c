//평범한 배낭

#include <stdio.h>
#include <string.h>
#define Max(a,b) (((a) > (b)) ? (a) : (b))

int N,K;

int take(int things[][]){
    int dp[N+1][K+1];
    for(int i = 0; i < N; i++){
    dp[i][0] = 0;
    }
    for(int j = 0; j < K; j++){
    dp[0][j] = 0;
    }

    for (int m = 0; m <= N; m++)
    {
        for (int l = 0; l <= K; l++)
        {
            if (things[m][0] > m)
            {
                dp[m][l] = dp[m-1][l];
            }
            else{
                dp[m][l] = Max(dp[m-1][l], dp[m][l-things[m-1][0]] + things[m-1][1]);
            }
        }
        
    }

    return dp[N][K];
    
}
int main(){
    scanf("%d %d",&N,&K);

    int things[N][2];

    for (int i = 0; i < N; i++)
    {
        scanf("\n%d %d",&things[i][0],&things[i][1]);
    }

    printf("%d",take);
    
}