//N과 M(1)

#include <stdio.h>

//k==M일 때를 기점으로 BT함수가 계속 리턴되면서 백트래킹 하는 흐름을 생각해보기
int N,M;

void BT(int k,int arr[M],int visited[N+1]){
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
        if (!visited[i])
        {
            arr[k] = i;
            visited[i] = 1;
            BT(k+1,arr,visited);
            visited[i] = 0; //백트래킹하면서 i를 다시 사용할 수 있도록 설정
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
    BT(0,arr,visited);
    
    return 0;
}