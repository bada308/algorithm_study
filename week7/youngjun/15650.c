//N과 M (2)

#include <stdio.h>

int N,M;

void BT(int k,int arr[M],int visited[N+1],int p){
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
        if (!visited[i] && (p < i)) //잘 생각해보기 //visited배열 없어도 풀어진다??
        {
            arr[k] = i;
            visited[i] = 1;
            BT(k+1,arr,visited,i);
            visited[i] = 0;
        }
        
    }
}

int main(){
    scanf("%d %d",&N,&M);
    int arr[M];
    
    int visited[N+1];
    for (int i = 0; i <= N; i++)
    {
        visited[i] = 0;
    }
    BT(0,arr,visited,0);
    
    return 0;
}