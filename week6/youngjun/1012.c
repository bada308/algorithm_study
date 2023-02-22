//유기농 배추

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int T;
int M,N,K;
int X,Y;

void dfs(int field[][N],int x,int y,int visited[][N]){ //DFS 탐색
    visited[x][y] = 1;
    if(x>0)
    {
        if (field[x-1][y] == 1 && visited[x-1][y] == 0)
        {
            dfs(field,x-1,y,visited);
        }
    }
    if (x<M-1)
    {
        if (field[x+1][y] == 1 && visited[x+1][y] == 0)
        {
            dfs(field,x+1,y,visited);
        }
    }
    if (y>0)
    {
        if (field[x][y-1] == 1 && visited[x][y-1] == 0)
        {
            dfs(field,x,y+1,visited);
        }
    }
    if (y<N-1)
    {
        if (field[x][y+1] == 1 && visited[x][y+1] == 0)
        {
            dfs(field,x,y+1,visited);
        }
    }
    
}

int main(){

    scanf("%d",&T);
    getchar();
    int anum[T];

    for (int i = 0; i < T; i++)
    {
        int num = 0;
        scanf("%d %d %d",&M,&N,&K);
        getchar();
        int field[M][N];
        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < N; j++)
            {
                field[i][j] = 0;
            }
        
        }

    
        int visited[M][N];
        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < N; j++)
            {
                visited[i][j] = 0;
            }
        }
        for (int j = 0; j < K; j++)
        {
            scanf("%d %d",&X,&Y);
            field[X][Y] = 1;
            getchar();
        }
        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (field[i][j] == 1 && visited[i][j] == 0)
                {
                    dfs(field,i,j,visited);
                    num++;
                }
            }
        }
        anum[i] = num;
    }

    for (int i = 0; i < T; i++)
    {
        printf("%d\n",anum[i]);
    }

    return 0;
}

//
/*
    int** field;
    field = (int**)malloc(sizeof(int*)*(M));
    for (int i = 0; i < M; i++)
    {
        field[i] = (int*)malloc(sizeof(int)*N);
    }
    int** visited;

    visited = (int**)malloc(sizeof(int*)*(M));
    for (int i = 0; i < M; i++)
    {
        visited[i] = (int*)malloc(sizeof(int)*N);
    }

    for (int i = 0; i <= M; i++)
    {
        free(field[i]);
        free(visited[i]);
    }
    free(field);
    free(visited);
*/