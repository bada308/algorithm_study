//보물섬

#include <stdio.h>
#include <stdlib.h>

struct Node{
    int x;
    int y;
    int cnt;
    struct Node *next;
};

char **map;
int **visit;

int search_map(struct Node* head, int n, int m);

int main(void){
    int n, m;
    int cnt = 0, max = 0;
    struct Node * head;
    struct Node * new_node;
    
    scanf("%d %d", &n, &m);
    map = (char**)malloc(n*sizeof(char*));
    visit = (int**)calloc(n, sizeof(int*));
    for(int i=0; i<n; i++){
        map[i] = (char*)malloc(m*sizeof(char));
        scanf("%s", map[i]);
        visit[i] = (int*)calloc(m, sizeof(int));
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(map[i][j] == 'W')
                continue;
            
            head = (struct Node*)malloc(1*sizeof(struct Node));
            new_node = (struct Node*)malloc(1*sizeof(struct Node));
            head->next = new_node;
            new_node -> x = i;
            new_node -> y = j;
            new_node -> cnt = 0;
            new_node -> next = NULL;
            
            cnt = search_map(head, n, m);
            
            if(cnt > max){
                max = cnt;
            }
        }
    }
    printf("%d\n", max);
}

int search_map(struct Node* head, int n, int m){
    int max = 0;
    int x[4] = {1, -1, 0, 0};
    int y[4] = {0, 0, 1, -1};
    int X, Y;
    struct Node *temp, *new, *use;
    temp = head;
    temp = temp->next;
    use = temp;
    visit[temp->x][temp->y] = 1;
    
    while(head -> next != NULL){
        temp = head->next;
        if(temp == NULL)
            break;
        for(int i=0; i<4; i++){
            X = temp->x + x[i];
            Y = temp->y + y[i];
            if(X < 0 || X >= n || Y <0 || Y >= m){
                continue;
            }
            if(visit[X][Y] == 1 || map[X][Y] == 'W'){
                continue;
            }
            
            visit[X][Y] = 1;
            new = (struct Node*)malloc(1*sizeof(struct Node));
            new->x = X;
            new->y = Y;
            new->cnt = temp->cnt + 1;
            new->next = NULL;
            use->next = new;
            use = use->next;
            if(new->cnt > max)
                max = new->cnt;
            
        }

        if(temp->next == NULL)
            break;
        head->next = temp->next;
        free(temp);
    }
    
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            visit[i][j] = 0;
        }
    }
    return max;
}

/*
#include <stdio.h>
#include <string.h>
#include "QUEUE.h"

int M,N;

int bfs(char map[][N],char visited[][N],int x, int y){
    struct QUEUE* queue = createQueue(M*N);
    enqueue(queue,)
    visited[x][y] = 1;
}

int main(){
    scanf("%d %d",&M,&N);
    char map[M][N];
    for (int i = 0; i < M; i++)
    {
        getchar();
        for (int j = 0; j < N; j++)
        {
            scanf("%c",&map[i][j]);
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
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (map[i][j] == 'L' && visited[i][j] == 0)
            {
                bfs();
            }
        }
    }
    
}
*/