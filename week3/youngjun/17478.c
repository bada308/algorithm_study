//재귀함수가 뭔가요?

#include <stdio.h>

int N; //지역변수 선언

void P(n){
    for (int i = 0; i < n*4; i++)
    {
        printf("_");
    }
}

void K(n){
    if (n == 0)
    {
        return;
    }
    
    for (int i = 0; i < (n-1)*4; i++)
    {
        printf("_");
    }
    printf("라고 답변하였지.\n");
    K(n-1);
}

void F(n){
    if(n == N){
        P(n);
        printf("\"재귀함수가 뭔가요?\"\n");
        P(n);
        printf("\"재귀함수는 자기 자신을 호출하는 함수라네\"\n");
        P(n);
        printf("라고 답변하였지.\n");
        K(n);

        return;
    }

    P(n);
    printf("\"재귀함수가 뭔가요?\"\n");
    P(n);
    printf("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n");
    P(n);
    printf("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n");
    P(n);
    printf("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n");

    F(n+1);
}

int main(){
    scanf("%d",&N);
    printf("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n");
    F(0);

    return 0;
}