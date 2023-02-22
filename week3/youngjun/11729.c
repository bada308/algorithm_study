//하노이 탑

#include <stdio.h>
#include <string.h>

int Num_Hanoi(int n);
void Hanoi(int n,int start,int to,int finish);

int main(){
    int n;
    scanf("%d",&n);
    printf("%d\n",Num_Hanoi(n));
    Hanoi(n,1,2,3);
}

void Hanoi(int n,int start,int to,int finish){
    if (n==1)
    {
        printf("%d %d\n",start,finish);
        return;
    }
    Hanoi(n-1,start,finish,to);
    printf("%d %d\n",start,finish);
    Hanoi(n-1,to,start,finish);
    
}

int Num_Hanoi(int n){
    if(n==1){
        return 1;
    }
    return 2 * Num_Hanoi(n-1) + 1;
}