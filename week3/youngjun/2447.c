//별 찍기

#include <stdio.h>
#include <string.h>

char table[6562][6562];
void origin_star(int y,int x);
void star(int n,int y,int x);


int main(){
    int n;
    scanf("%d",&n);
    memset(table,' ',sizeof(table));
    star(n,0,0);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%c",table[i][j]);
        }
        printf("\n");
        
    }
    return 0;
}

void origin_star(int y,int x){
    table[y][x] = '*';
    table[y][x+1] = '*';
    table[y][x+2] = '*';

    table[y+1][x] = '*';
    table[y+1][x+2] = '*';

    table[y+2][x] = '*';
    table[y+2][x+1] = '*';
    table[y+2][x+2] = '*';
}

void star(int n,int y,int x){

    if (n==3)
    {
        origin_star(y,x);
        return;
    }
    star(n/3,y,x);
    star(n/3,y,x+n/3);
    star(n/3,y,x+n/3*2);

    star(n/3,y+n/3,x);
    star(n/3,y+n/3,x+n/3*2);
    
    star(n/3,y+n/3*2,x);
    star(n/3,y+n/3*2,x+n/3);
    star(n/3,y+n/3*2,x+n/3*2);
}