//스타트와 링크

#include <stdio.h>
#define minus(x, y) (((x) > (y)) ? (x-y) : (y-x))

int n, cap[20][20];
int team[20]; // 스타트 팀와 링크 팀을 구분 짓기 위한 배열
//int index = 0; // team 배열의 index
int min = 100;

void calculate() {
	int a1 = 0, b1 = 0; // 1이 스타트 팀일 때
	int a2 = 0, b2 = 0; // 0이 스타트 팀일 때

	for (int i = 0; i < n; i++)
    {
		for (int j = 0; j < n; j++)
        {
			if (i == j)
				continue;
			if (team[i] == 1 && team[j] == 1) {
				a1 += cap[i][j];
				a2 += cap[j][i];
			}
			if (team[i] == 0 && team[j] == 0) {
				b1 += cap[i][j];
				b2 += cap[j][i];
			}
		}
	}

	int gap1 = minus(a1, b1);
	int gap2 = minus(a2, b2);

	if (gap1 < min)
		min = gap1;
	if (gap2 < min)
		min = gap2;
}
void comb(int depth, int isChoose, int cnt) {

	if (isChoose == 1)
		team[depth] = 1;
	else
		team[depth] = 0;

	if (depth - cnt == n / 2)
		return;
	else {
		if (depth == n - 1 || cnt == n / 2) {
			calculate();
			return;
		}
	}

	// O를 고르면
	comb(depth + 1, 1, cnt + 1);
	// X를 고르면
	comb(depth + 1, 0, cnt);

	return;
}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
    {
        getchar();
		for (int j = 0; j < n; j++)
        {
			scanf("%d", &cap[i][j]);
        }    
    }
	comb(0, 1, 1);

	printf("%d", min);
}



/*
#include <stdio.h>
int N;
int num = 0;

int team(int sol[N/2],int arr[][N]){

}

int BT(int k,int sol[N/2],int visited[N+1],int p,int arr[][N]){
    if (k == N/2 && team(sol,arr) < num)
    {
        num = team(sol,arr);
        return;
    }
    for (int i = 1; i <= N; i++)
    {
        if (!visited[i] && (p < i))
        {
            sol[k] = i;
            visited[i] = 1;
            BT(k+1,sol,visited,i,arr);
            visited[i] = 0;
        }
        
    }
}

int main(){
    scanf("%d",&N);
    int sol[N/2];
    int arr[N][N];
    for (int i = 0; i < N; i++)
    {
        getchar();
        for (int j = 0; j < N; j++)
        {
            scanf("%d ",&arr[i][j]);
        }
    }
    int visited[N+1];
    for (int i = 0; i <= N; i++)
    {
        visited[i] = 0;
    }
    
    
    
}
*/