//적록 색약

#include <stdio.h>
#include <string.h>
int N;

void dfs(char area[][N],int x,int y,int visited[][N]){
    visited[x][y] = 1;
    
    if (x>0)
    {
        if(area[x-1][y] == area[x][y] && visited[x-1][y] == 0){
            dfs(area,x-1,y,visited);
        }
    }
    if (y>0)
    {
        if(area[x][y-1] == area[x][y] && visited[x][y-1] == 0){
            dfs(area,x,y-1,visited);
        }
    }
    if (x<N-1)
    {
        if(area[x+1][y] == area[x][y] && visited[x+1][y] == 0){
            dfs(area,x+1,y,visited);
        }
    }
    if (y<N-1)
    {
        if(area[x][y+1] == area[x][y] && visited[x][y+1] == 0){
            dfs(area,x,y+1,visited);
        }
    }
}

int main(){
    scanf("%d",&N);

    char area[N][N];
    for (int i = 0; i < N; i++)
    {
        getchar();
        for (int j = 0; j < N; j++)
        {
            scanf("%s",&area[i][j]);
        }
    }
    int visited[N][N];

    for (int i = 0; i < 2; i++)
    {
        int num = 0;
        if (i == 1)
        {
            for (int j = 0; j < N; j++)
            {
                for (int l = 0; l < N; l++)
                {
                    if (area[j][l] == 'R')
                    {
                        area[j][l] = 'G';
                    }
                }
                
            }
            
        }
        
        for (int l = 0; l < N; l++)
        {
            for (int j = 0; j < N; j++)
            {
                visited[l][j] = 0;
            }
        }

        for (int l = 0; l < N; l++)
        {
            for (int j = 0; j < N; j++)
            {
                if (!visited[l][j])
                {
                    dfs(area,l,j,visited);
                    num++;
                }
            }
        }
        printf("%d ",num);
    }
    
    return 0;
}