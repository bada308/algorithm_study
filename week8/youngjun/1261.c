//최단거리

#include <stdio.h>
#include <string.h>
int INF = 10000;


int M,N;

int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};

void dijkstra(int maze[][M+1],int answer[][M+1]){
    int front = 0, rear = 0;
    int q[M*N*4][2];
    q[front][0] = 1;
    q[front][1] = 1;
    rear++;
    answer[1][1] = 0; // 초기 거리값 = 0

    while (front < rear)
    {
        int cx = q[front][0];
        int cy = q[front][1];
        front++;

        for (int i = 0; i < 4; i++)
        {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            if (nx < 1 || nx > N || ny < 1 || ny > M)
                continue;
            if (maze[nx][ny] == 1) //벽을 지날때
            {
                if (answer[nx][ny] > answer[cx][cy] + 1)
                {
                    answer[nx][ny] = answer[cx][cy] + 1;
                    q[rear][0] = nx; // 이 시점에서 rear == front !!
                    q[rear][1] = ny;
                    rear++;
                }
            }
            else if (maze[nx][ny] == 0)
            {
                if (answer[nx][ny] > answer[cx][cy]) //빈 방을 지날 때
                {
                    answer[nx][ny] = answer[cx][cy];
                    q[rear][0] = nx;
                    q[rear][1] = ny;
                    rear++;
                }
            }
        }
    }
}

int main(){
    scanf("%d%2d",&M,&N);
    int maze[N+1][M+1];
    int answer[N+1][M+1];
    

    for (int i = 1; i <= N; i++)
    {
        getchar();
        for (int j = 1; j <= M; j++)
        {
            scanf("%1d",&maze[i][j]);
            answer[i][j] = INF;
        }
    }

    dijkstra(maze,answer);
    
    printf("\n%d",answer[N][M]);
    
    return 0;
}