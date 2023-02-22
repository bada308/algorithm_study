//정수 삼각형

#include <stdio.h>
#include <stdlib.h>
#define Max(a,b) (((a) > (b)) ? (a) : (b))

int N;

int dp(int** wh){
    int sum[N][N];
    sum[0][0] = wh[0][0];

    for (int i = 1; i < N; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            if (j>0)
            {
                sum[i][j] = sum[i-1][j-1] + wh[i][j];
            }
            if (j==0)
            {
                sum[i][j] = sum[i-1][j] + wh[i][j];
            }
            
            sum[i][j] = Max(sum[i][j],sum[i-1][j] + wh[i][j]);
        }
    }
    int r = sum[N-1][0];
    for (int k = 1; k < N; k++)
    {
        r = Max(r,sum[N-1][k]);
    }
    
    return r;
}

int main(){
    scanf("%d",&N);

    //동적할당
    int** wh;
    wh = (int**)malloc(sizeof(int*)*N);
    for (int i = 0; i < N; i++)
    {
        wh[i] = (int*)malloc(sizeof(int)*N);
    }
    //

    for (int i = 0; i < N; i++)
    {
        getchar();
        for (int j = 0; j <= i; j++)
        {
            scanf("%d ",&wh[i][j]);
        }
    }

    printf("%d",dp(wh));

    //동적할당 해제
    for (int k = 0; k < N; k++)
    {
        free(wh[k]);
    }
    free(wh);
    //

    return 0;
}

/*
int** wh;
wh = (int**)malloc(sizeof(int*)*(N+1));
for (int i = 0; i < N; i++)
{
    wh[i] = (int*)malloc(sizeof(int)*(N+1)*2);
}
*/

/*
for (int k = 0; k <= N; k++)
    {
        free(wh[k]);
    }
    free(wh);
*/