//N과 M(4)

#include <stdio.h>
int N,M;

void BT(int k,int arr[M],int p){
    if (k == M)
    {
        printf("\n");
        for (int i = 0; i < M; i++)
        {
            printf("%d ",arr[i]);
        }
        return;
    }
    for (int i = 1; i <= N; i++)
    {
        if (p <= i)
        {
            arr[k] = i;
            BT(k+1,arr,i);
        }
    }
    
}

int main(){
    scanf("%d %d",&N,&M);
    int arr[M];
    
    BT(0,arr,0);
    
    return 0;
}