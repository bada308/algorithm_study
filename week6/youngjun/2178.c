//미로 탐색

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define Min(a,b) (((a) < (b)) ? (a) : (b))

int N,M;
/*
int bfs(int** maze,int x,int y){
    struct QUEUE* queue = createQueue(N*M);
    enqueue(queue,)
}*/

int dfs(int maze[][M],int x,int y,int visited[][M],int* num_s){
    if (x == N-1 && y == M-1)
    {
        *num_s = Min(maze[x][y],*num_s);
    }
    
    visited[x][y] = 1;
    if(x>0)
    {
        if (maze[x-1][y] == 1 && visited[x-1][y] == 0)
        {
            maze[x-1][y] = maze[x][y] + 1;
            dfs(maze,x-1,y,visited,num_s);
        }
    }
    if (x<M-1)
    {
        if (maze[x+1][y] == 1 && visited[x+1][y] == 0)
        {
            maze[x+1][y] = maze[x][y] + 1;
            dfs(maze,x+1,y,visited,num_s);
        }
    }
    if (y>0)
    {
        if (maze[x][y-1] == 1 && visited[x][y-1] == 0)
        {
            maze[x][y-1] = maze[x][y] + 1;
            dfs(maze,x,y-1,visited,num_s);
        }
    }
    if (y<N-1)
    {
        if (maze[x][y+1] == 1 && visited[x][y+1] == 0)
        {
            maze[x][y+1] = maze[x][y] + 1;
            dfs(maze,x,y+1,visited,num_s);
        }
    }
    return *num_s;
}

int main(){
    scanf("%d %d",&N,&M);
    int num = N*M;
    int* num_s = &num;

    int maze[N][M];
    for (int i = 0; i < N; i++)
    {
        getchar();
        for (int j = 0; j < M; j++)
        {
            scanf("%1d",&maze[i][j]);
        }
    }
    maze[N-1][M-1] = N * M;
    int visited[N][M];
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            visited[i][j] = 0;
        }
    }
    printf("%d",dfs(maze,0,0,visited,num_s));

    return 0;
}