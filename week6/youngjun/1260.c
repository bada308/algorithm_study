//DFS와 BFS

#include <stdio.h>
#include <string.h>
#include "QUEUE.h"  //c언어는 따로 지원해주는 헤더파일이 없기 때문에 다른 사람의 코드를 헤더파일로 저장했음
int node;
int line;

void corr(int graph[][line],int a,int b,int i){ //graph배열을 직관적으로 보이게 정리해주는 재귀함수
    if (!graph[a][i])
    {
        graph[a][i] = b;
    }
    else corr(graph,a,b,i+1);
    if (i>0)
    {
        for (int k = 0; k < i; k++){
            for (int j = k+1; j <= i; j++)
            {
                if (graph[a][k] > graph[a][j])
                {
                    int temp = graph[a][k];
                    graph[a][k] = graph[a][j];
                    graph[a][j] = temp;
                }
                
            }
        
        }
    }
    
}

void dfs(int graph[][line],int v,int visited[]){ //DFS 탐색
    visited[v] = 1;
    printf("%d ",v);
    for (int i = 0; i < line; i++)
    {
        if (!visited[graph[v][i]])
        {
            v = graph[v][i];
            dfs(graph,v,visited);
        }
        
    }
    
}

void bfs(int graph[][line],int v,int visited[]){
    
    struct Queue* queue = createQueue(node);
    enqueue(queue,v);
    printf("%d ",v);
    visited[v] = 1;
    while (queue -> size)
    {
        v = dequeue(queue); //먼저 들어온 노드를 꺼낼 수 있음
        for (int i = 0; i < sizeof(graph[v]) / sizeof(int); i++)
        {   
            if (!visited[graph[v][i]])
            {
                enqueue(queue,graph[v][i]);
                printf("%d ",graph[v][i]);
                visited[graph[v][i]] = 1;
            }
            
        }
        
    }
    

}

int main(){
    int start;
    int a,b;

    scanf("%d %d %d",&node,&line,&start);

    int graph[node+1][line];
    for (int i = 0; i < node+1; i++)
    {
        for (int j = 0; j < line; j++)
        {
            graph[i][j] = 0;
        }
        
    }
    

    for (int i = 0; i < line; i++)
    {
        getchar();
        scanf("%d %d",&a,&b);
        corr(graph,a,b,0);
        corr(graph,b,a,0);
    }

    int visited[1001] = {1, };

    printf("\n");
    dfs(graph,start,visited);
    printf("\n");
    bfs(graph,start,visited);
    
    return 0;
}